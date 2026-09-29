"""Serve the dashboard locally, answering /api/state from state/ exactly as the Netlify function
does from GitHub. For checking the page before a deploy: python tools/dashboard_dev.py [port]"""

import http.server
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOWED = {"summary.json": "application/json", "picks_snake.json": "application/json", "picks_snake_nonews.json": "application/json",
           "trades.csv": "text/csv", "daily_profit.csv": "text/csv"}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT / "site"), **k)

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path == "/api/state":
            f = urllib.parse.parse_qs(u.query).get("f", [""])[0]
            p = ROOT / "state" / f
            if f not in ALLOWED or not p.exists():
                self.send_error(404 if f in ALLOWED else 400)
                return
            body = p.read_bytes()
            self.send_response(200)
            self.send_header("content-type", ALLOWED[f])
            self.send_header("content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
