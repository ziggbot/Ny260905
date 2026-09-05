#!/usr/bin/env python3
"""Starta en lokal demo-server för Isplan på ditt eget Wi-Fi.

Kör:   python3 demo-server.py
Öppna sedan adressen som skrivs ut i telefonens webbläsare
(telefonen och datorn måste vara på samma nätverk).
Avsluta med Ctrl+C. Kräver bara Python 3, inga paket.
"""
import http.server
import os
import socket
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = os.path.dirname(os.path.abspath(__file__))


def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))  # ingen trafik skickas, bara val av nätverkskort
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        print("  " + self.address_string() + " " + (fmt % args))


if __name__ == "__main__":
    ip = lan_ip()
    with http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler) as srv:
        print("Isplan demo-server igång.")
        print()
        print("  Öppna i telefonen:  http://%s:%d/" % (ip, PORT))
        print("  På den här datorn:  http://localhost:%d/" % PORT)
        print()
        print("Telefonen måste vara på samma Wi-Fi. Avsluta med Ctrl+C.")
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\nStoppad.")
