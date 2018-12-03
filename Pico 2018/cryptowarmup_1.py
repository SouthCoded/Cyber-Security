alphabet = "abcdefghijklmnopqrstuvwxyz"


table_value =  "llkjmlmpadkkc"

axis_value = "thisisalilkey"


bit = 0
flag = ""


for d in table_value:
	
	pos_table = alphabet.find(d)
	pos_axis = alphabet.find(axis_value[bit:bit+1])


	bit += 1
	bit = bit % len(axis_value)


	y = (pos_table - pos_axis) % 26

	flag += alphabet[y:y+1]


print(flag.upper())

