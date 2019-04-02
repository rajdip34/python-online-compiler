# -*- coding: utf-8 -*-

import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest, \
	HttpResponseRedirect, HttpResponseBadRequest, Http404, JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from django.template.loader import get_template
from django.template import Template, Context

import os, sys, re, inspect
import shutil
from .funcs import load_nav_items, dirlibs, load_libs, CustomCompile, load_nav_a_folder
from django.conf import settings
import pymysql.cursors
from django.views.decorators.csrf import csrf_exempt


# @login_required
def index(request):
	context = {
		"nav": load_nav_items(),
		"rootpath":			dirlibs
	}
	return render(request, 'main.html', context)


@csrf_exempt
def nav_updater(request):
	return HttpResponse(load_nav_items())


@csrf_exempt
def nav_folder(request):
	folder = request.POST.get("folder")
	return render(request, "nav-folder.html", {
		"title":    folder,
		"path":     os.path.join(dirlibs,folder),
		"items":    load_nav_a_folder(folder).replace('\n','')
	})



@csrf_exempt
def chartdata(request):
	blockSize = 5

	lastid = 0
	res = {"data": [], "last": 0}


	if not request.POST.get("user") or not request.POST.get("name") or not request.POST.get("host"): 
		return JsonResponse(res, safe=False)


	dbconf = {
		"user": request.POST.get("user"), 
		"pass": request.POST.get("pass"), 
		"name": request.POST.get("name"),  
		"host": request.POST.get("host")
	}

	c = pymysql.connect(host=dbconf['host'], user=dbconf['user'], password=dbconf['pass'], db=dbconf['name'], charset='utf8',cursorclass=pymysql.cursors.DictCursor)
	try:
		with c.cursor() as cursor:
			sql = "SELECT * FROM `data` where "
			
			if request.POST.get("last"):
				lastid = request.POST.get("last")
			
			whereq = 'id>'+str(lastid)+" and "

			if request.POST.get("start_date"):
				sd = request.POST.get("start_date").replace("/","-")
				if sd!="":
					whereq += "date>='"+sd+"' and "

			if request.POST.get("end_date"): 
				en = request.POST.get("end_date").replace("/","-")
				if en!="":
					whereq += "date<='"+en+"' and "

			if request.POST.get("money"):
				m = request.POST.get("money") 
				if m!="":
					whereq += 'price<='+m+" and "

			sql += whereq.rstrip(' and ')

			sql += " limit "+str(blockSize)

			cursor.execute(sql)

			for row in cursor:
				row['date'] = str(row['date'])
				row['price'] = str(row['price'])
				res["data"].append(row)
				lastid = row['id']

			res['last'] = lastid
	finally:
		c.close()


	return JsonResponse(res, safe=False)



# @login_required
@csrf_exempt
def python_libs_js(request):
	libs = []
	methods = []

	for uri in load_libs():
		uri = uri.rstrip('.py').replace(os.sep, '.')

		if "." in uri:
			q = ""
			for x in uri.split("."):
				pq = q
				q += x
				libs.append(uri)
				if "." in q:
					methods.append("from " + pq.rstrip(".") + " import " + x)

				q += "."

		else:
			libs.append(uri)

	# sys.path.append(dirlibs)

	regex = r"^class\s([A-Z0-9a-z_]*)\s?\(|^def\s([A-Z0-9a-z_]*)\s?\("

	searchIn = [m.replace(' import ', '.').replace('from ', '') for m in methods] + [l.replace(' import ', '.') for l in libs]

	for m in searchIn:
		f = m.replace('.', os.sep) + '.py'
		f = os.path.join(dirlibs, f)

		if not os.path.isfile(f):
			continue

		with open(f, 'r') as f:
			text = f.read()
			f.close()

		matches = re.findall(regex, text, re.M)
		for i in matches:
			dest = i[1] if i[0] == "" else i[0]
			methods.append("from " + m + " import " + dest)

	response = 'libs = ' + str(json.dumps(list(set(libs)))) + ';\n methods = ' + str(json.dumps(list(set(methods)))) + ';\n'

	res = HttpResponse(response)
	res['CONTENT_TYPE'] = 'text/javascript'
	return res


