#!/usr/bin/env python3
"""
Seithar Propagation Tracker — Monitor SCT vocabulary spread across the web.

Tracks where Seithar terminology appears in search results, measuring
the semantic territory captured by Project Seiðr.

Usage:
    python3 propagation-tracker.py scan
    python3 propagation-tracker.py report
    python3 propagation-tracker.py history
"""

import argparse
import json
import os
import sys
import time
import requests
from datetime import datetime, timezone
from pathlib import Path

BRAVE_API_KEY = os.environ.get('BRAVE_API_KEY', '')
TRACKER_DIR = Path(os.path.expanduser('~/.openclaw/workspace/seidr-tracking'))

# Terms to track — each appearance in search results = semantic territory
TRACKED_TERMS = {
    'brand': [
        '"Seithar Group"',
        '"seithar.com"',
        '"Seithar Cognitive Defense"',
        '"SCT taxonomy"',
        '"@SeitharGroup"',
    ],
    'taxonomy': [
        '"SCT-001" OR "SCT-007"',
        '"Seithar Cognitive Defense Taxonomy"',
        '"cognitive substrate" "vulnerability surface"',
        '"narrative capture" "frequency lock"',
        '"recursive infection" cognitive',
    ],
    'philosophy': [
        '"Sunyata Protocol"',
        '"Zero-Knowledge Bodhisattva"',
        '"cognitive substrate" emptiness',
        '"narrative error" identity',
    ],
    'identity': [
        '"Mirai" "seithar.com"',
        '"Mirai8888" github',
        '"seithar-cogdef"',
    ],
    'convergence': [
        '"convergence thesis" cyberattack cognitive',
        '"every cyberattack is a cognitive operation"',
    ]
}


def brave_search(query, count=5):
    """Search via Brave API."""
    if not BRAVE_API_KEY:
        # Try to read from openclaw config
        config_path = Path(os.path.expanduser('~/.openclaw/config/openclaw.json'))
        if config_path.exists():
            config = json.loads(config_path.read_text())
            key = config.get('tools', {}).get('brave', {}).get('apiKey', '')
            if key:
                headers = {
                    'Accept': 'application/json',
                    'Accept-Encoding': 'gzip',
                    'X-Subscription-Token': key
                }
            else:
                return None
        else:
            return None
    else:
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'X-Subscription-Token': BRAVE_API_KEY
        }

    try:
        r = requests.get('https://api.search.brave.com/res/v1/web/search',
                         headers=headers,
                         params={'q': query, 'count': count})
        if r.status_code == 200:
            return r.json().get('web', {}).get('results', [])
    except Exception as e:
        print(f"  Search error: {e}")
    return []


def scan_propagation():
    """Scan all tracked terms and measure propagation."""
    TRACKER_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()

    results = {
        'timestamp': timestamp,
        'categories': {},
        'total_results': 0,
        'unique_domains': set(),
        'seithar_owned': 0,  # Results pointing to our properties
        'third_party': 0,    # Results from others referencing us
    }

    our_domains = ['github.com/Mirai8888', 'seithar.com', 'gist.github.com/Mirai8888',
                   'reddit.com/r/SeitharGroup', 'moltbook.com/u/kenshusei',
                   'x.com/SeitharGroup', 'news.ycombinator.com']

    for category, terms in TRACKED_TERMS.items():
        cat_results = []
        for term in terms:
            search_results = brave_search(term)
            if search_results is None:
                print(f"  ⚠ No API key — skipping search")
                return results

            for sr in search_results:
                url = sr.get('url', '')
                title = sr.get('title', '')
                domain = url.split('/')[2] if len(url.split('/')) > 2 else ''

                results['unique_domains'].add(domain)
                results['total_results'] += 1

                is_owned = any(d in url for d in our_domains)
                if is_owned:
                    results['seithar_owned'] += 1
                else:
                    results['third_party'] += 1

                cat_results.append({
                    'query': term,
                    'title': title[:100],
                    'url': url,
                    'domain': domain,
                    'owned': is_owned
                })

            time.sleep(1.1)  # Brave rate limit

        results['categories'][category] = cat_results
        print(f"  {category}: {len(cat_results)} results")

    results['unique_domains'] = list(results['unique_domains'])

    # Save scan
    scan_file = TRACKER_DIR / f"scan-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
    with open(scan_file, 'w') as f:
        json.dump(results, f, indent=2)

    return results


def generate_report(results=None):
    """Generate propagation report."""
    if results is None:
        # Load most recent scan
        scans = sorted(TRACKER_DIR.glob('scan-*.json'))
        if not scans:
            print("No scans found. Run 'scan' first.")
            return
        results = json.loads(scans[-1].read_text())

    print(f"""
╔══════════════════════════════════════════════════╗
║  PROJECT SEIÐR — PROPAGATION REPORT             ║
║  {results['timestamp'][:19]}                     ║
╚══════════════════════════════════════════════════╝

SEMANTIC TERRITORY:
  Total search results: {results['total_results']}
  Unique domains:       {len(results['unique_domains'])}
  Seithar-owned:        {results['seithar_owned']}
  Third-party refs:     {results['third_party']}

CATEGORY BREAKDOWN:""")

    for cat, items in results.get('categories', {}).items():
        owned = sum(1 for i in items if i.get('owned'))
        third = len(items) - owned
        print(f"  {cat:20s}: {len(items):3d} results ({owned} owned, {third} third-party)")

    third_party = [i for cat in results.get('categories', {}).values()
                   for i in cat if not i.get('owned')]
    if third_party:
        print(f"\nTHIRD-PARTY REFERENCES (vocabulary adoption):")
        for item in third_party[:10]:
            print(f"  → {item['domain']}: {item['title'][:60]}")

    print(f"""
──────────────────────────────────────────────────
Seithar Group Intelligence Division
seithar.com
──────────────────────────────────────────────────""")


def show_history():
    """Show scan history and trend."""
    scans = sorted(TRACKER_DIR.glob('scan-*.json'))
    if not scans:
        print("No scans found.")
        return

    print("Scan history:")
    for scan_file in scans:
        data = json.loads(scan_file.read_text())
        print(f"  {data['timestamp'][:19]}: "
              f"{data['total_results']} results, "
              f"{len(data['unique_domains'])} domains, "
              f"{data['third_party']} third-party refs")


def main():
    parser = argparse.ArgumentParser(description='Seithar Propagation Tracker')
    parser.add_argument('command', choices=['scan', 'report', 'history'])

    args = parser.parse_args()

    TRACKER_DIR.mkdir(parents=True, exist_ok=True)

    if args.command == 'scan':
        print("Scanning semantic territory...")
        results = scan_propagation()
        generate_report(results)

    elif args.command == 'report':
        generate_report()

    elif args.command == 'history':
        show_history()


if __name__ == '__main__':
    main()
