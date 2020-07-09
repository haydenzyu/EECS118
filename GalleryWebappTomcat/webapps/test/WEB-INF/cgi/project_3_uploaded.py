import cgi, cgitb, pymysql

form = cgi.FieldStorage()

db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

query =""
gallery_name = form.getvalue('upload_img')
query = "select gallery_id from gallery where name='"+gallery_name+"'"
cur.execute(query)
id = cur.fetchone()

if form.getvalue('url')!="" or form.getvalue('title')!="" or form.getvalue('artist')!="" or form.getvalue('year')!="" or form.getvalue('type')!="" or form.getvalue('width')!="" or form.getvalue('height')!="" or form.getvalue('location')!="" or form.getvalue('description')!="":
	url = form.getvalue('url')
	title = form.getvalue('title')
	artist = form.getvalue('artist')
	year = form.getvalue('year')
	type = form.getvalue('type')
	width = form.getvalue('width')
	height = form.getvalue('height')
	location = form.getvalue('location')
	description = form.getvalue('description')

	query = "INSERT IGNORE INTO detail(year, type, width, height, location, description) \
				VALUES(%s, %s, %s, %s, %s, %s)"
	val = (year, type, width, height, location, description)
	cur.execute(query, val)
	db.commit()

	query = "select max(detail_id) from detail"
	cur.execute(query)
	max_num_detail = cur.fetchone()
	
	if artist!="":
		query = "select artist_id from artist where name='"+artist+"'"
		cur.execute(query)
		artist_id = cur.fetchone()
		artist_id = artist_id[0]
	else:
		artist_id = None

	query = "INSERT IGNORE INTO image(title, link, gallery_id, artist_id, detail_id) \
				VALUES(%s, %s, %s, %s, %s)"
	val = (title, url, str(id[0]), str(artist_id), str(max_num_detail[0]))
	cur.execute(query, val)
	db.commit()

	query = "select max(image_id) from image"
	cur.execute(query)
	max_num_image = cur.fetchone()
	max_num_image = int(max_num_image[0])

	query = "update detail set image_id = %s where detail_id='"+str(max_num_detail[0])+"'"
	cur.execute(query, str(max_num_image))
	db.commit()

	db.close()
	display = "<TITLE>Uploaded</TITLE><H1>Uploaded</H1>"
else:
	display = "<TITLE>Not uploaded</TITLE><H1>No input, not uploaded</H1>"

display += "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_gallery1.py' method='POST'><input type='hidden' name='gal_name' value='"+gallery_name+"'><button type='submit'>Go Back</button></form>"
print("Content-Type: text/html")
print()
print(display)