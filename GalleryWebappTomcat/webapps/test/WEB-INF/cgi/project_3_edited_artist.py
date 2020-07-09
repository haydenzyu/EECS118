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
id = form.getvalue('edited_artist')

birth_year = form.getvalue('birth_year')
country = form.getvalue('country')
description = form.getvalue('description')

query = "update artist set birth_year = %s where artist_id='"+id[1]+"'"

if birth_year != "":
	query = "update artist set birth_year = %s where artist_id='"+id[1]+"'"
	cur.execute(query, str(birth_year))
	db.commit()
	
if country != "":
	query = "update artist set country = %s where artist_id='"+id[1]+"'"
	cur.execute(query, str(country))
	db.commit()
	
if description != "":
	query = "update artist set description = %s where artist_id='"+id[1]+"'"
	cur.execute(query, str(description))
	db.commit()

display = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_gallery1.py' method='POST'><input type='hidden' name='gal_name' value='"+gallery_name+"'><button type='submit'>Go Back</button></form>"

print("Content-Type: text/html")
print()
print("<TITLE>Edited</TITLE>")
print("<H1>Edited</H1>")
print(display)
db.close()