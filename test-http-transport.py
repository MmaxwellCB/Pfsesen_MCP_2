#!/usr/bin/env python3
"""
Quick test script to verify HTTP transport configuration
"""
import os
import sys

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    try:
        from fastmcp import FastMCP
        print("  ✅ FastMCP imported successfully")
    except ImportError as e:
        print(f"  ❌ FastMCP import failed: {e}")
        return False

    try:
        import httpx
        print("  ✅ httpx imported successfully")
    except ImportError as e:
        print(f"  ❌ httpx import failed: {e}")
        return False

    return True

def test_env_config():
    """Test environment configuration"""
    print("\nTesting environment configuration...")

    required_vars = ["PFSENSE_URL", "PFSENSE_API_KEY"]
    missing = []

    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        print(f"  ⚠️  Missing environment variables: {', '.join(missing)}")
        print("  💡 Create a .env file from .env.example and configure your pfSense details")
        return False

    print("  ✅ Required environment variables found")
    return True

def test_http_config():
    """Test HTTP transport configuration"""
    print("\nTesting HTTP transport configuration...")

    mode = os.getenv("MCP_MODE", "stdio")
    host = os.getenv("MCP_HOST", "0.0.0.0")
    port = os.getenv("MCP_PORT", "8000")

    print(f"  Mode: {mode}")
    print(f"  Host: {host}")
    print(f"  Port: {port}")

    if mode == "http":
        print(f"  ✅ HTTP transport configured on http://{host}:{port}/mcp")
    else:
        print(f"  ℹ️  Currently in {mode} mode")
        print("  💡 Set MCP_MODE=http to enable HTTP transport")

    return True

def test_server_init():
    """Test server initialization"""
    print("\nTesting server initialization...")
    try:
        # Set to stdio mode for testing (don't actually start HTTP server)
        os.environ["MCP_MODE"] = "stdio"

        # Import after setting env vars
        from src.main import mcp, VERSION

        print(f"  ✅ Server initialized successfully (v{VERSION})")
        print(f"  Server name: {mcp.name if hasattr(mcp, 'name') else 'pfSense Enhanced MCP Server'}")

        return True
    except Exception as e:
        print(f"  ❌ Server initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("pfSense MCP Server - HTTP Transport Test")
    print("=" * 60)

    # Load .env if available
    try:
        from dotenv import load_dotenv
        if load_dotenv():
            print("✅ Loaded configuration from .env file\n")
        else:
            print("ℹ️  No .env file found, using environment variables\n")
    except ImportError:
        print("ℹ️  python-dotenv not installed, using environment variables\n")

    all_passed = True

    # Run tests
    all_passed &= test_imports()
    all_passed &= test_env_config()
    all_passed &= test_http_config()
    all_passed &= test_server_init()

    print("\n" + "=" * 60)
    if all_passed:
        print("✅ All tests passed!")
        print("\nTo start the server in HTTP mode:")
        print("  1. Set MCP_MODE=http in your .env file")
        print("  2. Run: ./run-http.sh")
        print("  3. Or: python3 -m src.main")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)
    print("=" * 60)

if __name__ == "__main__":
    main()
