#Gift Wrap 

from pwn import *

p = remote('2018shell3.picoctf.com', 34532)

x = p.recvall()

print (x)

#0x000009d3 = spawn_shell
#0x7ff6c4816000 = base_address
#0x7ff6c48169d3 = added address  



