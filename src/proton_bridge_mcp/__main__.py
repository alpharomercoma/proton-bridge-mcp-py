import os
import shutil
import sys

from . import NPM_PACKAGE


def _require_npx():
    npx = shutil.which("npx")
    if npx:
        return npx
    sys.stderr.write(
        "proton-bridge-mcp: this package is a thin wrapper around the Node.js "
        f"implementation ({NPM_PACKAGE}) and requires Node.js/npx on PATH.\n"
        "Install Node.js 18+ from https://nodejs.org and try again.\n"
    )
    sys.exit(1)


def run_server():
    """Console script: proton-bridge-mcp — runs the MCP server over stdio."""
    npx = _require_npx()
    # execvp replaces this process outright, so the MCP client talks directly
    # to the Node process over stdio with no buffering/wrapping in between.
    os.execvp(npx, [npx, "-y", NPM_PACKAGE, *sys.argv[1:]])


def run_setup():
    """Console script: proton-bridge-mcp-setup — runs the interactive setup wizard."""
    npx = _require_npx()
    os.execvp(npx, [npx, "-y", "-p", NPM_PACKAGE, "proton-bridge-mcp-setup", *sys.argv[1:]])


if __name__ == "__main__":
    run_server()
