#!/usr/bin/env python3
"""
Startup script for AI Resume Builder Backend
"""

import os
from app import app

if __name__ == '__main__':
    # Get configuration from environment variables
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting AI Resume Builder Backend...")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Debug: {debug}")
    print(f"Open http://{host}:{port} in your browser")
    
    app.run(host=host, port=port, debug=debug)
