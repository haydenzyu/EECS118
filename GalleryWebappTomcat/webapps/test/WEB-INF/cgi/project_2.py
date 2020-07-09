##  Hayden Yu   ##
##  66185399    ##
##  MP2         ##
##  10/14/19    ##

import cgi, cgitb

print("Content-Type: text/html")
print()
print("<TITLE>EECS 118 MP2</TITLE>")
print("<H1>Uploader</H1>")
print("<H2>First Image:</H2>")
print("""<form enctype="multipart/form-data" action="/test/cgi-bin/project_2_page2.py" method="POST">
		Upload First Image's URL Here: <input type='text' name='img1'><br />
		Title: <input type="text" name="img1_title"><br />
		Artist: <input type="text" name="img1_artist"><br />
		Year: <input type="text" name="img1_year"><br />
		Description: <input type="text" name="img1_des"><br />
		<H2>Second Image:</H2>
		Upload Second Image's URL Here: <input type='text' name='img2'<br><br>
		Title: <input type="text" name="img2_title"><br />
		Artist: <input type="text" name="img2_artist"><br />
		Year: <input type="text" name="img2_year"><br />
		Description: <input type="text" name="img2_des"><br />
		<input type='submit' value='Upload'/></form>""")


