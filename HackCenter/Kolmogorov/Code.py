#!/usr/bin/env python

import socket

ip = 'enigma2017.hackcenter.com'
port = 45121

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))

answer = 0

def read_until(msg):
	message = ""
        while msg not in message:
          message+=s.recv(1)
        return message



while True:
	
	firstnum = read_until("'")

	letter = s.recv(1)

	s.recv(1)

	secondnum = read_until("'")

	secondLetter = s.recv(1)

	l = []
	for t in firstnum.split():
		try:
			l.append(int(t))
		except ValueError:
			pass
  	    

  	print read_until(".")

	s.send(letter * l[0] + secondLetter)

	s.recv(80)


	
	
s.shutdown(socket.SHUT_WR) 
s.close()