#gallery 1

import cgi, cgitb, pymysql
import project_3_style as css

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

js = "<script>"
	
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

search_img = """<form id='search_img_box' enctype='multipart/form-data' action ='/test/cgi-bin/project_3_search.py' method='POST' target='_blank'>
				<input type='text' name='img_detail'/><br/>
				<input type='radio' name='search_img_type' value='type'> Type
				<input type='radio' name='search_img_type' value='year'> Year
				<input type='radio' name='search_img_type' value='artist'> Artist's name
				<input type='radio' name='search_img_type' value='location'> Location
				<input type='submit' value='Search Image'/></form>
			 """
search_artist = """<form id='search_artist_box' enctype='multipart/form-data' action ='/test/cgi-bin/project_3_search.py' method='POST' target='_blank'>
				   <input type='text' name='artist_detail'/><br/>
				   <input type='radio' name='search_artist_type' value='country' /> Country
				   <input type='radio' name='search_artist_type' value='birth_year' /> Birthday Year
				   <input type='submit' value='Search Artist'/></form>
				   """
				   
#get Gallery's Name
form = cgi.FieldStorage()
gal = form.getvalue('gal_name') 

query = "select gallery_id from gallery where name='"+gal+"'"
cur.execute(query)
gal_id = cur.fetchone()

#find max number of images in a gallery
query = "select*from image where gallery_id ='"+str(gal_id[0])+"'"
cur.execute(query)
max_num_img = cur.fetchall()

#upload image
display_upload = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_upload.py' method='POST'><input type='hidden' name='upload_img' value='"+gal+"'><input type='submit' value='Upload an Image'></form>"
display_delete = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_del_img.py' method='POST'>Image name:<input type='text' name='del_name'><input type='hidden' name='del_img_gal' value='"+gal+"'><input type='submit' value='Delete'></form>"
display_back = "<form action='/test/cgi-bin/project_3.py'><button type='submit'>Back to Galleries</button></form>"
display_create_artist = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_create_artist.py'><input type='hidden' name='upload_artist' value='"+gal+"'><button type='submit'>Add an Artist</button></form>"

print("Content-Type: text/html")
print()
print("<TITLE>%s</TITLE>"%(gal))
print(css.css)
print("<H1>%s%s%s%s</H1>"%(gal, display_back, display_create_artist, display_upload))
print(display_delete)
print(search_img+search_artist)
if max_num_img:
	query = "select link from image where gallery_id ='"+str(gal_id[0])+"'"
	cur.execute(query)
	gal_1_img = cur.fetchall() #all the links in the gallery
	for i in range(len(max_num_img)):
		#start of queries
		query = "select*from image where link='"+gal_1_img[i][0]+"'"
		cur.execute(query)
		img_detail = cur.fetchone()
		query = "select detail_id from image where link='"+gal_1_img[i][0]+"'"
		cur.execute(query)
		detail_id = cur.fetchone()
		query = "select*from detail where detail_id='"+str(detail_id[0])+"'"
		cur.execute(query)
		detail = cur.fetchone()
		query = "select artist_id from image where link='"+gal_1_img[i][0]+"'"
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
		display_imgs = "<img src='"+gal_1_img[i][0]+"' width="+str(detail[4])+"px height="+str(detail[5])+"px alt='img not found'>"
		display_img_title_link = "<h3 >"+str(img_detail[1])+"<br/><a href='"+str(img_detail[2])+"' >"+str(img_detail[2])+"</a></h3>"
		display_detail_tag = "<h4 id='img"+str(i)+"'></h4>"
		display_detail_button = "<button onclick='open_detail"+str(i)+"()'> Show Detail </button>"
		edit_detail_button = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_edit_detail.py' method='POST'><input type='hidden' name='edit_detail' value='"+str(detail_id[0])+"'><input type='hidden' name='gal_value' value='"+gal+"'><input type='submit' value='Edit Detail'></form>"
		display_artist_tag = "<h4 id='artist"+str(i)+"'></h4>"
		display_artist_button = "<button onclick='open_artist"+str(i)+"()'> Show Artist </button>"
		edit_artist_button = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_edit_artist.py' method='POST'><input type='hidden' name='edit_artist' value='"+str(artist_id)+"'><input type='hidden' name='gal_value' value='"+gal+"'><input type='submit' value='Edit Artist'></form>"
		display += display_imgs + display_img_title_link + display_detail_button + edit_detail_button + display_detail_tag + display_artist_button + edit_artist_button + display_artist_tag
		#end of string concatenation
		
	print(display)
	#print("%s"%())
else:
	display="<h4>No images, please upload</h4>"
	print(display)

js += "</script>" #end of js
print(js)
db.close()