import cgi, cgitb, pymysql

form = cgi.FieldStorage()

db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()
gallery_name = form.getvalue('upload_img')

print("Content-Type: text/html")
print()
if form.getvalue('artist_name')!="" or form.getvalue('birth_year')!="" or form.getvalue('country')!="" or form.getvalue('description')!="":
	name = form.getvalue('artist_name')
	birth_year = form.getvalue('birth_year')
	country = form.getvalue('country')
	description = form.getvalue('description')
	query = "INSERT IGNORE INTO artist(name, birth_year, country, description) \
			VALUES(%s, %s, %s, %s)"
	val = (name, str(birth_year), country, description)
	cur.execute(query, val)
	db.commit()
	
	print("<TITLE>Added</TITLE><H1>Added</H1>")
else:
	print("<TITLE>Not Added</TITLE><H1>No input, nothing is added</H1>")


display = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_gallery1.py' method='POST'><input type='hidden' name='gal_name' value='"+gallery_name+"'><button type='submit'>Go Back</button></form>"

print(display)
