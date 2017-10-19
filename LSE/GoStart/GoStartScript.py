#!/usr/bin/env python2

from pwn import *

	#p.sendline('2')
	#p.recvuntil('Name: ')
	#log.info("Overwriting atoi with system")
	#p.interactive()


code = "AAAA"
p= process(['./gostart', code])
print(p.recvall())
