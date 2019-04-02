

#!/usr/bin/env /media/mnt/env/COMPILER/bin/python
"""
blockSize = 5

import pymysql.cursors, json, cgi
print("Content-type: application/json\n") 


lastid = 0
res = {"data": [], "last": 0}
form = cgi.FieldStorage()


if not form.getvalue("user") or not form.getvalue("name") or not form.getvalue("host"): 
	print(json.dumps(res))
	exit()


dbconf = {
	"user":	form.getvalue("user"), 
	"pass":	form.getvalue("pass"), 
	"name":	form.getvalue("name"), 	
	"host":	form.getvalue("host")
}


c = pymysql.connect(host=dbconf['host'], user=dbconf['user'], password=dbconf['pass'], db=dbconf['name'], charset='utf8',cursorclass=pymysql.cursors.DictCursor)
try:
	with c.cursor() as cursor:
		sql = "SELECT * FROM `data` where "
		
		if form.getvalue("last"):
			lastid = form.getvalue("last")
		
		whereq = 'id>='+str(lastid)+" and "

		if form.getvalue("start_date"):
			sd = form.getvalue("start_date").replace("/","-")
			if sd!="":
				whereq += "date>='"+sd+"' and "

		if form.getvalue("end_date"): 
			en = form.getvalue("end_date").replace("/","-")
			if en!="":
				whereq += "date<='"+en+"' and "

		if form.getvalue("money"):
			m = form.getvalue("money") 
			if m!="":
				whereq += 'price<='+m+" and "

		sql += whereq.rstrip(' and ')

		sql += " limit "+str(lastid)+", "+str(blockSize)

		cursor.execute(sql)

		for row in cursor:
			row['date'] = str(row['date'])
			row['price'] = str(row['price'])
			res["data"].append(row)
			lastid = row['id']

		res['last'] = lastid
finally:
	c.close()


print(json.dumps(res))

"""