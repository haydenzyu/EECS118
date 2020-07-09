import cgi, cgitb, pymysql
import project_3_style as css

cgitb.enable()

form = cgi.FieldStorage()
gal_name = form.getvalue('edit_gal')
#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

display_upload = """<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_edited_gallery.py' method='POST'>
				Name: <input type='text' name="gallery_name"><br/>
				Description: <input type='text' name="description"><br/>
				"""
				
display_upload += "<input type='hidden' name='name_of_gal' value='"+gal_name+"'><input type='submit' value='Confirm'/></form>"

print("Content-Type: text/html")
print()
print("<TITLE>Edit Gallery</TITLE>")
print("<H1>Edit Gallery</H1>")
print(display_upload)


	
