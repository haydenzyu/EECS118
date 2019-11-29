
p1_diagram = '/images/p2_diagram.JPG'
p2_diagram = '/images/p1_diagram.JPG'

selection = """<select name='{}' class='select-css'>
                <option value='set_parallel'>set_parallel</option>
                <option value='set_perpendicular'>set_perpendicular</option>
                <option value='set_equal'>set_equal</option>
                <option value='set_fraction'>set_fraction</option>
                <option value='set_sum_value'>set_sum_value</option>
                <option value='set_similar'>set_similar</option>
                <option value='set_congruent'>set_congruent</option>
        </select>
        <input name='{}' type='text' placeholder='Ex. a1,a2,90' size='15' maxlength='18'>
        <br><br>
        """

navbar = """<ul>
        <li><a %s href="/test/cgi-bin/GeometryProblemSolver/M161_UI.py">Problem 1</a></li>
        <li><a %s href="/test/cgi-bin/GeometryProblemSolver/M261_UI.py">Problem 2</a></li>
        %s
        </ul>"""

def style():
    print("""<style>
    body,h1,h2,h3,h4,h5,h6{
        font-family: "Montserrat", sans-serif;
        color: #000
    }

    h1 {
        text-align: center;
    }

    img {
        width: 98%;
    }

    div {
        display: block;
    }

    container {
        width: 100%;
        overflow: auto;
        position: absolute;
        height: auto;
    }

    .diagram, .predicates, .output {
        height: 100%;
    }

    .diagram {
        float: left;
        width: 50%;
    }

    .predicates {
        float: left;
        width: 25%;
    }

    .output {
        float: left;
        width: 25%;
    }

    @media only screen and (max-width: 1000px) {
        .diagram, .predicates, .output {
                height: 50%;
        }

        .diagram {
                float: left;
                width: 100%;
        }

        .predicates {
                float: left;
                width: 50%;
        }
        
        .output {
                float: left;
                width: 50%;
        }

    }

    .btn {
        background-color: #4CAF50;
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        width: 100%;
        opacity: 0.9;
        border-radius: .2em;
    }

    .btn:hover {
        opacity: 1;
    }

    input[type=text] {
        width: 49%;
        height: 35px;
        padding: .6em 1.4em .5em .8em;
        font-size: 14px;
        font-family: "Montserrat", sans-serif;
	color: #444;
        border: solid #ccc;
        border-radius: .2em;
        outline: none;
    }

    input[type=text]:focus {
        border: solid #555;
    }

    .select-css {
        -moz-appearance: none;
	-webkit-appearance: none;
	appearance: none;
	width: 49%;
        font-size: 14px;
        font-family: "Montserrat", sans-serif;
        font-weight: 700;
	color: #444;
	padding: .6em 1.4em .5em .8em;
	border-radius: .2em;
	background-color: #fff;
	background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23007CB2%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E'),
	linear-gradient(to bottom, #ffffff 0%,#e5e5e5 100%);
	background-repeat: no-repeat, repeat;
	background-position: right .7em top 50%, 0 0;
	background-size: .65em auto, 100%;
    }
    
    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: #545454;
        width: 100%
        position: sticky;
        top: 0;
    }

    li {
        float: left
    }

    li a {
        display: block;
        color: white;
        text-align: center;
        padding: 15px 20px;
        text-decoration: none;
    }

    li a:hover:not(.active) {
        background-color: #000
    }

    .active {
        background-color: #000
    }
    </style>""")