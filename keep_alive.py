# Keep-alive server — Render free tier ko jaag rakhta hai
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class _H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"alive")
    def log_message(self, *a): pass  # silent logs

def keep_alive():
    srv = HTTPServer(("0.0.0.0", 8080), _H)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
