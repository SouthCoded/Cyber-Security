

from pwn import *


#p = remote('35.198.185.193',1338)
p = process('./police_academy')

p.recv()
p.sendline('kaiokenx20')

p.recv()

p.interactive()

#10210897103

#8392585648256674918



