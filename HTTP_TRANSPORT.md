# HTTP Transport Configuration

The pfSense Enhanced MCP Server now supports **Streamable HTTP** transport, enabling remote access and compatibility with both Claude Code CLI and Claude web interface.

## Quick Start - HTTP Mode

### 1. Configure Environment

Edit your `.env` file:

```bash
# Set transport to HTTP
MCP_MODE=http

# Configure HTTP settings
MCP_HOST=0.0.0.0   # Listen on all interfaces
MCP_PORT=8000       # HTTP port

# Your pfSense configuration
PFSENSE_URL=https://your-pfsense.local
PFSENSE_API_KEY=your-api-key-here
```

### 2. Start the Server

**Using the startup script:**
```bash
./run-http.sh
```

**Or manually:**
```bash
export MCP_MODE=http
python3 -m src.main
```

The server will start on `http://0.0.0.0:8000/mcp`

### 3. Configure Claude

#### For Claude Code CLI

Add to your `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "pfsense": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

#### For Claude Web Interface

Add the server URL in Claude's settings:
- URL: `http://your-server-ip:8000/mcp`
- For local: `http://localhost:8000/mcp`

## Transport Modes Comparison

| Feature | stdio | HTTP (Streamable) |
|---------|-------|-------------------|
| **Access** | Local only | Local & Remote |
| **Claude CLI** | ✅ Yes | ✅ Yes |
| **Claude Web** | ❌ No | ✅ Yes |
| **Scalability** | Single instance | Stateless, scalable |
| **Deployment** | Simple | Requires hosting |
| **Security** | File system | Network (add HTTPS) |

## Production Deployment

### Add HTTPS with Nginx

```nginx
server {
    listen 443 ssl http2;
    server_name pfsense-mcp.example.com;

    ssl_certificate /etc/ssl/certs/your-cert.pem;
    ssl_certificate_key /etc/ssl/private/your-key.pem;

    location /mcp {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Docker Deployment

Update `docker-compose.yml`:

```yaml
services:
  pfsense-mcp:
    build: .
    environment:
      - MCP_MODE=http
      - MCP_HOST=0.0.0.0
      - MCP_PORT=8000
    ports:
      - "8000:8000"
    env_file:
      - .env
```

Then run:
```bash
docker-compose up -d
```

## Security Considerations

1. **Authentication**: The MCP server uses your pfSense API credentials for backend auth
2. **Network Security**:
   - Use HTTPS in production (reverse proxy)
   - Restrict access with firewall rules
   - Consider using a VPN for remote access
3. **API Keys**: Store credentials securely, never commit to version control
4. **Rate Limiting**: Enable `ENABLE_RATE_LIMITING=true` in `.env`

## Troubleshooting

### Server Won't Start
```bash
# Check if port is already in use
lsof -i :8000

# Try a different port
export MCP_PORT=8001
python3 -m src.main
```

### Connection Refused
- Ensure firewall allows connections on your MCP_PORT
- Check MCP_HOST is set correctly (0.0.0.0 for all interfaces)
- Verify the server is running: `curl http://localhost:8000/mcp`

### Claude Can't Connect
- Check the URL in Claude settings matches your server
- For remote access, use your server's public IP or domain
- Ensure no proxy/VPN is blocking the connection

## Advanced Configuration

### Environment Variables

```bash
# HTTP Transport Settings
MCP_MODE=http                # Enable HTTP transport
MCP_HOST=0.0.0.0            # Bind address
MCP_PORT=8000               # HTTP port

# Performance
CONCURRENT_REQUESTS=10      # Max concurrent requests
CONNECTION_TIMEOUT=30       # Request timeout (seconds)

# Monitoring
ENABLE_METRICS=true         # Enable Prometheus metrics
METRICS_PORT=9090          # Metrics endpoint

# Logging
LOG_LEVEL=INFO             # DEBUG, INFO, WARNING, ERROR
LOG_FORMAT=json            # text or json
```

### Health Check Endpoint

The server exposes a health check endpoint:

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "version": "4.1.0",
  "transport": "http"
}
```

## Migration from stdio

If you're currently using stdio mode:

1. **Backup your config**: `cp .env .env.backup`
2. **Update .env**: Change `MCP_MODE=stdio` to `MCP_MODE=http`
3. **Update Claude settings**: Switch from command-based to URL-based config
4. **Test**: Start the server and verify connectivity

Both modes can coexist - run separate instances with different ports!

## Support

For issues or questions:
- 📝 [GitHub Issues](https://github.com/gensecaihq/pfsense-mcp-server/issues)
- 📖 [Full Documentation](README.md)
- 💬 Community discussions welcome!
