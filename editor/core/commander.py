#!/usr/bin/env /media/mnt/env/COMPILER/bin/python

"""
import shutil
from theme import dirlibs, template

print("Content-type: text/html\n\n")
import cgi, os, sys


form = cgi.FieldStorage()
type = form.getvalue("type")

if type=="savefile":
	path = form.getvalue("path").replace('+',' ')
	text = form.getvalue("text")

	if os.sep not in path:
		path = os.path.join( dirlibs, path+'.py')

	pn = path.split(os.sep)
	pn = pn[len(pn)-1]

	with open(path , 'w+') as f:
		f.write(text)

	print(template("nav-file",{"name":pn,"path":path}))

elif type=="delete":
	p = form.getvalue("path").replace('+','')
	os.remove(p) if os.path.isfile(p) else shutil.rmtree(p)

elif type=="load":
	p = form.getvalue("path").replace('+','')
	with open(p, 'r') as f:
		file = f.read()
		f.close()
	print(file)

elif type=="newfile":
	p = form.getvalue("path").replace('+','')


	i = 1
	while True:
		pn = "newfile"+str(i)+".py"
		pf = os.path.join(p, pn)
		if not os.path.isfile(pf):
			break
		i += 1

	with open(pf , 'w+') as f:
		f.write("# new file")

	print(template("nav-file",{"name":pn,"path":pf}))

elif type=="newfolder":
	p = form.getvalue("path").replace('+','')

	i = 1
	while True:
		pn = "newfolder"+str(i);
		pf = os.path.join(p, pn)
		if not os.path.isdir(pf):
			break
		i += 1

	os.makedirs(pf)
	print(template("nav-folder",{"title":pn,"path":pf,"items":""}))
	
elif type=="rename":
	current = form.getvalue("current").replace('+'," ")
	name = form.getvalue("name").replace('+'," ")
	
	path = os.path.join( os.path.dirname(current), name)

	os.rename(current, path)
	print(name+","+path)

elif type=="uploadfile":
	name = form.getvalue('name').replace('+','')
	text = form.getvalue('text')

	file = os.path.join( dirlibs, name)

	with open(file , 'w+') as f:
		f.write(text)
	print(template("nav-file",{"name":name,"path":file}))

elif type=="uploadfolder":
	name = form.getvalue('name').replace('+','')
	arr = name.split("/")
	folders = arr[0:-1]
	name = arr[-1:][0]

	text = form.getvalue('text')

	folder = dirlibs
	for f in folders:
		folder = os.path.join(folder, f)
		if not os.path.isdir(folder):
			os.makedirs(folder)

	file = os.path.join(folder, name)

	with open(file , 'w+') as f:
		f.write(text)

elif type=="backtest" or type=="run":
		
	code = form.getvalue("code")

	code = code.replace(chr(13), "")
	code = code.strip()

	for f in os.listdir(dirlibs):
		ff = os.path.join(dirlibs,f)
		if os.path.isdir(ff):
			sys.path.append(ff)


	try:
		rel = compile(code, 'test', 'exec')
		pi = exec(rel, {})
	except:
		a, b, c = sys.exc_info()
		line_number = c.tb_lineno 
		print(b)
		print(c)
"""