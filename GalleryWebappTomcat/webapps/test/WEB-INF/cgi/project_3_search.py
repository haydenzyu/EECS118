import cgi, cgitb, pymysql
import project_3_style as css

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()

search_img_type = form.getvalue('search_img_type')
search_img_term = form.getvalue('img_detail')
search_artist_type = form.getvalue('search_artist_type')
search_artist_term = form.getvalue('artist_detail')

display = ""
display_imgs = ""
display_img_title_link = ""


img_detail = ""
display_details = ""
detail = ""
detail_id = 0
display_detail_tag = ""
display_detail_button = ""
edit_detail_button = ""

artist = ""
artist_id = 0
artist_detail = ""
display_artist = ""
display_artist_tag = ""
display_artist_button = ""
edit_artist_button = ""

print("Content-Type: text/html")
print()
print("<TITLE>Result</TITLE>")
print(css.css)
print("<h1>Result</h1>")


if search_img_type:
	search_img_type = search_img_type
	js = "<script>"

	if search_img_type == "type":
		query = "select image_id from detail where type='"+search_img_term+"'"
		cur.execute(query)
		imgs = cur.fetchall()
	elif search_img_type == "year":
		query = "select image_id from detail where year='"+search_img_term+"'"
		cur.execute(query)
		imgs = cur.fetchall()
	elif search_img_type == "location":
		query = "select image_id from detail where location='"+search_img_term+"'"
		cur.execute(query)
		imgs = cur.fetchall()
	elif search_img_type == "artist":
		query = "select artist_id from artist where name='"+search_img_term+"'"
		cur.execute(query)
		artist_id = cur.fetchone()
		query = "select image_id from image where artist_id='"+str(artist_id[0])+"'"
		cur.execute(query)
		imgs = cur.fetchall()
	
	if len(imgs):
		for i in range(len(imgs)):
			#start of queries
			query = "select link from image where image_id ='"+str(imgs[i][0])+"'"
			cur.execute(query)
			img_link = cur.fetchone()
			
			query = "select*from image where link='"+img_link[0]+"'"
			cur.execute(query)
			img_detail = cur.fetchone()
			query = "select detail_id from image where link='"+img_link[0]+"'"
			cur.execute(query)
			detail_id = cur.fetchone()
			query = "select*from detail where detail_id='"+str(detail_id[0])+"'"
			cur.execute(query)
			detail = cur.fetchone()
			query = "select artist_id from image where link='"+img_link[0]+"'"
			cur.execute(query)
			artist_id = cur.fetchone()
			
			#if the artist doesn't exist, js for displaying artist
			if artist_id[0] == 0:
				display_artist = "Artist is not added"
				js += "\n\tfunction open_artist"+str(i)+"(){\n\t\tdocument.getElementById('artist"+str(i)+"').innerHTML ='"+str(display_artist)+"';}"
			else:
				query = "select*from artist where artist_id='"+str(artist_id[0])+"'"
				cur.execute(query)
				artist_detail = cur.fetchone()
				display_artist = "Name: "+str(artist_detail[1])+"<br />Birth Year: "+str(artist_detail[2])+"<br />Coutry: "+str(artist_detail[3])+"<br />Description: "+str(artist_detail[4])
				js += "\n\tfunction open_artist"+str(i)+"(){\n\t\tdocument.getElementById('artist"+str(i)+"').innerHTML ='"+str(display_artist)+"';}"
			#end of queries
			
			#js for displaying details
			display_details = "Year: "+str(detail[2])+"<br />Type: "+str(detail[3])+"<br />Width: "+str(detail[4])+"<br />Height: "+str(detail[5])+"<br />Location: "+str(detail[6])+"<br />Description: "+str(detail[7])
			js += "\n\tfunction open_detail"+str(i)+"(){\n\t\tdocument.getElementById('img"+str(i)+"').innerHTML ='"+str(display_details)+"';}"
			
			
			#start of string concatenation
			display_imgs = "<img src='"+img_link[0]+"' width="+str(detail[4])+"px height="+str(detail[5])+"px alt='img not found'>"
			display_img_title_link = "<h3 >"+str(img_detail[1])+"<br/><a href='"+str(img_detail[2])+"' >"+str(img_detail[2])+"</a></h3>"
			display_detail_tag = "<h4 id='img"+str(i)+"'></h4>"
			display_detail_button = "<button onclick='open_detail"+str(i)+"()'> Show Detail </button>"
			display_artist_tag = "<h4 id='artist"+str(i)+"'></h4>"
			display_artist_button = "<button onclick='open_artist"+str(i)+"()'> Show Artist </button>"
			display += display_imgs + display_img_title_link + display_detail_button + display_detail_tag + display_artist_button + display_artist_tag
			#end of string concatenation
			
		print(display)
	else:
		display="<h4>No images, please upload</h4>"
		print(display)

	js += "</script>" #end of js
	print(js)
	db.close()

elif search_artist_type:
	search_artist_type = search_artist_type

	if search_artist_type == "country":
		query = "select artist_id from artist where country='"+search_artist_term+"'"
		cur.execute(query)
		ids = cur.fetchall()
	elif search_artist_type == "birth_year":
		query = "select artist_id from artist where birth_year='"+search_artist_term+"'"
		cur.execute(query)
		ids = cur.fetchall()
	
	if len(ids):
		for i in range(len(ids)):
			if ids[i][0] != 0:
				#start of queries
				query = "select*from artist where artist_id ='"+str(ids[i][0])+"'"
				cur.execute(query)
				artist_detail = cur.fetchone()
				display_artist = "Name: "+str(artist_detail[1])+"<br />Birth Year: "+str(artist_detail[2])+"<br />Coutry: "+str(artist_detail[3])+"<br />Description: "+str(artist_detail[4])+"<br/><br/>"
			else:
				display_artist = "Artist is not added"
			
			#start of string concatenation
			display += display_artist
			#end of string concatenation
			
		print(display)
	else:
		display="<h4>No such Artist, please add</h4>"
		print(display)

	db.close()
else:
	search_img_type = None
	search_artist_type = None
	display = "Select a search option"