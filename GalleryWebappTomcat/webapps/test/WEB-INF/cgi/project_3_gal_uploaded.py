import cgi, cgitb, pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()

if form.getvalue('gal_name')!="" or form.getvalue('description')!="":
	sql = "INSERT IGNORE INTO gallery(name, description) \
			VALUES(%s, %s)"
	val = (str(form.getvalue('gal_name')), str(form.getvalue('description')))
	cur.execute(sql, val)
	db.commit()
	display = "<TITLE>Uploaded</TITLE><H1>Uploaded</H1><form action='/test/cgi-bin/project_3.py'><button type='submit'>Go Back</button></form>"
	
else:
	display = "<TITLE>Not Uploaded</TITLE><H1>Not Uploaded, no input</H1><form action='/test/cgi-bin/project_3.py'><button type='submit'>Go Back</button></form>"

db.close()


print("Content-Type: text/html")
print()
print(display)