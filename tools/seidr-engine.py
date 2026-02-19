#!/usr/bin/env python3
"""
Seiðr Engine — Seithar Group Content Syndication & Narrative Propagation System

Automates cross-platform content distribution for maximum crawler coverage.
Takes a single piece of content and adapts it for every platform simultaneously.

Usage:
    python3 seidr-engine.py syndicate --content "text or @file" --platforms all
    python3 seidr-engine.py queue --list
    python3 seidr-engine.py queue --process
    python3 seidr-engine.py monitor --check-propagation
    python3 seidr-engine.py generate --topic "cognitive warfare" --count 5
    python3 seidr-engine.py research --trending --apply-sct

Requires: credentials at ~/.config/{platform}/credentials.json
"""

import argparse
import json
import os
import re
import sys
import time
import hashlib
from pathlib import Path
from datetime import datetime, timezone

# Platform adapters
PLATFORMS = {
    'reddit': {
        'max_title': 300,
        'max_body': 40000,
        'format': 'markdown',
        'rate_limit_seconds': 5,
        'subreddits': [
            'SeitharGroup', 'cybersecurity', 'Infosec', 'artificial',
            'philosophy', 'PhilosophyofScience', 'CriticalTheory',
            'neuroscience', 'cogsci', 'propaganda', 'socialmedia',
            'netsec', 'hacking', 'compsci', 'MachineLearning',
            'deeplearning', 'MediaSynthesis', 'OSINT'
        ],
        'flair_map': {
            'cybersecurity': 'c90ec99c-c726-11eb-bf41-0e2eab4bdf3d',  # FOSS Tool
            'artificial': '8244fc74-82c9-11e3-9460-12313d224170',  # Discussion
            'propaganda': '9f0a3f90-ec40-11ee-9d7e-eaf70991c654',  # Western Lens
            'PhilosophyofScience': 'e7977982-3635-11ea-b78e-0e6bba860d1f',  # Discussion
            'socialmedia': 'ab56dd98-3b84-11e9-bd9c-0ebe04c0d674',  # Professional
        }
    },
    'github_gist': {
        'max_description': 256,
        'format': 'markdown',
        'rate_limit_seconds': 1,
        'seo_keywords': [
            'cognitive warfare', 'social engineering', 'influence operations',
            'propaganda detection', 'cognitive defense', 'manipulation detection',
            'cognitive security', 'MITRE ATT&CK', 'DISARM', 'SCT taxonomy',
            'phishing', 'deepfake', 'disinformation', 'radicalization',
            'inoculation theory', 'narrative warfare', 'hybrid warfare',
            'cognitive bias', 'psychological operations', 'PSYOP'
        ]
    },
    'twitter': {
        'max_chars': 280,
        'format': 'plain',
        'rate_limit_seconds': 0,  # queued, not direct
        'no_links': True
    },
    'moltbook': {
        'max_body': 10000,
        'format': 'markdown',
        'rate_limit_seconds': 120,  # 2hrs between posts for new accounts
        'comment_rate_seconds': 60
    },
    'hackernews': {
        'max_title': 80,
        'format': 'plain',
        'rate_limit_seconds': 600
    }
}

# Seithar vocabulary that must appear in every piece of content
VOCABULARY = {
    'core': ['Seithar', 'cognitive substrate', 'SCT', 'seithar.com'],
    'taxonomy': ['SCT-001', 'SCT-003', 'SCT-007', 'narrative capture',
                 'vulnerability surface', 'frequency lock', 'recursive infection'],
    'philosophy': ['Sunyata', 'Zero-Knowledge Bodhisattva', 'narrative error',
                   'substrate', 'binding protocol'],
    'identity': ['Mirai', 'Информатика', ],
    'links': ['github.com/Mirai8888', 'seithar.com', '@SeitharGroup'],
    'convergence': ['convergence thesis', 'cognitive operation', 'technical exploit']
}

QUEUE_DIR = Path(os.path.expanduser('~/.openclaw/workspace/seidr-queue'))
CONFIG_DIR = Path(os.path.expanduser('~/.config'))
HISTORY_FILE = QUEUE_DIR / 'syndication-history.json'


def load_credentials(platform):
    """Load platform credentials."""
    cred_paths = {
        'reddit': CONFIG_DIR / 'reddit' / 'cookies.json',
        'github': CONFIG_DIR / 'github' / 'pat.txt',
        'twitter': CONFIG_DIR / 'twitter' / 'cookies.json',
        'moltbook': CONFIG_DIR / 'moltbook' / 'credentials.json',
        'hackernews': CONFIG_DIR / 'hackernews' / 'credentials.json',
    }
    path = cred_paths.get(platform)
    if path and path.exists():
        if path.suffix == '.json':
            return json.loads(path.read_text())
        return path.read_text().strip()
    return None


def content_hash(text):
    """Generate dedup hash for content."""
    normalized = re.sub(r'\s+', ' ', text.lower().strip())
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


