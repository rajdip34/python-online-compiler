#!/usr/bin/env /media/mnt/env/COMPILER/bin/python
"""
import cgi
from os import path
from theme import load_nav_a_folder, dirlibs, template

print("Content-type: text/html\n\n")
form = cgi.FieldStorage()
try:
	folder = form.getvalue("folder")
	print(template("nav-folder",{
		"title":folder,
		"path":path.join(dirlibs,folder),
		"items":load_nav_a_folder(folder).replace('\n','')
	}))
except:
	pass
"""