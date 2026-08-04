# proton-bridge-mcp (Python wrapper)

A `pip`/`uvx`-installable wrapper around [`proton-bridge-mcp`](https://github.com/alpharomercoma/proton-bridge-mcp), an [MCP](https://modelcontextprotocol.io) server for reading and searching Proton Mail via Proton Mail Bridge.

**This package contains no Python implementation.** It's a thin shim that execs into the real Node.js implementation via `npx`. It exists so Python-oriented MCP tooling (`uvx`, `pipx`, `pip install`) can install and run it without needing to know it's Node underneath.

Unofficial, community project. Not affiliated with or endorsed by Proton AG.

## Requirements

- **Node.js 18+** must be installed and on `PATH` (specifically `npx`). This wrapper cannot function without it — there is no pure-Python fallback.
- A Proton Mail plan that supports Bridge, with [Proton Mail Bridge](https://proton.me/mail/bridge) running

## Install

```bash
pip install proton-bridge-mcp
# or
uvx proton-bridge-mcp
```

## Setup

Run the interactive setup wizard once (fetches and pins Bridge's TLS certificate, verifies login, writes credentials to `~/.config/proton-bridge-mcp/`, chmod 600):

```bash
proton-bridge-mcp-setup
```

## Register with an MCP client

**Claude Code:**

```bash
claude mcp add proton-mail -s user -- proton-bridge-mcp
```

**Claude Desktop / other MCP clients:**

```json
{
  "mcpServers": {
    "proton-mail": {
      "command": "proton-bridge-mcp"
    }
  }
}
```

## Why does this exist separately from the npm package?

The actual server (`list_mailboxes`, `list_messages`, `search_messages`, `get_message` tools; TLS certificate pinning instead of disabled verification; the setup wizard) lives entirely in the Node.js project: **https://github.com/alpharomercoma/proton-bridge-mcp**. That's the canonical implementation, source of truth for behavior, and where issues/PRs about actual functionality belong. This repo only exists to make it reachable from `pip`/`uvx` workflows.

## License

MIT — see [LICENSE](LICENSE).
