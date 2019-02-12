import subprocess
from subprocess import Popen, PIPE, STDOUT

from subprocess import check_output



a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 <>,.!@$%^&*()-_///\'\":}[{]\\}|"

flag = ""

start = 0

while start != 60:

	for x in a:
		temp = flag
		temp += x
		process = subprocess.run(['ltrace -o hey.txt ./0pack.elf '], input = temp, encoding = "UTF-8",shell=True)

		output = open("hey.txt", "r")

		red = output.read()
		numberOfSleeps = red.count("sleep")

		start += 1

		if numberOfSleeps == ((len(flag)+1)*10):
			flag += x
			start = 0
		print(x,flag)

#Break at __libc_start_main

# 0x7ffff7a05b95 - Input Password - fgets

# 0x555555566a19 - fgets
#ThisIsATriumph





