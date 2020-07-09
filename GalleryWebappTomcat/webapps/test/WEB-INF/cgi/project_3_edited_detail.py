import cgi, cgitb, pymysql

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()
query = ""

form = cgi.FieldStorage()

gallery_name = form.getvalue('gal_n')
id = form.getvalue('edited_detail')

title = form.getvalue('title')
url = form.getvalue('url')
year = form.getvalue('year')
type = form.getvalue('type')
width = form.getvalue('width')
height = form.getvalue('height')
location = form.getvalue('location')
description = form.getvalue('description')

if title!="":
	query = "update image set title = %s where detail_id='"+str(id)+"'"
	cur.execute(query, str(title))
	db.commit()

if url!="":
	query = "update image set link = %s where detail_id='"+str(id)+"'"
	cur.execute(query, str(url))
	db.commit()

if year != "":
	query = "update detail set year = %s where detail_id='"+str(id)+"'"
	cur.execute(query, str(year))
	db.commit()
	
if type != "":
	query = "update detail set type = %s where detail_id='"+str(id)+"'"
	cur.execute(query, type)
	db.commit()
	
if width != "":
	query = "update detail set width = %s where detail_id='"+str(id)+"'"
	cur.execute(query, str(width))
	db.commit()
	
if height != "":
	query = "update detail set height = %s where detail_id='"+str(id)+"'"
	cur.execute(query, str(height))
	db.commit()
	
if location != "":
	query = "update detail set location = %s where detail_id='"+str(id)+"'"
	cur.execute(query, location)
	db.commit()

if description != "":
	query = "update detail set description = %s where detail_id='"+str(id)+"'"
	cur.execute(query, description)
	db.commit()


display = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_gallery1.py' method='POST'><input type='hidden' name='gal_name' value='"+gallery_name+"'><button type='submit'>Go Back</button></form>"

print("Content-Type: text/html")
print()
print("<TITLE>Edited</TITLE>")
print("<H1>Edited</H1>")
print(display)
db.close()