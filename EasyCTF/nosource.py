import base64
import math

key = "nosource"

def process(a, b):
    length = max(len(a), len(b))
    out = ""
    i = 0

    while i < length:
      ca = ord(a[i % len(a)])
      cb = ord(b[i % len(b)])
      out += chr(ca ^ cb)
      i += 1
    
    return out


flag = 'Fg4GCRoHCQ4TFh0IBxENAE4qEgwHMBsfDiwJRQImHV8GQAwBDEYvV11BCA=='
flag = base64.b64decode(flag)

result = 'eGF1Zm91amt9eW5ncmNuZSBFYWNyQnh6YEN6KndUfjpoL39ueTRMMjMuew=='
result = base64.b64decode(result)
print(result)

print(base64.b64encode(process(flag, key)))


  