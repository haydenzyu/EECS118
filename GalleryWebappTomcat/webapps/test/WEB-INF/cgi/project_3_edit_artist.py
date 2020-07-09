import cgi, cgitb, pymysql

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor();

form = cgi.FieldStorage()

id = form.getvalue('edit_artist')
gal = form.getvalue('gal_value')

display_detail = """<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_edited_artist.py' method='POST'>
				Birth Year: <input type='text' name="birth_year"><br/>
				Country: <input type='text' name="country"><br/>
				Description: <input type='text' name="description"><br/>
				"""
				
if id == 0:
	display_detail = "Artist doesn't exist, please create one"
	display_detail += ""
else:
	display_detail += "<input type='hidden' name='edited_artist' value='"+str(id)+"'>" + "<input type='hidden' name='gal_n' value='"+gal+"'>" + "<input type='submit' value='Confirm'/></form>"

print("Content-Type: text/html")
print()
print("<TITLE>Edit Artist</TITLE>")
print("<H1>Edit Artist</H1>")
print(display_detail)