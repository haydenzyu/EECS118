#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! This is my first CGI program</h2>')
print ('</body>')
print ("""<form><input type='submit' value='Upload'/></form>""")
print ('</html>')

###print """/Content-type:text/html\r\n\r\n
#<html>
#<head>
#<title>Hello - Second CGI Program</title>
#</head>
#<body>
#<h2>Hello</h2>
#</body>
#</html>