"""Thin Python wrapper around the @alpharomercoma/proton-bridge-mcp npm package.

This project has no Python implementation of the MCP server itself — it
shells out to the real (Node.js) implementation via `npx`, so pip/uvx users
who prefer a Python-shaped install don't need to know it's Node underneath.

Source of truth: https://github.com/alpharomercoma/proton-bridge-mcp
"""

__version__ = "1.0.2"

NPM_PACKAGE = "@alpharomercoma/proton-bridge-mcp"
