import cgi, cgitb, os
cgitb.enable()

form = cgi.FieldStorage()

#first image's values
if form.getvalue('img1_title'):
	img1_title = "Title: "+form.getvalue('img1_title')
else:
	img1_title = 'no title'
if form.getvalue('img1_artist'):
	img1_artist = "Artist: "+form.getvalue('img1_artist')
else:
	img1_artist = 'no artist'
if form.getvalue('img1_year'):
	img1_year = "Year: "+form.getvalue('img1_year')
else:
	img1_year = 'no year'
if form.getvalue('img1_des'):
	img1_des = "Description: "+form.getvalue('img1_des')
else:
	img1_des = 'no description'
if form.getvalue('img1'):
	img1 = form.getvalue('img1')
else:
	img1 = "no image"

#second image's values
if form.getvalue('img2_title'):
	img2_title = "Title: "+form.getvalue('img2_title')
else:
	img2_title = 'no title'
if form.getvalue('img2_artist'):
	img2_artist = "Artist: "+form.getvalue('img2_artist')
else:
	img2_artist = 'no artist'
if form.getvalue('img2_year'):
	img2_year = "Year: "+form.getvalue('img2_year')
else:
	img2_year = 'no year'
if form.getvalue('img2_des'):
	img2_des = "Description: "+form.getvalue('img2_des')
else:
	img2_des = 'no description'
if form.getvalue('img2'):
	img2 = form.getvalue('img2')
else:
	img2 = "no image"

#Java Script
js = """<script> 
function change_img_to2(){
	document.getElementById("main_title").innerHTML = 'Image 2';
	document.getElementById("img").src = '%s';
	document.getElementById("title_in").innerHTML = '%s';
	document.getElementById("artist_in").innerHTML = '%s';
	document.getElementById("year_in").innerHTML = '%s';
	document.getElementById("des_in").innerHTML = '%s';
}

function change_img_to1(){
	document.getElementById("main_title").innerHTML = 'Image 1';
	document.getElementById("img").src = '%s';
	document.getElementById("title_in").innerHTML = '%s';
	document.getElementById("artist_in").innerHTML = '%s';
	document.getElementById("year_in").innerHTML = '%s';
	document.getElementById("des_in").innerHTML = '%s';
}
</script>"""

print("Content-Type: text/html")
print()
print(js%(img2, img2_title,img2_artist,img2_year,img2_des, img1, img1_title,img1_artist,img1_year,img1_des))#insert JS here
print("<h1 id='main_title'>Image 1</h1>")
print("""<img src='%s' width=300px height=300px alt="no image" id='img'><br />"""%(img1)) #display image here
#display image's info
print("<h4 id='title_in'>%s</h4>"%(img1_title)) 
print("<h4 id='artist_in'>%s</h4>"%(img1_artist))
print("<h4 id='year_in'>%s</h4>"%(img1_year))
print("<h4 id='des_in'>%s</h4>"%(img1_des))
#switching buttons
print("<button type='button' name='first_image' onclick='change_img_to1()'>First Image</button>")
print("<button type='button' name='second_image' onclick='change_img_to2()'>Second Image</button>")

 