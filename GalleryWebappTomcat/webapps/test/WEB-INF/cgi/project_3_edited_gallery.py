import cgi, cgitb, pymysql
import project_3_style as css

form = cgi.FieldStorage()
gal_name = form.getvalue('name_of_gal')

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()


gallery_name = form.getvalue('gallery_name')
description = form.getvalue('description')

if gallery_name != "":
	query = "update gallery set name = %s where name='"+gal_name+"'"
	cur.execute(query, str(gallery_name))
	db.commit()

if description != "":
	query = "update gallery set description = %s where name='"+gal_name+"'"
	cur.execute(query, str(description))
	db.commit()
	
db.close()

print("Content-Type: text/html")
print()
print("<TITLE>Edited Gallery</TITLE>")
print("<H1>Edited Gallery</H1>")
print("<form action='/test/cgi-bin/project_3.py'><input type='submit' value='Go Back'></form>")
print(description)
