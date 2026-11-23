# proton-bridge-mcp (Python wrapper)

A `pip`/`uvx`-installable wrapper around [`proton-bridge-mcp`](https://github.com/alpharomercoma/proton-bridge-mcp), an [MCP](https://modelcontextprotocol.io) server for reading, searching, organizing, and sending Proton Mail via Proton Mail Bridge.

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
claude mcp add --scope user proton-mail -- uvx proton-bridge-mcp
```

(If you installed with `pip install`, `-- proton-bridge-mcp` works too.)

**Claude Desktop / other MCP clients:**

```json
{
  "mcpServers": {
    "proton-mail": {
      "command": "uvx",
      "args": ["proton-bridge-mcp"]
    }
  }
}
```

**Codex CLI:**

```bash
codex mcp add proton-mail -- uvx proton-bridge-mcp
```

You don't need a feature flag. Earlier versions of this README said to enable `mcp_2026_07_28`, but that flag only opts into a newer MCP protocol revision. Turn it off again with `codex features disable mcp_2026_07_28`.

## Tools and approvals

The server has ten tools. Four are read-only (`list_mailboxes`, `list_messages`, `search_messages`, `get_message`). Six change your mailbox or send mail (`move_messages`, `flag_messages`, `delete_messages`, `manage_mailbox`, `send_message`, `create_draft`). Every tool is annotated, so:

- **Codex** runs the read tools without asking and asks before every write. `codex exec` declines writes unless you pre-approve them per tool in `~/.codex/config.toml`.
- **Claude Code** in auto mode (the default since v2.1.283) lets a classifier approve most calls. To make sure you're asked before mail is sent or deleted, add `ask` rules for `mcp__proton-mail__send_message`, `mcp__proton-mail__delete_messages`, and `mcp__proton-mail__manage_mailbox`.

The upstream README has [ready-to-paste settings for both clients](https://github.com/alpharomercoma/proton-bridge-mcp#2-register-with-your-mcp-client).

## Which version runs?

Each launch runs `npx -y @alpharomercoma/proton-bridge-mcp`, which resolves to the newest npm release. Upgrading the server doesn't need a new wrapper release. One exception: if you've ever run `npm install -g @alpharomercoma/proton-bridge-mcp` on the same machine, npx may keep running that global copy. Remove it with `npm uninstall -g @alpharomercoma/proton-bridge-mcp`.

## Why does this exist separately from the npm package?

The actual server (all ten tools, TLS certificate pinning instead of disabled verification, the setup wizard) lives entirely in the Node.js project: **https://github.com/alpharomercoma/proton-bridge-mcp**. That's the canonical implementation, source of truth for behavior, and where issues/PRs about actual functionality belong. This repo only exists to make it reachable from `pip`/`uvx` workflows.

## License

MIT — see [LICENSE](LICENSE).
