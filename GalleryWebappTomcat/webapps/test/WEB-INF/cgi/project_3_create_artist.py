import cgi, cgitb, pymysql

cgitb.enable()

form = cgi.FieldStorage()

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()
name = form.getvalue('upload_artist')
display_upload = """<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_artist_added.py' method='POST'>
				Name: <input type='text' name="artist_name"><br/>
				Birth Year: <input type='text' name="birth_year"><br/>
				Country: <input type='text' name="country"><br/>
				Description: <input type='text' name="description"><br/>
				"""
				
display_upload += "<input type='hidden' name='upload_img' value='"+name+"'><input type='submit' value='Add'/></form>"

print("Content-Type: text/html")
print()
print("<TITLE>Add an Artist</TITLE>")
print("<H1>Add an Artist</H1>")
print(display_upload)