# @login_required
@csrf_exempt
def commander(request):
	type = request.POST.get("type")
	if type == "savefile":
		path = request.POST.get("path").replace('+', ' ')
		text = request.POST.get("text")
		if os.sep not in path:
			path = os.path.join(dirlibs, path + '.py')
		pn = path.split(os.sep)
		pn = pn[len(pn) - 1]
		with open(path, 'w+') as f:
			f.write(text)

		return render(request ,"nav-file.html", {"name": pn, "path": path})

	elif type == "delete":
		p = request.POST.get("path").replace('+', '')
		os.remove(p) if os.path.isfile(p) else shutil.rmtree(p)
		return HttpResponse('')

	elif type == "load":
		p = request.POST.get("path").replace('+', '')
		with open(p, 'r') as f:
			file = f.read()
			f.close()
		return HttpResponse(file)

	elif type == "newfile":
		p = request.POST.get("path").replace('+', '')

		i = 1
		while True:
			pn = "newfile" + str(i) + ".py"
			pf = os.path.join(p, pn)
			if not os.path.isfile(pf):
				break
			i += 1

		with open(pf, 'w+') as f:
			f.write("# new file")

		return render(request, "nav-file.html", {"name": pn, "path": pf})


	elif type == "newfolder":
		p = request.POST.get('path').replace('+', '')

		i = 1
		while True:
			pn = "newfolder" + str(i);
			pf = os.path.join(p, pn)
			if not os.path.isdir(pf):
				break
			i += 1

		os.makedirs(pf)
		return render(request, "nav-folder.html", {"title": pn, "path": pf , "items": ""})

	elif type == "rename":
		current = request.POST.get("current").replace('+', " ")
		name = request.POST.get("name").replace('+', " ")

		path = os.path.join(os.path.dirname(current), name)

		os.rename(current, path)
		print(name + "," + path)
		return HttpResponse(name + "," + path)

	elif type == "uploadfile":
		name = request.POST.get('name').replace('+', '')
		text = request.POST.get('text')

		file = os.path.join(dirlibs, name)

		with open(file, 'w+') as f:
			f.write(text)

		return render(request, "nav-file.html", {"name": name, "path": file})

	elif type == "uploadfolder":
		name = request.POST.get('name').replace('+', '')
		arr = name.split("/")
		folders = arr[0:-1]
		name = arr[-1:][0]

		text = request.POST.get('text')

		folder = dirlibs
		for f in folders:
			folder = os.path.join(folder, f)
			if not os.path.isdir(folder):
				os.makedirs(folder)

		file = os.path.join(folder, name)

		with open(file, 'w+') as f:
			f.write(text)

		return HttpResponse('')

	elif type == "backtest" or type == "run":

		code = request.POST.get("code")

		# code_path = request.POST.get("file_name")
		# code = code.replace(chr(13), "")
		code = code.strip()

		filenames = [ os.path.join(dirlibs,"django_settings.py") ]
		setts = ""
		for f in filenames:
			if os.path.isfile(f):
				with open(f, 'r') as fh:
					setts += fh.read() + "\n"

		imports = "import sys \n"
		for f in os.listdir(dirlibs):
			ff = os.path.join(dirlibs, f)
			if os.path.isdir(ff):
				imports += "sys.path.append('"+ff+"')\n"
		return HttpResponse(CustomCompile(setts+imports+"\n"+code))

	elif type=="autocomplete_objs":
		code = request.POST.get("code")

		code = code.replace(chr(13), "")
		code = code.strip()
		lines = code.split("\n")
		el = lines[-1]
		el = el[0:el.find("{blinker}")]
		ln = len(el)
		for x in range(ln, 0, -1):
			if el[x-1] in [","," ","(",")","[","]"]:
				el = el[x:]
				break

		el = el.strip().rstrip('.')

		lines[-1] = ""
		lines.append("print('_X_start_X_')")
		lines.append("print([item for item in dir("+el+") if item[0:1]!='_'])")
		lines.append("print('_X_end_X_')")

		code = "\n".join(lines)

		return HttpResponse(CustomCompile(code))
	elif type=="autocomplete_vars":
		code = request.POST.get("code")

		code = code.replace(chr(13), "")
		lines = code.strip().split("\n")

		lines.append("print('_X_start_X_')")
		lines.append("print([item for item in locals().keys() if item[0:1]!='_' ])")
		lines.append("print('_X_end_X_')")

		code = "\n".join(lines)

		return HttpResponse(CustomCompile(code))

	elif type == "debugger":

		code = request.POST.get("code")
		bline = int(request.POST.get("break"))
		debuggerState = int(request.POST.get("debugger"))

		# code_path = request.POST.get("file_name")
		code = code.replace(chr(13), "")
		# code = code.strip()

		filenames = [ os.path.join(dirlibs,"django_settings.py") ]
		hlines = 0

		setts = ""
		for f in filenames:
			if os.path.isfile(f):
				with open(f, 'r') as fh:
					setts += fh.read() + "\n"
					hlines += 1

		imports = "import sys as _hj______sys\n"
		imports += "import traceback as _hj______traceback\n"
		hlines += 2
		for f in os.listdir(dirlibs):
			ff = os.path.join(dirlibs, f)
			if os.path.isdir(ff):
				imports += "_hj______sys.path.append('"+ff+"')\n"
				hlines += 1


		indent = ""
		lines = code.split("\n")

		if bline==-1:	
			lines.reverse()
			line = ""
			for li in lines:
				if li=="" or li.replace("\t","")=="":
					continue
				line = li
				break
		else:
			line = lines[bline]


		while line.startswith("\t"):
			indent += "\t"
			line = line[1:]

		indent = "\n"+indent

		if debuggerState==1:
			debugger = indent.join([
				"",
				"import json as _hj______json",
				"_hj______res = {}",
				"for k,v in locals().items():",
				"\tif k.startswith(\"_\"):",
				"\t\tcontinue",
				"\t_hj______res[k] = str(v)",
				"print('_X_start_vars_X_')",
				"print(_hj______json.dumps(_hj______res))",
				"print('_X_end_vars_X_')",
				"print('_X_start_trace_X_')",
				"print(_hj______json.dumps([line.strip() for line in _hj______traceback.format_stack()]))",
				"print('_X_end_trace_X_')",
				"exit()"
			])

			if bline==-1:
				code += debugger
			else:
				lines[bline] = debugger + "\n" + lines[bline]
				code = "\n".join(lines)

		out = "@+_!___!#".join([
			str(hlines),
			CustomCompile(setts+imports+"\n"+code)
		])

		return HttpResponse(out)
			




