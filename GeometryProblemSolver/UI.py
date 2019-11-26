import cgi, cgitb
import css

def display_problem1():
    print("<h1>Problem 1</h1>")
    print(css.navbar % ('class="active"', "" ""))    
    print("<h3>Two triangles have two intersection points</h2>")
    print("""<h2>The intersections are on two different sides
           Only one vertex of a triangle is inside another triangle</h3>""")
    print("""<br><form enctype='multipart/form-data' action='/test/cgi-bin/new_gallery.py' method='post'>
        <p>%s galleries</p>
        <input type='hidden' id='gallery_id' name='gallery_id' value='%s'>
        <input type='submit' value='+'/>
        </form>""" % (count, form.getvalue('gallery_id')))

def display_problem2():
    print("<h1>Problem 2</h1>")
    print(css.navbar % ("", 'class="active"', ""))
    print("<h2>Two triangles have three intersection points</h2>")
    print("""<h3>Three intersections are on three different sides of a triangle 
           No side of a triangle is completely inside another triangle</h3>""")
    print("""<br><form enctype='multipart/form-data' action='/test/cgi-bin/new_gallery.py' method='post'>
        <p>%s galleries</p>
        <input type='hidden' id='gallery_id' name='gallery_id' value='%s'>
        <input type='submit' value='+'/>
        </form>""" % (count, form.getvalue('gallery_id')))

if __name__ == '__main__':
    cgitb.enable()
    form = cgi.FieldStorage()

    print("Content-Type: text/html")    # HTML is following
    print()                             # blank line, end of headers
    print("<TITLE>Geometry Solver</TITLE>")

    css.style()

    if (form.getvalue('problem') == 'first') or not form.getvalue('problem'):
        display_problem1()
    elif (form.getvalue('problem') == 'second'):
        display_problem2()
    
