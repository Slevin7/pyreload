# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from . import SocketServer
from .RemoteManager import BackendBase


class RequestHandler(SocketServer.BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):

        print(self.request.recv(1024))



class SocketBackend(BackendBase):

    def setup(self, host, port):
        #local only
        self.server = SocketServer.ThreadingTCPServer(("localhost", port), RequestHandler)

    def serve(self):
        self.server.serve_forever()
