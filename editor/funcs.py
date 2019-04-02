from os import path, walk, listdir
import os, subprocess
from django.template.loader import render_to_string
from django.conf import settings
from tempfile import NamedTemporaryFile
import shlex
import os
from subprocess import Popen, PIPE



template_path = path.join( path.dirname(path.dirname(path.realpath(__file__))), 'theme')
dirlibs = path.join(path.dirname(path.realpath(__file__)), 'files')

def load_files():
	global dirlibs
	res = []

	for dirpath, dirnames, filenames in walk(dirlibs):
		for d in dirnames:
			dpath = path.join(dirpath, d)
			# print(dpath)
			if len(listdir(dpath))==0:
				res.append(dpath.replace(dirlibs,'').lstrip(os.sep)+os.sep)

		for filename in [f for f in filenames if f.endswith(".py")]:
			uri = path.join(dirpath, filename)

			res.append(uri.replace(dirlibs,'').lstrip(os.sep))

	# print(res)
	# exit()
	return res


def load_libs():
	global dirlibs
	res = []

	for dirpath, dirnames, filenames in walk(dirlibs):
		for d in dirnames:
			dpath = path.join(dirpath, d)
			# print(dpath)
			if len(listdir(dpath))==0:
				res.append(dpath.replace(dirlibs,'').lstrip(os.sep)+os.sep)
				
		for filename in filenames:
			if filename.endswith('.py'):
				uri = path.join(dirpath, filename)
				
				if '__init__' in uri:
					continue 

				res.append(uri.replace(dirlibs,'').lstrip(os.sep))

	return res


def template(tmpl, data={}):
	global template_path
	uri = path.join(template_path, tmpl+'.html')

	if not path.isfile(uri):
		print("Template "+str(tmpl)+" doesn't exists.")
		exit()

	f = open(uri, 'r')
	temp = f.read()
	f.close()

	for k, v in data.items():
		temp = temp.replace("{{"+k+"}}", v)

	return temp


def set_val_inside_folder(item, res):
	if item=="":
		pass
	elif os.sep not in item:
		res["files"].append(item)
	else:
		arr = item.split(os.sep)
		if arr[0] not in res["folders"]:
			res["folders"][arr[0]] = {"files":[], "folders":{}}

		res["folders"][arr[0]] = set_val_inside_folder(os.sep.join(arr[1:]), res["folders"][arr[0]])
	
	return res


def group_editable_files_and_folders():
	res = {".":{"files":[], "folders":{}}}

	for item in load_files():
		# print([item, "os.sep" not in item])
		# continue
		if os.sep not in item:
			res["."]["files"].append(item)
		else:
			# if item not in res["."]["folders"]:
			# 	res["."]["folders"][item] = {"files":[], "folders":{}}
			res["."] = set_val_inside_folder(item, res["."])
	# print(res)
	# exit()
	return res


def generate_nav_loop(ref, path):
	nav = ""
	for f in ref['files']:
		nav += render_to_string("nav-file.html",{"name":f,"path":path+os.sep+f})+"\n"

	for fn, fv in ref['folders'].items():
		nav += render_to_string("nav-folder.html", {"title":fn,"path":path+os.sep+fn,"items":generate_nav_loop(fv,path+os.sep+fn)})+"\n"

	return nav


def load_nav_items():
	global dirlibs
	return generate_nav_loop(group_editable_files_and_folders()['.'],  dirlibs)


def load_nav_a_folder(fn):
	global dirlibs
	f = path.join(dirlibs,fn)
	return generate_nav_loop(group_editable_files_and_folders()['.']['folders'][fn],  f)


def CustomCompile(code):
	global dirlibs
	temp = NamedTemporaryFile(mode='w+', delete=False)
	code = "#!/usr/bin/python\nimport sys as _hj______sys\n_hj______sys.path.append('"+dirlibs+"')\n" + code
	temp.write(code)
	f = str(temp.name)
	temp.close()
	os.chmod(f, 0o777)

	process = Popen(f, stdout=PIPE, stderr=PIPE, shell=False)
	stdout, stderr = process.communicate()
	
	res = stdout
	res +=b'\n'+ stderr 


	return res
