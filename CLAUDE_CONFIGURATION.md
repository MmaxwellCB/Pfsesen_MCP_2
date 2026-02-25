# 🔌 Claude Configuration Complete!

Your pfSense MCP Server is now properly configured for Claude Code!

## ✅ What's Configured

- ✅ `.mcp.json` created in project directory
- ✅ Server configured: `http://localhost:8000/sse`
- ✅ Server is running (PID: 85924)

## 🚀 How to Use in Claude Code

### Step 1: Navigate to the Project

```bash
cd /Users/mmaxwell/pfsense-mcp-server
```

### Step 2: Start Claude from This Directory

```bash
claude
```

### Step 3: Approve the MCP Server

When you start Claude from the project directory, you'll see:

```
Found MCP server configuration in .mcp.json
Do you want to enable the "pfsense" MCP server? (y/n)
```

Type `y` or press Enter to approve.

### Step 4: Verify It's Working

Once in Claude, run:
```
/context
```

You should see the pfSense MCP server listed in the available context.

## 🧪 Test Commands

Try these commands in Claude to test the pfSense server:

```
# Check if the server is accessible
What MCP servers do I have loaded?

# Test the connection (will need pfSense credentials in .env)
Can you test the pfSense connection?

# List available tools
What tools are available for managing pfSense?

# Get system status (requires pfSense credentials)
Show me the pfSense system status
```

## ⚠️ Important: pfSense Credentials Required

The MCP server is running, but it needs **pfSense credentials** to actually connect to your firewall.

Edit `/Users/mmaxwell/pfsense-mcp-server/.env` and add:

```bash
PFSENSE_URL=https://your-pfsense.local
PFSENSE_API_KEY=your-api-key-here
```

**Without credentials**, the tools will return connection errors.

## 🔄 Reload MCP Servers

If you're already in a Claude session:

```
/reload
```

This will reload MCP server configurations.

## 📋 Available Tools (20+)

Once connected, you'll have access to:

### System
- `system_status` - System info, CPU, memory, disk
- `test_connection` - Test API connection
- `enhanced_test_connection` - Advanced test

### Firewall
- `search_firewall_rules` - Search/filter rules
- `create_firewall_rule` - Create new rule
- `update_firewall_rule` - Update rule
- `delete_firewall_rule` - Delete rule
- `apply_firewall_changes` - Apply changes

### Network
- `search_interfaces` - List interfaces
- `get_interface_details` - Interface details
- `update_interface` - Modify interface

### NAT
- `search_nat_port_forward` - Port forwards
- `create_nat_port_forward` - Create forward
- `update_nat_port_forward` - Update forward
- `delete_nat_port_forward` - Delete forward

### DHCP
- `search_dhcp_leases` - View leases
- `get_dhcp_server_config` - DHCP settings

### VPN
- `search_ipsec_tunnels` - IPsec tunnels
- `search_openvpn_connections` - OpenVPN

### Services
- `search_services` - List services
- `get_service_status` - Service status
- `control_service` - Start/stop/restart

## 🔧 Alternative: Global Configuration

If you want the pfSense server available in **all** Claude sessions (not just this project):

**Option 1: Symlink the .mcp.json**
```bash
ln -s /Users/mmaxwell/pfsense-mcp-server/.mcp.json ~/.claude/.mcp.json
```

**Option 2: Use enabledMcpjsonServers in settings**

Add to `~/.claude/settings.json`:
```json
{
  "enableAllProjectMcpServers": true
}
```

This will auto-approve all project MCP servers.

## 🛑 Stop/Start Server

### Check if server is running:
```bash
ps -p 85924 || echo "Not running"
```

### Stop the server:
```bash
kill 85924
```

### Start the server again:
```bash
cd /Users/mmaxwell/pfsense-mcp-server
source venv/bin/activate
export MCP_MODE=http
python -m src.main
```

Or use the startup script:
```bash
./run-http.sh
```

## 📖 Files Created

- `.mcp.json` - Claude MCP server configuration (this directory)
- `mcp-http.json` - Reference configuration with docs
- `SERVER_RUNNING.md` - Server status and management
- `CLAUDE_CONFIGURATION.md` - This file

## 🆘 Troubleshooting

### "MCP server not found"
- Make sure you're in `/Users/mmaxwell/pfsense-mcp-server` when starting Claude
- Check `.mcp.json` exists: `ls -la .mcp.json`
- Verify server is running: `lsof -i :8000`

### "Connection refused" errors
- Check server is running: `ps -p 85924`
- Test endpoint: `curl http://localhost:8000/sse`
- Check logs: `tail -f /private/tmp/claude-501/-Users-mmaxwell/tasks/b71efbe.output`

### Tools return "No pfSense credentials"
- Edit `.env` and add `PFSENSE_URL` and `PFSENSE_API_KEY`
- Restart the server after updating `.env`

---

**You're all set! Start Claude from the project directory and approve the MCP server when prompted!** 🎉
