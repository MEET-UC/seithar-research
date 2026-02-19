# Jan Wilmake GitHub Scoping Report
**Date:** 2026-02-19
**Purpose:** Identify patterns useful for Seithar's self-assembling taxonomy and cognitive warfare apparatus

## Who Is This Person

Jan Wilmake is a prolific solo builder focused on one thesis: making APIs and context discoverable and composable for AI agents. Heavy Cloudflare Workers stack. Everything is MCP-first (Model Context Protocol). About 40+ public repos, most from the last 6 months.

## Repo Inventory (Notable Only)

| Repo | Stars | What It Does |
|------|-------|-------------|
| `openapi-mcp-server` | 874 | Converts any OpenAPI spec into an MCP server. The flagship. |
| `openapisearch` | 59 | Searchable registry of OpenAPI specs. Discovery layer for AI agents. |
| `socialdatapod` | 50 | User-owned social data stores (SOLID protocol inspired). X/Twitter data tools. |
| `LLMTEXT-mcp` | 48 | Converts llms.txt files into MCP servers. Bridge between standards. |
| `with-mcp` | 34 | One-line middleware to turn any API + OpenAPI spec into an MCP endpoint. |
| `universal-mcp-oauth` | 30 | Dynamic client registration and OAuth for arbitrary MCP servers. Zero-config auth. |
| `efficient-recorder` | 229 | Open source Rewind.ai alternative. Privacy-focused screen recording + retrieval. |
| `contextarea` | 23 | Cloud IDE for context engineering. URLs as context, cached results as URLs. |
| `install-this-mcp` | 22 | Reduces friction for MCP server installation. |
| `context-for-github` | 8 | Generates high-level context overviews of all your GitHub repos daily. |
| `speculative-dual-streaming` | 4 | Streams two LLMs simultaneously, routes based on which needs search. |
| `entity-resolution-demo` | 2 | AI-powered identity resolution across social platforms. |
| `humanmcp` | -- | Human-in-the-loop over MCP. |
| `bash-mcp` | -- | Bash execution via MCP. |
| `build-and-reset` | -- | GitHub Action that resets its own repo every 15 minutes. |

## Patterns Directly Useful for Seithar

### 1. OpenAPI-as-Discovery-Protocol (openapisearch, openapi-mcp-server)

The core insight: OpenAPI specs are a machine-readable capability registry that already exists for thousands of services. Wilmake built infrastructure to crawl, index, search, and auto-bridge these specs into MCP tool surfaces.

**Seithar application:** The scanner and taxonomy evolution systems need a way to discover and classify external capabilities automatically. Instead of building custom discovery, we could consume the OpenAPI ecosystem as a data source. Every API with an OpenAPI spec becomes a potential tool node in the taxonomy without manual registration.

### 2. Protocol Bridging as a One-Liner (with-mcp, LLMTEXT-mcp)

`with-mcp` turns any existing API server + OpenAPI spec into an MCP endpoint with one middleware call. `LLMTEXT-mcp` does the same for the llms.txt standard. The pattern: take an existing protocol/format, write a thin shim, and it becomes composable in a new protocol.

**Seithar application:** HoleSpawn and the plugin architecture should adopt this pattern. Instead of requiring tools to be built for Seithar specifically, write bridge shims that consume existing standards (MCP, OpenAPI, llms.txt) and project them into Seithar's internal protocol. This is how you get self-assembly: you inherit the entire MCP/OpenAPI ecosystem for free.

### 3. URL-as-Context Primitive (contextarea)

Everything in contextarea is a URL. Inputs are URLs. Outputs are URLs. Results are cached and addressable. Different representations (JSON, MD, HTML) are negotiated via Accept headers or file extensions. The prompt, the context, and the result are all first-class URL resources.

**Seithar application:** The autoprompt system should treat prompts and results as URL-addressable resources. This enables caching, sharing, composition, and referencing across sessions. A taxonomy node could literally be a URL that returns its definition, relationships, and operations based on content negotiation.

### 4. Universal OAuth Discovery (universal-mcp-oauth)

Uses RFC 8414 (OAuth Authorization Server Metadata) and RFC 7591 (Dynamic Client Registration) to authenticate with any arbitrary MCP server. The client discovers auth requirements, registers itself dynamically, and authenticates, all without prior configuration.

**Seithar application:** If Seithar components need to authenticate with external services (APIs, data sources, other agents), this zero-config auth pattern eliminates the need for pre-configured credentials. Components can self-register with new services as they discover them. Critical for autonomous operation.

### 5. Self-Resetting Build Artifact (build-and-reset)

A GitHub Action that resets its own repo every 15 minutes. Trivial concept, but the pattern of ephemeral, self-resetting state is interesting for testing and for systems that need to prevent state accumulation.

**Seithar application:** Useful pattern for HoleSpawn disposable environments. Spawn a context, let it run, reset after use. Prevents contamination between operations.

### 6. Entity Resolution Across Platforms (entity-resolution-demo)

AI-powered identity resolution linking the same person across different social platforms.

**Seithar application:** Directly relevant to cognitive warfare target mapping. Cross-platform identity linkage is a foundational capability for building target dossiers from open source data.

## Technical Ideas to Adopt

1. **OpenAPI as taxonomy seed data.** Crawl openapisearch.com or apis.guru to auto-populate capability nodes in the taxonomy. Each API endpoint becomes a leaf node with typed inputs/outputs.

2. **MCP bridge pattern for plugin architecture.** Do not invent a new plugin protocol. Use MCP as the transport and write bridges from existing formats. This gives us instant access to the growing MCP tool ecosystem.

3. **Content negotiation for taxonomy nodes.** Each taxonomy node should respond to different representations: human-readable (MD/HTML), machine-readable (JSON-LD), and agent-readable (MCP tool definition). Single URL, multiple views.

4. **Dynamic auth discovery.** Implement RFC 8414 / RFC 7591 in Seithar's external integration layer. Any service that supports these standards becomes zero-config.

5. **Speculative dual-streaming for scanner.** When the scanner needs to classify something, run two models simultaneously and take the faster/better result. Reduces latency for time-sensitive operations.

## Code/Specs Worth Deeper Study

- `openapi-mcp-server/worker.ts` - The actual OpenAPI-to-MCP conversion logic. Single file, Cloudflare Worker. Study how it maps OpenAPI operations to MCP tools.
- `with-mcp/example.ts` - The one-liner bridge pattern implementation.
- `universal-mcp-oauth/ADR.md` - Architecture Decision Record for the auth flow. Documents the tradeoffs.
- `universal-mcp-oauth/packages/` - Modular auth components. Could be lifted directly.
- `openapisearch/docs/openapi-discovery.md` - How to discover OpenAPI specs in the wild. Relevant for scanner crawling.
- `contextarea/app/` - The URL-as-context implementation. How they handle content negotiation and caching.

## Assessment

Wilmake is building a composability layer for the AI tool ecosystem. His thesis is: existing APIs + thin protocol bridges = infinite tool surface for agents. This is directly aligned with Seithar's need for self-assembling tool taxonomies.

The key takeaway is not any single repo but the meta-pattern: **do not build capabilities, build bridges to existing capabilities.** The taxonomy should not catalog tools we build. It should catalog tools that already exist, discovered automatically through protocol standards (OpenAPI, MCP, llms.txt, OAuth metadata), and made composable through thin shims.

The weaknesses: everything is Cloudflare-specific, no offline/local operation, no adversarial considerations, no security hardening beyond basic OAuth. We would need to harden anything we adopt.
