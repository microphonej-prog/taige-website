#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""极简 CONNECT 转发器：把 git 的 HTTPS 代理请求固定转发到可达的 GitHub 边缘 IP。
127.0.0.1:8899 -> 140.82.112.3:443（TLS SNI 仍为 github.com，证书校验正常）"""
import socket, threading, sys

LISTEN = ("127.0.0.1", 8899)
TARGETS = [("140.82.112.3", 443), ("140.82.113.3", 443), ("140.82.114.3", 443),
           ("140.82.121.4", 443), ("20.205.243.166", 443)]


def pump(a, b):
    try:
        while True:
            d = a.recv(65536)
            if not d:
                break
            b.sendall(d)
    except Exception:
        pass
    finally:
        for s in (a, b):
            try:
                s.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass


def handle(c):
    try:
        buf = b""
        while b"\r\n\r\n" not in buf:
            d = c.recv(4096)
            if not d:
                return
            buf += d
            if len(buf) > 65536:
                return
        line = buf.split(b"\r\n")[0].decode("latin1")
        if not line.upper().startswith("CONNECT"):
            c.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
            return
        up = None
        for tgt in TARGETS:
            try:
                up = socket.create_connection(tgt, timeout=12)
                break
            except Exception:
                up = None
        if up is None:
            c.sendall(b"HTTP/1.1 502 Bad Gateway\r\n\r\n")
            return
        c.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        t = threading.Thread(target=pump, args=(c, up), daemon=True)
        t.start()
        pump(up, c)
    except Exception as e:
        print("handle err:", e, file=sys.stderr)
    finally:
        try:
            c.close()
        except Exception:
            pass


srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(LISTEN)
srv.listen(50)
print("listening on %s:%d -> %s" % (LISTEN + (str(TARGETS),)), flush=True)
while True:
    conn, _ = srv.accept()
    threading.Thread(target=handle, args=(conn,), daemon=True).start()
