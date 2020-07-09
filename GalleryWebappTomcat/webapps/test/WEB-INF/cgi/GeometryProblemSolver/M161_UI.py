import cgi, cgitb
from css import selection as s
import css
from M161 import output
from M161 import predicates
from M161 import get_all

if __name__ == '__main__':
    cgitb.enable()
    form = cgi.FieldStorage()

    print("Content-Type: text/html")    # HTML is following
    print()                             # blank line, end of headers
    print("<TITLE>Geometry Solver</TITLE>")

    css.style()

    result = ''
    if form.getvalue('output'):
        for i in range(1,4):
            predicate = form.getvalue('pred'+str(i))
            answer = form.getvalue('txt'+str(i)).split(',')
            if not form.getvalue('txt'+str(i)) or form.getvalue('txt'+str(i)) == '':
                continue
            func = predicates.get(predicate, "not valid")
            if predicate == 'set_sum_value' or predicate == 'set_fraction':
                func(answer[0], answer[1], int(answer[2]))
            else:
                func(answer[0], answer[1])
        result = get_all()

    print("<h1>Geometry Problem Solver</h1>")
    print(css.navbar % ('class="active"', "", ""))
    print("<h2>Two triangles have three intersection points</h2>")
    print("""<h3>Three intersections are on three different sides of a triangle<br> 
           No side of a triangle is completely inside another triangle</h3>""")
    print("""<div id='container'>
            <div class='diagram'>
                <h2>Diagrams</h2>
                <img src='%s' alt='diagram 2'>
            </div>
            <div class='predicates'>
              <h2>Inputs</h2>
              <form enctype='multipart/form-data' action='/test/cgi-bin/GeometryProblemSolver/M161_UI.py' method='post'>
                    %s%s%s
                    <input type='hidden' name='output' value='output'>
                    <button type='submit' class='btn'>Get All</button>
              </form>
            </div>
            <div class='output'>
                <h2>Output</h2>
                <p>%s</p>
            </div>
        </div>""" % (css.p1_diagram, s.format('pred1', 'txt1'), s.format('pred2', 'txt2'), 
                s.format('pred3', 'txt3'), result))