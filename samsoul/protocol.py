#! /usr/bin/env python

import socket

class Protocol:
    data = dict() # NetSoul personal data
    ns_server = 'ns-server.epita.fr'
    ns_port = 4242

    def __init__(self):
        self.connect()

    def get_data(self, hello):
        s = hello.split()
        self.data["socket"] = s[1]
        self.data["md5"] = s[2]
        self.data["ip"] = s[3]
        self.data["port"] = s[4]
        self.data["timestamp"] = s[5]

    def connect(self):
        ns = socket.socket()
        ns.connect((socket.gethostbyname(self.ns_server), self.ns_port))
        hello = ns.recv(8192)
        print(hello)
        self.get_data(hello)
        return ns
