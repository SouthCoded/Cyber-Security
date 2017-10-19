import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('92.222.90.84',5003))
answer = 0

def read_until(msg):
	message = ""
        while msg not in message:
          message+=s.recv(1)
        return message



while True:
	numbers = read_until("W")
	print ("number is " + numbers)
	phrase = s.recv(500)
	print ("phrase is " + phrase)
	answer = 0
	answers = 0.0
        if "avg" in repr(phrase):
		x=0
		total = ""
		for num in numbers:
		   if num.isdigit():
			total += str(num)
		   else:
			if total.isdigit():
				x = x+1 
				answer+= int(total)
				total = ""
		
		answers = float(answer) / float(x)
		s.send(str(answers) + "\n")
		print("This is the answers " + str(answers))
	if "max" in repr(phrase):
		total = ""
		for num in numbers:
		   if num.isdigit():
			total += str(num)

		   else:
			if total.isdigit():
				big = int(total)
				if big > answer:
				   answer = big
				total = ""
		s.send(str(answer) + "\n")

	if "sum" in repr(phrase):
		total = ""
		for num in numbers:		
		   if num.isdigit():
                   	total += str(num)
		   else:
			if total.isdigit():
				answer += int(total)
				total = ""
		s.send(str(answer) + "\n")

	if "min" in repr(phrase):
		total = ""
		answer = 9999
		for num in numbers:
		   if num.isdigit():	   
			total += str(num)
		   else:
			if total.isdigit():
				big = int(total)	
		   		if big < answer:
                   			answer = big
                		total = ""
		s.send(str(answer) + "\n")
	if not numbers:
	   print repr(numbers)
           break

	print("This is the answer " + str(answer))

	
	
s.shutdown(socket.SHUT_WR) 
s.close()
