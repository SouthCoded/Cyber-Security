#!/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('92.222.90.84',5003))
answer = 0

def read_until(msg):
	message = ""
        while msg not in message:
          message+=s.recv(1)
        return message




