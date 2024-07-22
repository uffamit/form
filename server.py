#!/usr/bin/env python

import os
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit_form':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            form_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            name = form_data.get('name', [''])[0]
            age = form_data.get('age', [''])[0]
            email = form_data.get('email', [''])[0]

            filename = f"{name}.txt"

            subprocess.run(['./form_data', name, age, email, filename])

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Form Submitted!</h1></body></html>')

        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

port = int(os.environ.get("PORT", 8080))
httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
httpd.serve_forever()
