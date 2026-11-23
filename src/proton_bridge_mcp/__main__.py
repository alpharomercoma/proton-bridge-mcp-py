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
        "Install Node.js 20+ from https://nodejs.org and try again.\n"
    )
    sys.exit(1)


_REENTRY_GUARD = "PROTON_BRIDGE_MCP_PY_WRAPPER"


def _exec_npx(args):
    # If npx can't run the Node package's own bin (e.g. when launched from
    # inside the npm package's source folder), it falls back to PATH and can
    # find this wrapper again, which would exec npx again, forever. The env
    # var survives exec, so a second entry means we are in that loop.
    if os.environ.get(_REENTRY_GUARD):
        sys.stderr.write(
            "proton-bridge-mcp: npx started this Python wrapper again instead of the "
            f"Node server ({NPM_PACKAGE}); stopping to avoid an endless loop.\n"
            "This happens when it runs from inside the npm package's source folder. "
            "Run it from another directory.\n"
        )
        sys.exit(1)
    npx = _require_npx()
    os.environ[_REENTRY_GUARD] = "1"
    # execvp replaces this process outright, so the MCP client talks directly
    # to the Node process over stdio with no buffering/wrapping in between.
    os.execvp(npx, [npx, *args])


def run_server():
    """Console script: proton-bridge-mcp — runs the MCP server over stdio."""
    _exec_npx(["-y", NPM_PACKAGE, *sys.argv[1:]])


def run_setup():
    """Console script: proton-bridge-mcp-setup — runs the interactive setup wizard."""
    _exec_npx(["-y", "-p", NPM_PACKAGE, "proton-bridge-mcp-setup", *sys.argv[1:]])


if __name__ == "__main__":
    run_server()
