import cgi, cgitb, pymysql

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()

detail_id = form.getvalue('edit_detail')
gal = form.getvalue('gal_value')

display_detail = """<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_edited_detail.py' method='POST'>
				Title: <input type='text' name="title"><br/>
				URL: <input type='text' name="url"><br/>
				Year: <input type='text' name="year"><br/>
				Type: <input type='text' name="type"><br/>
				Width: <input type='text' name="width"><br/>
				Height: <input type='text' name="height"><br/>
				Location: <input type='text' name="location"><br/>
				Description: <input type='text' name="description"><br/>
				"""
display_detail += "<input type='hidden' name='edited_detail' value='"+str(detail_id)+"'>" + "<input type='hidden' name='gal_n' value='"+gal+"'>" + "<input type='submit' value='Confirm'/></form>"

print("Content-Type: text/html")
print()
print("<TITLE>Edit Detail</TITLE>")
print("<H1>Edit Detail</H1>")
print(display_detail)