#!/usr/bin/python
__author__ = 'f0xd3v1lsw1ld@gmail.com'
# simple example how to realize a webserver with python
# you need a index.html file in the same directory as the python script
# then run this script and after this open your browser and navigate to http://localhost:8080/
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

def main():
    HandlerClass = SimpleHTTPRequestHandler
    ServerClass = BaseHTTPServer.HTTPServer
    Protocol = "HTTP/1.0"

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8080
    server_address = ('', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == "__main__":
    main()