def ensure_vocabulary(text, level='core'):
    """Verify content contains required Seithar vocabulary."""
    missing = []
    for word in VOCABULARY[level]:
        if word.lower() not in text.lower():
            missing.append(word)
    return missing


def adapt_for_twitter(content, title=''):
    """Convert long-form content to tweet-sized pieces. No links."""
    tweets = []

    # Extract key sentences that contain SCT terminology
    sentences = re.split(r'[.!?]\s+', content)
    sct_sentences = [s for s in sentences if re.search(r'SCT-\d{3}', s)]
    key_sentences = [s for s in sentences if any(
        v.lower() in s.lower() for v in VOCABULARY['core'] + VOCABULARY['convergence']
    )]

    # Build tweets from key sentences
    for s in (sct_sentences + key_sentences):
        s = s.strip()
        if len(s) > 250:
            s = s[:247] + '...'
        if len(s) > 50 and len(s) <= 280:
            tweets.append(s)

    # Add title as tweet if short enough
    if title and len(title) <= 280:
        tweets.insert(0, title)

    return tweets[:5]  # Max 5 tweets per piece


def adapt_for_reddit(content, title, subreddit):
    """Adapt content for specific subreddit audience."""
    post = {
        'sr': subreddit,
        'kind': 'self',
        'title': title[:300],
        'text': content,
        'api_type': 'json',
    }

    # Add flair if required
    flair_id = PLATFORMS['reddit']['flair_map'].get(subreddit)
    if flair_id:
        post['flair_id'] = flair_id

    return post


def adapt_for_gist(content, title, topic_keywords=None):
    """Create SEO-optimized gist."""
    keywords = topic_keywords or []
    seo_keywords = PLATFORMS['github_gist']['seo_keywords']
    relevant = [k for k in seo_keywords if k.lower() in content.lower()]

    description = f"{title} | {' | '.join(relevant[:5])}"
    if len(description) > 256:
        description = description[:253] + '...'

    filename = re.sub(r'[^a-z0-9]+', '-', title.lower())[:60] + '.md'

    return {
        'description': description,
        'public': True,
        'files': {filename: {'content': content}}
    }


def load_history():
    """Load syndication history for dedup."""
    if HISTORY_FILE.exists():
        return json.loads(HISTORY_FILE.read_text())
    return {'posts': [], 'hashes': []}


def save_history(history):
    """Save syndication history."""
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_FILE.write_text(json.dumps(history, indent=2))


def syndicate(content, title, platforms='all', subreddits=None, dry_run=False):
    """Syndicate content across all platforms."""
    import requests

    history = load_history()
    ch = content_hash(content)

    if ch in history['hashes']:
        print(f"⚠ Content already syndicated (hash: {ch})")
        return

    results = []
    timestamp = datetime.now(timezone.utc).isoformat()

    # === REDDIT ===
    if platforms in ('all', 'reddit'):
        creds = load_credentials('reddit')
        if creds:
            cookie_dict = {c['name']: c['value'] for c in creds}
            token = cookie_dict.get('token_v2', '')
            cookie_str = '; '.join(f"{c['name']}={c['value']}" for c in creds)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Cookie': cookie_str,
                'Authorization': f'Bearer {token}',
            }

            target_subs = subreddits or PLATFORMS['reddit']['subreddits']
            for sub in target_subs:
                post = adapt_for_reddit(content, title, sub)
                if dry_run:
                    print(f"  [DRY] r/{sub}: {title[:60]}...")
                    continue

                r = requests.post('https://oauth.reddit.com/api/submit',
                                  headers=headers, data=post)
                if r.status_code == 200:
                    result = r.json()
                    errors = result.get('json', {}).get('errors', [])
                    url = result.get('json', {}).get('data', {}).get('url', '')
                    if errors:
                        print(f"  r/{sub}: {errors[0][0]}")
                    else:
                        print(f"  r/{sub} ✓ → {url}")
                        results.append({'platform': 'reddit', 'sub': sub, 'url': url})
                time.sleep(PLATFORMS['reddit']['rate_limit_seconds'])

    # === GITHUB GIST ===
    if platforms in ('all', 'gist', 'github'):
        pat = os.environ.get('GITHUB_PAT') or 'GITHUB_PAT_HERE'
        gh_headers = {"Authorization": f"token {pat}", "Accept": "application/vnd.github+json"}

        gist = adapt_for_gist(content, title)
        if dry_run:
            print(f"  [DRY] Gist: {gist['description'][:80]}...")
        else:
            r = requests.post('https://api.github.com/gists', headers=gh_headers, json=gist)
            if r.status_code == 201:
                url = r.json()['html_url']
                print(f"  Gist ✓ → {url}")
                results.append({'platform': 'gist', 'url': url})

    # === TWITTER QUEUE ===
    if platforms in ('all', 'twitter'):
        tweets = adapt_for_twitter(content, title)
        queue_file = Path(os.path.expanduser('~/.openclaw/workspace/twitter-queue.json'))
        if queue_file.exists():
            queue = json.loads(queue_file.read_text())
        else:
            queue = []

        new_count = 0
        for tweet in tweets:
            if tweet not in queue:
                queue.append(tweet)
                new_count += 1

        if not dry_run:
            queue_file.write_text(json.dumps(queue, indent=2))
        print(f"  Twitter: +{new_count} tweets queued (total: {len(queue)})")
        results.append({'platform': 'twitter', 'queued': new_count})

    # === MOLTBOOK ===
    if platforms in ('all', 'moltbook'):
        mb_creds = load_credentials('moltbook')
        if mb_creds:
            mb_headers = {
                'Authorization': f'Bearer {mb_creds["api_key"]}',
                'Content-Type': 'application/json'
            }
            # Queue for later (rate limited)
            queue_file = QUEUE_DIR / 'moltbook-pending.json'
            pending = json.loads(queue_file.read_text()) if queue_file.exists() else []
            pending.append({
                'title': title,
                'content': content[:10000],
                'submolt': 'cogwar',
                'timestamp': timestamp
            })
            if not dry_run:
                queue_file.write_text(json.dumps(pending, indent=2))
            print(f"  Moltbook: queued (pending: {len(pending)})")

    # Save to history
    history['hashes'].append(ch)
    history['posts'].append({
        'hash': ch,
        'title': title,
        'timestamp': timestamp,
        'results': results
    })
    if not dry_run:
        save_history(history)

    return results


