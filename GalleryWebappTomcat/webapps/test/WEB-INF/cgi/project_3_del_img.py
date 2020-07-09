import cgi, cgitb, pymysql

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()
gallery_name = form.getvalue('del_img_gal')

print("Content-Type: text/html")
print()
if form.getvalue('del_name')!="":
	name = form.getvalue('del_name')
	query = "select detail_id from image where title=%s"
	cur.execute(query, name)
	img_detail_id = cur.fetchone()
	
	query = "delete from detail where detail_id=%s"
	cur.execute(query, str(img_detail_id[0]))
	
	query = "delete from image where title=%s"
	cur.execute(query, name)
	db.commit()
	print("<TITLE>Deleted</TITLE><H1>Deleted</H1>")
else:
	print("<TITLE>Not Deleted</TITLE><H1>No input, nothing is deleted</H1>")
	
display = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_gallery1.py' method='POST'><input type='hidden' name='gal_name' value='"+gallery_name+"'><button type='submit'>Go Back</button></form>"
print(display)
