
import binascii
key = "axNiYiit"

def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    print(r)
    r = binascii.hexlify(bytes(r, "utf-8"))
    print(r)
    p = str(binascii.unhexlify(r))[2:]

def demystery(s):
	r = ""
	data = binascii.unhexlify(s)
	p = data.decode("utf-8") 
	for i, c in enumerate(p):
		r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
	print(r)

input = "6519c3af42077910576b506dc3b17337c387c29373c2901dc2b9c2abc39964595bc39ac2a86e"

demystery(input)

#mystery("ABCDEFGHIJK")
