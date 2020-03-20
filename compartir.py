#!/usr/bin/env python3

# desde terminal (python3 -m http.server 8000)

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.1.134", PORT), Handler) as httpd:
    print ("serving at port", PORT)
    httpd.serve_forever()
