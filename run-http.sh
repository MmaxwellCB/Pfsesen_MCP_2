#!/bin/bash
# Start pfSense MCP Server in HTTP mode

# Load environment variables
set -a
source .env 2>/dev/null || true
set +a

# Set HTTP mode
export MCP_MODE=http
export MCP_HOST=${MCP_HOST:-"0.0.0.0"}
export MCP_PORT=${MCP_PORT:-"8000"}

echo "Starting pfSense MCP Server in HTTP mode..."
echo "Server will be available at: http://${MCP_HOST}:${MCP_PORT}/mcp"
echo ""
echo "Press Ctrl+C to stop"
echo ""

python3 -m src.main
