import cgi, cgitb, pymysql

display = """<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_gal_uploaded.py' method='POST'>
			 Name: <input type='text' name='gal_name'><br/>
			 Description: <input type='text' name='description'><br/>
			 <input type='submit' value='Upload'></form>"""

print("Content-Type: text/html")
print()
print("<TITLE>Upload a Gallery</TITLE>")
print("<H1>Upload a Gallery</H1>")
print(display)

	

	
