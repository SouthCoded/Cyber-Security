import zipfile
import os
import lzma
import tarfile



name = "password.x.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a"

os.system('unxz ' + name)
os.system('tar -xf ' + name)



while name != "password":
	print(name)
	# zip = zipfile.ZipFile(name)
	# zip.extractall()
	# name = name[0:len(name)-2]
	


	with tarfile.open(name) as f:
		f.extractall('.')

	name = name[0:len(name)-2]



