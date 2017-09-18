#!/usr/bin/env python

from http.server import HTTPServer
from handler import RequestHandler

if __name__ == "__main__":

    address = ("127.0.0.1", 8080)
    httpd = HTTPServer(address, RequestHandler)

    print("Starting server at " + address[0] + ":" + str(address[1]))
    httpd.serve_forever()
