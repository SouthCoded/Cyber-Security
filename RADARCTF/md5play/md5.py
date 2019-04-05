import urllib2
from itertools import product
from string import ascii_lowercase

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]

for x in keywords:

		content = urllib2.urlopen("http://blackfoxs.org/radar/md5play/?md5=" + x).read()
		
		if "!=" not in contents:
			print content

radar{s0m3_bug5_1s_fun}