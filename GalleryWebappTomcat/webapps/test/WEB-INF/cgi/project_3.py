##  Hayden Yu     ##
##  66185399      ##
##  Project 3	  ##
##  10/21/2019     ##


import cgi, cgitb, pymysql
import datetime as dt
import project_3_style as css

cgitb.enable()

#mysql Code
db = pymysql.connect(host = 'localhost',
                     user = 'gallery',
                     passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

query = "select name from gallery"
cur.execute(query)
gal_name = cur.fetchall()
gal_upload = "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_gal_upload.py' method='POST'><input type='submit' value='Upload'></form>"
if gal_name!=None:
	query = "select description from gallery"
	cur.execute(query)
	gal_des = cur.fetchall()

	query = "select max(gallery_id) from gallery"
	cur.execute(query)
	max_num_gal = cur.fetchone()
	max_num_gal = int(max_num_gal[0])

	display_gals = ""
	
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
				 

	for i in gal_name:
		query = "select gallery_id from gallery where name ='"+i[0]+"'"
		cur.execute(query)
		x = cur.fetchone()
		query = "select description from gallery where name ='"+i[0]+"'"
		cur.execute(query)
		y = cur.fetchone()
		query = "select link from image where gallery_id ='"+str(x[0])+"'"
		cur.execute(query)
		gal_img = cur.fetchone()
		if gal_img==None:
			gal_img = "none"
		display_gals += "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_gallery1.py' method='POST'>"
		display_gals += "<input type='hidden' name='gal_name' value='"+i[0]+"'>"
		display_gals += "<img src='"+gal_img[0]+"' width=200px height=200px alt='img not available'><br/>"
		display_gals += "Name: "+i[0]+"<input type='submit' value='VIEW'/><br/>"+"Description: "+y[0]+"</form>"
		display_gals += "<form enctype='multipart/form-data' action='/test/cgi-bin/project_3_edit_gallery.py' method='POST'><input type='hidden' name='edit_gal' value='"+i[0]+"'><input type='submit' value='EDIT'></form><br/>"

current_day = ""
if dt.datetime.now().hour >= 5 and dt.datetime.now().hour < 12:
	current_day = "Morning"
elif dt.datetime.now().hour >= 12 and dt.datetime.now().hour < 17:
	current_day = "Afternoon"
else:
	current_day = "Evening"
	
print("Content-Type: text/html")
print()
print("<TITLE>EECS 118 MP3</TITLE>")
print(css.css)
print("<H1>Good "+current_day+"<br/>Galleries"+gal_upload+"</H1>")
print(search_img+search_artist)
print(display_gals)
db.close()
