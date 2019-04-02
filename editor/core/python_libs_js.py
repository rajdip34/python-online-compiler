#!/usr/bin/env /media/mnt/env/COMPILER/bin/python

"""
import json, sys, os, re
from theme import load_libs, dirlibs


print("Content-type: text/html\n\n")

libs = []
methods = []


for uri in load_libs():
	uri = uri.rstrip('.py').replace(os.sep,'.')
	if "." in uri:
		q = ""
		for x in uri.split("."):
			pq = q
			q += x
			libs.append(uri)
			if "." in q:
				methods.append("from "+pq.rstrip(".")+" import "+x)
				
			q += "."

	else:
		libs.append(uri)

sys.path.append(dirlibs)

regex = r"^class\s([A-Z0-9a-z_]*)\s?\(|^def\s([A-Z0-9a-z_]*)\s?\("

for m in methods:
	m = m.replace(' import ','.').replace('from ','')
	f = m.replace('.', os.sep)+'.py'
	f = os.path.join(dirlibs, f)

	if not os.path.isfile(f):
		continue

	with open(f,'r') as f:
		text = f.read()
		f.close()

	matches = re.findall(regex, text, re.M)
	for i in matches:
		dest = i[1] if i[0]=="" else i[0]
		methods.append("from "+m+" import "+dest)


print('libs = '+str(json.dumps(list(set(libs))))+';\n')
print('methods = '+str(json.dumps(list(set(methods))))+';\n')

"""
