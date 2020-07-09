import cgi, cgitb, pymysql

form = cgi.FieldStorage()

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

display_upload = """<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_uploaded.py' method='POST'>
				URL: <input type='text' name="url"><br/>
				Title: <input type='text' name="title"><br/>
				Artist: <input type='text' name="artist"><br/>
				Year: <input type='text' name="year"><br/>
				Type: <input type='text' name="type"><br/>
				Width: <input type='text' name="width"><br/>
				Height: <input type='text' name="height"><br/>
				Location: <input type='text' name="location"><br/>
				Description: <input type='text' name="description"><br/>
				
				"""

display_upload += "<input type='hidden' name='upload_img' value='"+form.getvalue('upload_img')+"'>" + "<input type='submit' value='Upload'/></form>"


print("Content-Type: text/html")
print()
print("<TITLE>Upload</TITLE>")
print("<H1>Upload</H1>")
print(display_upload)