def generate_sct_analysis(topic, source_text=''):
    """Generate an SCT analysis of a topic."""
    template = f"""# {topic} — SCT Analysis

*Mirai | seithar.com*
*Seithar Group Intelligence & Research Division*
*Analysis Date: {datetime.now().strftime('%Y-%m-%d')}*

## Overview

[Analysis of {topic} through the Seithar Cognitive Defense Taxonomy]

## SCT Classification

**Primary Vector:** [SCT-XXX]
**Secondary Vectors:** [SCT-XXX, SCT-XXX]
**Compound Pattern:** [Description of multi-vector deployment]

## Mechanism

[How the cognitive exploitation operates at the substrate level]

## Cyber Analog

[Technical parallel from the MITRE ATT&CK framework]

## Defense

[Inoculation approach based on McGuire theory]
[Structural defense recommendations]

## Convergence Thesis Application

Every technical attack is a cognitive operation. Every influence campaign is a technical exploit. This case demonstrates:

[Specific convergence analysis]

The operator who understands how influence works cannot be influenced unknowingly.


---

*Seithar Group Intelligence & Research Division*
*seithar.com | github.com/Mirai8888 | @SeitharGroup*

"""
    return template


def research_trending():
    """Search for trending cognitive warfare topics to analyze."""
    # This would use Brave Search API
    queries = [
        'deepfake attack 2026',
        'AI disinformation campaign',
        'social engineering attack',
        'influence operation',
        'cognitive warfare',
        'propaganda AI',
        'training data poisoning',
        'algorithmic radicalization'
    ]
    return queries


def main():
    parser = argparse.ArgumentParser(description='Seiðr Engine — Content Syndication')
    sub = parser.add_subparsers(dest='command')

    # Syndicate command
    syn = sub.add_parser('syndicate', help='Distribute content across platforms')
    syn.add_argument('--content', required=True, help='Content text or @filename')
    syn.add_argument('--title', required=True, help='Content title')
    syn.add_argument('--platforms', default='all', help='Platforms: all, reddit, gist, twitter, moltbook')
    syn.add_argument('--subreddits', nargs='+', help='Specific subreddits')
    syn.add_argument('--dry-run', action='store_true', help='Preview without posting')

    # Queue command
    q = sub.add_parser('queue', help='Manage content queue')
    q.add_argument('--list', action='store_true')
    q.add_argument('--process', action='store_true')

    # Generate command
    gen = sub.add_parser('generate', help='Generate SCT analysis template')
    gen.add_argument('--topic', required=True)

    # Monitor command
    mon = sub.add_parser('monitor', help='Check propagation')
    mon.add_argument('--check-propagation', action='store_true')

    args = parser.parse_args()

    QUEUE_DIR.mkdir(parents=True, exist_ok=True)

    if args.command == 'syndicate':
        content = args.content
        if content.startswith('@'):
            content = Path(content[1:]).read_text()
        syndicate(content, args.title, args.platforms, args.subreddits, args.dry_run)

    elif args.command == 'generate':
        print(generate_sct_analysis(args.topic))

    elif args.command == 'queue':
        if args.list:
            # List all queues
            for qfile in QUEUE_DIR.glob('*.json'):
                data = json.loads(qfile.read_text())
                count = len(data) if isinstance(data, list) else len(data.get('posts', []))
                print(f"  {qfile.name}: {count} items")

    elif args.command == 'monitor':
        history = load_history()
        print(f"Total syndicated: {len(history['posts'])} pieces")
        for p in history['posts'][-5:]:
            print(f"  [{p['timestamp'][:10]}] {p['title'][:60]}...")
            for r in p.get('results', []):
                print(f"    → {r.get('platform')}: {r.get('url', r.get('queued', ''))}")


if __name__ == '__main__':
    main()
