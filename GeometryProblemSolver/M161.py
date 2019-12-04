# from objects import *

class Part:
    def __init__(self, name):
        self.name = name
        self.parallel = []
        self.perpendicular = []
        self.equal = []
        self.sum_value = {}
        self.fraction = {}
        self.similar = []
        self.congruent = []

class Angle(Part):
    def __init__(self, name):
        self.name = name
        self.right_angle = False
        self.angle = 0
        Part.__init__(self, name)
        
ar1 = Part('ar1'); ar2 = Part('ar2'); ar3 = Part('ar3'); ar4 = Part('ar4')
sa1 = Part('sa1'); sb1 = Part('sb1'); sc1 = Part('sc1')
sa2 = Part('sa2'); sb2 = Part('sb2'); sc2 = Part('sc2')
sa3 = Part('sa3'); sb3 = Part('sb3'); sc3 = Part('sc3')
sa4 = Part('sa4'); sb4 = Part('sb4'); sc4 = Part('sc4')
sa5 = Part('sa5'); sb5 = Part('sb5')
sa6 = Part('sa6'); sb6 = Part('sb6')
a1 = Angle('a1'); b1 = Angle('b1'); c1 = Angle('c1')
a2 = Angle('a2'); b2 = Angle('b2'); c2 = Angle('c2')
a3 = Angle('a3'); c3 = Angle('c3')
b4 = Angle('b4'); c4 = Angle('c4')
d1 = Angle('d1'); d2 = Angle('d2'); d3 = Angle('d3'); d4 = Angle('d4')

angles = [a1, b1, c1, a2, b2, c2, a3, c3, b4, c4, d1, d2, d3, d4]

output = {}

init = True

# add known relations to output dictionary 
def initialize():
    global init
    if not init:
        return
    init = False

    set_equal('d1', 'a1')
    set_equal('d2', 'b2')
    set_sum_value('a1', 'd3', 180)
    set_sum_value('d1', 'd3', 180)
    set_sum_value('d2', 'd4', 180)
    set_sum_value('b2', 'd4', 180)
    set_sum_value('sa5', 'sb1', 'sb3')
    set_sum_value('sa2', 'sb5', 'sc3')
    set_sum_value('sa6', 'sc1', 'sa4')
    set_sum_value('sb6', 'sc2', 'sb4')
    set_sum_value('sa1', 'sb2', 'sc4')

def get_all():
    # Congruent: SSS, SAS, ASA, AAS, HL
    # Similar: AAA
    return output

def is_same_edge(n1, n2):
    edges = [['sb3', 'sa5', 'sb1'], 
        ['sc3', 'sb5', 'sa2'], 
        ['sa4', 'sa6', 'sc1'], 
        ['sb4', 'sb6', 'sc2'],
        ['sc4', 'sa1', 'sb2']]
    for e in edges:
        if n1 in e and n2 in e:
            return True
    return False

#When a “parallel” predicate is given
def set_parallel(name1, name2):
    initialize()
    # if name1 in globals()[name2].parallel:
    #     return
    if is_same_edge(name1, name2) or is_same_edge(name2, name1):
        return
    # add pair to output and add to objects parallel list
    if 'parallel' in output:
        if name1 in globals()[name2].parallel:
            return
        output['parallel'].append([name1, name2]) 
    else:
        output['parallel'] = [[name1, name2]]
    x = globals()[name1].parallel
    x.append(name2)
    y = globals()[name2].parallel
    y.append(name1)

    merge_parallel(globals()[name1], globals()[name2])

    # call "know" functions
    globals()['know_'+name1]()
    globals()['know_'+name2]()
    
# true is 2 line segments are perpendicular
def set_perpendicular(name1, name2): 
    initialize()

    # if name1 in globals()[name2].perpendicular:
    #     return
    if 'perpendicular' in output:
        if name1 in globals()[name2].perpendicular:
            return
        output['perpendicular'].append([name1, name2]) 
    else:
        output['perpendicular'] = [[name1, name2]]
    x = globals()[name1].perpendicular
    x.append(name2)
    y = globals()[name2].perpendicular
    y.append(name1)

    globals()['know_'+name1]()
    globals()['know_'+name2]()

#true if 2 angles, line segments, or areas are equal
def set_equal(name1, name2): 
    initialize()
    if name1 == name2:
        return
    if 'equal' in output:
        if name1 in globals()[name2].equal:
            return
        output['equal'].append([name1, name2]) 
    else:
        output['equal'] = [[name1, name2]]
    x = globals()[name1].equal
    x.append(name2)
    y = globals()[name2].equal
    y.append(name1)

    merge_equals(globals()[name1], globals()[name2])
    merge_sums(globals()[name1], globals()[name2])
    merge_fracs(globals()[name1], globals()[name2])

    globals()['know_'+name1]()
    globals()['know_'+name2]()

# true if 2 angles, line segments, or areas 
# satisfy the relationship name1=fraction*name2
def set_fraction(name1, name2, fraction): 
    initialize()
    # if name1 in globals()[name2].fraction: # and fraction in globals()[name2].fraction[name1]:
    #     return
    if 'fraction' in output:
        if name1 in globals()[name2].fraction: # and fraction in globals()[name2].fraction[name1]:
            return
        output['fraction'].append([name1, name2, fraction])
    else:
        output['fraction'] = [[name1, name2, fraction]]
    x = globals()[name1].fraction
    x[name2] = fraction
    y = globals()[name2].fraction
    y[name1] = 1/fraction

    merge_fraction(name1, name2, fraction)
    merge_fraction(name2, name1, 1/fraction)

    globals()['know_'+name1]()
    globals()['know_'+name2]()

# true if 2 angles, line segments, or areas 
# satisfy relationship name1+name2=sum
def set_sum_value(name1, name2, sum_val):
    initialize()
    # if name1 in globals()[name2].sum_value and sum_val in globals()[name2].sum_value[name1]:
    #     return
    if name1 == name2:
        return
    if 'sum_value' in output:
        if name1 in globals()[name2].sum_value and sum_val in globals()[name2].sum_value[name1]:
            return
        output['sum_value'].append([name1, name2, sum_val])
    else:
        output['sum_value'] = [[name1, name2, sum_val]]

    x = globals()[name1].sum_value
    if name2 in x and sum_val not in x[name2]:
        x[name2].append(sum_val)
    else:
        x[name2] = [sum_val]
    y = globals()[name2].sum_value
    if name1 in y and sum_val not in y[name1]:
        y[name1].append(sum_val)
    else:
        y[name1] = [sum_val]

    globals()['know_'+name1]()
    globals()['know_'+name2]()
    # split sides are equal to full side

# true if 2 shapes similar
# similar = corresponsing sides are proportional
def set_similar(name1, name2):
    # if name1 in globals()[name2].similar:
    #     return
    if 'similar' in output:
        if name1 in globals()[name2].similar:
            return
        output['similar'].append([name1, name2])
    else:
        output['similar'] = [[name1, name2]]
    
    x = globals()[name1].similar
    x.append(name2)
    y = globals()[name2].similar
    y.append(name1)

    globals()['know_'+name1]()
    globals()['know_'+name2]()
    # all angles are equal

# true if 3 shapes are congruent 
# congruent = same shape and size, but rotated, reflected and/or translated
def set_congruent(name1, name2):
    if 'congruent' in output:
        if name1 in globals()[name2].congruent:
            return
        output['congruent'].append([name1, name2])
    else:
        output['congruent'] = [[name1, name2]]
    
    x = globals()[name1].congruent
    x.append(name2)
    y = globals()[name2].congruent
    y.append(name1)

    globals()['know_'+name1]()
    globals()['know_'+name2]()

predicates = {
    'set_parallel': set_parallel,
    'set_perpendicular': set_perpendicular,
    'set_equal': set_equal,
    'set_fraction': set_fraction,
    'set_sum_value': set_sum_value,
    'set_similar': set_similar,
    'set_congruent': set_congruent
}

def check_congruency(a1, b1, c1, a2, b2, c2, sa1, sb1, sc1, sa2, sb2, sc2, ar1, ar2):
    if a2 in a1.equal:
        if b2 in b1.equal or c2 in c1.equal:
            if sc2 in sc1.equal or sa2 in sa1.equal or sb2 in sb1.equal:
                set_congruent(ar1, ar2)
                equal(sc1, sc2); equal(sa1, sa2); equal(sb1, sb2)
            else:
                set_similar(ar1, ar2)
            equal(b1, b2); equal(c1, c2)

        if c2 in b1.equal or b2 in c1.equal:
            if sb2 in sc1.equal or sa2 in sa1.equal or sc2 in sb1.equal:
                set_congruent(ar1, ar2)
                equal(sc1, sb2); equal(sa1, sa2); equal(sb1, sc2)
            else:
                set_similar(ar1, ar2)
            equal(b1, c2); equal(c1, b2)

        if sb2 in sb1.equal and sc2 in sc1.equal:
            set_congruent(ar1, ar2)
            equal(b1, b2); equal(c1, c2)
            equal(sc1, sc2); equal(sa1, sa2); equal(sb1, sb2)

        if sc2 in sb1.equal and sb2 in sc1.equal:
            set_congruent(ar1, ar2)
            equal(b1, c2); equal(c1, b2)
            equal(sc1, sb2); equal(sa1, sa2); equal(sb1, sc2)

        if sb2 in sb1.fraction and sc2 in sc1.fraction and sb1.fraction[sb2] == sc1.fraction[sc2]:
            set_similar(ar1, ar2)
            equal(b1, b2); equal(c1, c2)
            set_fraction(sa1.name, sa2, sb1.fraction[sb2])

        if sc2 in sb1.fraction and sb2 in sc1.fraction and sb1.fraction[sc2] == sc1.fraction[sb2]:
            set_similar(ar1, ar2)
            equal(b1, c2); equal(c1, b2)
            set_fraction(sa1.name, sa2, sb1.fraction[sc2])

def check_triangle(a1, b1, c1, a2, b2, c2, sa1, sb1, sc1, sa2, sb2, sc2, ar1, ar2):
    # Congruent: SSS, SAS, ASA, AAS, HL
    # Similar: AA, AAA
    check_congruency(a1, b1, c1, a2, b2, c2, sa1, sb1, sc1, sa2, sb2, sc2, ar1, ar2)
    check_congruency(a1, b1, c1, b2, c2, a2, sa1, sb1, sc1, sb2, sc2, sa2, ar1, ar2)
    check_congruency(a1, b1, c1, c2, a2, b2, sa1, sb1, sc1, sc2, sa2, sb2, ar1, ar2)
    check_congruency(b1, c1, a1, a2, b2, c2, sb1, sc1, sa1, sa2, sb2, sc2, ar1, ar2)
    check_congruency(b1, c1, a1, b2, c2, a2, sb1, sc1, sa1, sb2, sc2, sa2, ar1, ar2)
    check_congruency(b1, c1, a1, c2, a2, b2, sb1, sc1, sa1, sc2, sa2, sb2, ar1, ar2)
    check_congruency(c1, a1, b1, a2, b2, c2, sc1, sa1, sb1, sa2, sb2, sc2, ar1, ar2)
    check_congruency(c1, a1, b1, b2, c2, a2, sc1, sa1, sb1, sb2, sc2, sa2, ar1, ar2)
    check_congruency(c1, a1, b1, c2, a2, b2, sc1, sa1, sb1, sc2, sa2, sb2, ar1, ar2)

def know_ar1():
    return

def know_ar2():
    return

def know_ar3():
    return

def know_ar4():
    return

def check_angles(a):
    for angle in angles:
        if angle.name != a.name and angle.angle == a.angle and a.angle != 0:
            equal(angle, a.name)
        if angle.name != a.name and angle.angle != 0 and a.angle != 0:
            merge_sum_value(a.name, angle.name, a.angle+angle.angle, 0)
    for item in a.sum_value:
        if globals()[item].angle != 0:
            for value in a.sum_value:
                if type(value) == int:
                    a.angle = value - globals()[item].angle
                    globals()['know_'+a.name]()
                    break

def check_right_angle(angle, name1, name2, s1, s2):
    if angle.right_angle:
        set_sum_value(name1, name2, 90)
        set_sum_value(name1, name2, angle.name)
        check_perpendicular(s1, s2, True)

def know_a1():
    check_angles(a1)
    d1_a1(a1, d1, 'b1', sb3, 'sc4')
    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')

def know_b1():
    check_angles(b1)
    check_right_angle(b1, 'a2', 'c3', sa4, 'sc4')

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    
    if b1.right_angle:
        merge_sum_value('a1', 'c1', 90, 0)
        merge_sum_value('a1', 'c1', 'b1', 1)
        merge_sum_value('a2', 'c3', 90, 0)
        merge_sum_value('a2', 'c3', 'b1', 1)
        check_perpendicular(sa4, 'sc4', True)

    if 'c1' in b1.equal:
        equal(sb1, 'sc1')

    if 'c2' in b1.equal:
        set_parallel('sa4', 'sc3')

    if 'a2' in b1.equal:
        equal(sa4, 'sb4')
    if 'c3' in b1.equal:
        equal(sb4, 'sc4')
    
    if 'd1' in b1.equal or 'a1' in b1.equal:
        merge_sum_value('b1', 'd3', 180, 0)
        equal(sa1, 'sb1')
    
    if 'd3' in b1.equal:
        set_parallel('sc4', 'sb3')
        merge_sum_value('b1', 'd1', 180, 0)

    if 'a1' in b1.sum_value and 90 in b1.sum_value['a1'] or 'd1' in b1.sum_value and 90 in b1.sum_value['d1']:
        check = c1.right_angle
        c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
        merge_sum_value('c2', 'a3', 90, 0)
        merge_sum_value('c2', 'a3', 'c1', 1)
        check_perpendicular(sb3, 'sc4', True)

    if 'c1' in b1.sum_value:
        if 90 in b1.sum_value['c1']:
            check = a1.right_angle
            a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
            check_perpendicular(sb3, 'sa4', True)
        equal_angles('c1', b1, a1)

    if 'a2' in b1.sum_value:
        if 90 in b1.sum_value['a2']:
            check = c3.right_angle
            c3.right_angle = True; c3.angle = 90; set_angle(c3, check)
        equal_angles('a2', b1, c3)
    if 'c3' in b1.sum_value:
        if 90 in b1.sum_value['c3']:
            check = a2.right_angle
            a2.right_angle = True; a2.angle = 90; set_angle(a2, check)
        #merge_sum_value('c1', 'c2', 90, 0)
        #merge_sum_value('c1', 'c2', 'a3', 1)
        equal_angles('c3', b1, a2)
    
    if 'd1' in b1.sum_value or 'a1' in b1.sum_value:
        if 'a1' in b1.sum_value:
            i = 'a1'
        else:
            i = 'd1'
        if 90 in b1.sum_value[i]:
            check_perpendicular(sb3, 'sc4', True)
        if 180 in b1.sum_value[i]:
            equal(b1, 'd3')
        if i == 'd1':
            for item in b1.sum_value['d1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('b1', 'a1', item, x)
        else:
            for item in  b1.sum_value['a1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('b1', 'd1', item, x)
        equal_angles(i, b1, c1)

    if 'd3' in b1.sum_value and 180 in b1.sum_value['d3']:
        equal(c3, 'd1')

def c1_c2(known, a1, a1opp, a1adj, b1, a2, b2, sn, sa, sb, s1, s2, a3):
    check_angles(known)
    if known.right_angle:
        merge_sum_value(a1, b1, 90, 0)
        merge_sum_value(a1, b1, known.name, 1)
        merge_sum_value(a2, b2, 90, 0)
        merge_sum_value(a2, b2, known.name, 1)
        check_perpendicular(s1, s2, True)

    if a1 in known.equal or a1opp in known.equal:
        equal(sn, sa)
        merge_sum_value(known.name, a1adj, 180, 0)
    
    if b1 in known.equal:
        equal(sn, sb)

    if a1 in known.sum_value and 90 in known.sum_value[a1]:
        x = globals()[b1]
        check = x.right_angle
        x.right_angle = True; x.angle = 90; set_angle(x, check)

    if b1 in known.sum_value and 90 in known.sum_value[b1]:
        x = globals()[a1]
        check = x.right_angle
        x.right_angle = True; x.angle = 90; set_angle(x, check)

    if a2 in known.sum_value and 90 in known.sum_value[a2]:
        x = globals()[b2]
        check = x.right_angle
        x.right_angle = True; x.angle = 90; set_angle(x, check)

    if b2 in known.sum_value and 90 in known.sum_value[b2]:
        x = globals()[a2]
        check = x.right_angle
        x.right_angle = True; x.angle = 90; set_angle(x, check)

    if a3 in known.equal:
        set_parallel('sa3', 'sc4')

def equal_angles(a, b, c):
    for item in b.sum_value[a]:
        if type(item) == int and c.angle == 0:
            c.angle = 180 - item
            globals()['know_'+c.name]()
            if b.angle != 0:
                merge_sum_value(b.name, c.name, b.angle+c.angle, 0)
            if globals()[a].angle != 0:
                merge_sum_value(globals()[a].name, c.name, globals()[a].angle+c.angle, 0)

def know_c1():
    c1_c2(c1, 'a1', 'd1', 'd3', 'b1', 'a3', 'c2', sc1, 'sa1', 'sb1', sb3, 'sc4', 'c4')

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    
    if 'a2' in c1.equal:
        set_parallel('sb3', 'sb4')
        equal(a3, 'd2'); equal(a1, 'c3')

    if 'a1' in c1.sum_value or 'd1' in c1.sum_value:
        if 'a1' in c1.sum_value:
            i = 'a1'
        else:
            i = 'd1'
        equal_angles(i, c1, b1)
    if 'b1' in c1.sum_value:
        equal_angles('b1', c1, a1)

def know_a2():
    check_angles(a2)
    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    check_right_angle(a2, 'b1', 'c3', sb4, 'sc4')

    if a2.right_angle:
        merge_sum_value('b2', 'c2', 90, 0)
        merge_sum_value('b2', 'c2', 'a2', 1)
        merge_sum_value('b1', 'c3', 90, 0)
        merge_sum_value('b1', 'c3', 'a2', 1)
        check_perpendicular(sb4, 'sc4', True)

    if 'b1' in a2.equal:
        equal(sa4, 'sb4')
    if 'c3' in a2.equal:
        equal(sa4, 'sc4')

    if 'c2' in a2.equal:
        equal(sa2, 'sc2')
  
    if 'c1' in a2.equal:
        set_parallel('sb3', 'sb4')
    
    if 'd2' in a2.equal or 'b2' in a2.equal:
        merge_sum_value('a2', 'd4', 180, 0)
        equal(sa2, 'sb2')
    
    if 'd4' in a2.equal:
        set_parallel('sc4', 'sc3')
        merge_sum_value('a2', 'b2', 180, 0)
    
    if 'b2' in a2.sum_value and 90 in a2.sum_value['b2'] or 'd2' in a2.sum_value and 90 in a2.sum_value['d2']:
        check = c2.right_angle
        c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
        merge_sum_value('c1', 'a3', 90, 0)
        merge_sum_value('c1', 'a3', 'c2', 1)
        check_perpendicular(sc3, 'sc4', True)

    if 'c2' in a2.sum_value:
        if 90 in a2.sum_value['c2']:
            check = b2.right_angle
            b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
            check_perpendicular(sc3, 'sb4', True)
        equal_angles('c2', a2, b2)

    if 'b1' in a2.sum_value:
        if 90 in a2.sum_value['b1']:
            check = c3.right_angle
            c3.right_angle = True; c3.angle = 90; set_angle(c3, check)
        equal_angles('b1', a2, c3)
    if 'c3' in a2.sum_value:
        if 90 in a2.sum_value['c3']:
            check = b1.right_angle
            b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
            merge_sum_value('a1', 'c1', 90, 0)
            merge_sum_value('a1', 'c1', 'b1', 1)
        equal_angles('c3', a2, b1)

    if 'd2' in a2.sum_value or 'b2' in a2.sum_value:
        if 'd2' in a2.sum_value:
            i = 'd2'
        else:
            i = 'b2'
        if 90 in a2.sum_value[i]:
            check_perpendicular(sc3, 'sc4', True)
        if 180 in a2.sum_value[i]:
            equal(a2, 'd4')
        if i == 'd2':
            for item in  a2.sum_value['d2']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('a2', 'b2', item, x)
        else:
            for item in  a2.sum_value['b2']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('a2', 'd2', item, x)
        equal_angles(i, a2, c2)

    if 'd4' in a2.sum_value and 180 in a2.sum_value['d4']:
        equal(a2, 'd2')

def know_b2():
    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    d2_b2(b2, d2, 'a2', sc3, 'sc4')

def know_c2():
    c1_c2(c2, 'b2', 'd2', 'd4', 'a2', 'a3', 'c1', sc2, 'sb2', 'sa2', sc3, 'sc4', 'b4')

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    if 'b1' in c2.equal:
        set_parallel('sc3', 'sa4')
        equal(a3, 'd1'); equal(b2, 'c3')

    if 'b2' in c2.sum_value or 'd2' in b2.sum_value:
        if 'b2' in c2.sum_value:
            i = 'b2'
        else:
            i = 'd2'
        equal_angles(i, c2, a2)

def know_a3():
    check_angles(a3)
    check_right_angle(a3, 'b4', 'c4', sb3, 'sc3')

    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')
    
    if a3.angle > 0:
        merge_sum_value('c1', 'c2', 180-a3.angle, 0)

    if a3.right_angle:
        merge_sum_value('c1', 'c2', 90, 0)
        merge_sum_value('c1', 'c2', 'a3', 1)
        check_perpendicular(sb3,'sc3', True)

    if 'c4' in a3.equal:
        equal(sa3, 'sc3')
    if 'b4' in a3.equal:
        equal(sa3, 'sb3')
    # if 'c2' in a1.equal:
    
    if 'd1' in a3.equal or 'a1' in a3.equal:
        set_parallel('sc3', 'sa4')
        merge_sum_value('a3', 'd3', 180, 0)
    
    if 'd3' in a3.equal or 'b2' in a3.equal:
        set_parallel('sb3', 'sb4')
        merge_sum_value('a3', 'd4', 180, 0)
    
    if 'd3' in a3.equal:
        merge_sum_value('a3', 'd1', 180, 0)

    if 'd4' in a3.equal:
        merge_sum_value('a3', 'd2', 180, 0)
    
    if 'b4' in a3.sum_value:
        if 90 in a3.sum_value['b4']:
            check = c4.right_angle
            c4.right_angle = True; c4.angle = 90; set_angle(c4, check)
        equal_angles('b4', a3, c4)
    if 'c4' in a3.sum_value:
        if 90 in a3.sum_value['c4']:
            check = b4.right_angle
            b4.right_angle = True; b4.angle = 90; set_angle(b4, check)
        equal_angles('c4', a3, b4)
    if 'c3' in a3.sum_value:
        for item in a3.sum_value['c3']:
            if type(item) == int:
                merge_sum_value('d3', 'd4', 360-item, 0)
                break
    
    if 'd3' in a3.sum_value:
        if 90 in a3.sum_value['d3']:
            check_perpendicular(sa4, 'sc3', True)
    #         # check_perpendicular(sa4, 'sc1', 'sb3', 'sd4'], True)
    #         # check_perpendicular(sa5, 'sc1', 'sb3', 'sd4'], True)
        if 180 in a3.sum_value['d3']:
            equal(a3, 'd1')
        for item in a3.sum_value['d3']:
            if type(item) == int:
                merge_sum_value('c3', 'd4', 360-item, 0)
                break
    
    if 'd4' in a3.sum_value:
        if 90 in a3.sum_value['d4']:
            check_perpendicular(sb3, 'sb4', True)
    #         # check_perpendicular(sa3, ['sb2', 'sb4', 'sb5'], True)
    #         # check_perpendicular(sc4, ['sb2', 'sb4', 'sb5'], True)
        if 180 in a3.sum_value['d4']:
            equal(a3, 'd2')
        for item in a3.sum_value['d4']:
            if type(item) == int:
                merge_sum_value('c3', 'd3', 360-item, 0)
                break

    if 'c1' in a3.sum_value:
        if 90 in a3.sum_value['c1']:
            check = c2.right_angle
            c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
            check_perpendicular(sc3, 'sc4', True)
        for item in a3.sum_value['c1']:
            if type(item) == int:
                c2.angle = 180 - item
                break
    
    if 'c2' in a3.sum_value:
        if 90 in a3.sum_value['c2']:
            check = c1.right_angle
            c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
            check_perpendicular(sb3, 'sc4', True)
        for item in a3.sum_value['c2']:
            if type(item) == int:
                c1.angle = 180 - item
                break

    if 'd1' in a3.sum_value and 180 in a3.sum_value['d1'] or 'a1' in a3.sum_value and 180 in a3.sum_value['a1']:
        equal(a3, 'd3')

    if 'd2' in a3.sum_value and 180 in a3.sum_value['d2'] or 'b2' in a3.sum_value and 180 in a3.sum_value['b2']:
        equal(a3, 'd4')

def know_c3():
    check_angles(c3)
    check_right_angle(c3, 'a2', 'b1', sa4, 'sb4')

    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    
    if 'a2' in c3.equal:
        equal(sa4, 'sc4')
    if 'b1' in c3.equal:
        equal(sb4, 'sc4')
    
    if 'd1' in c3.equal or 'a1' in c3.equal:
        set_parallel('sb3', 'sb4')
        merge_sum_value('c3', 'd3', 180, 0)
    
    if 'd2' in c3.equal or 'b2' in c3.equal:
        set_parallel('sa4', 'sc3')
        merge_sum_value('c3', 'd4', 180, 0)
    
    if 'd3' in c3.equal:
        merge_sum_value('c3', 'd1', 180, 0)

    if 'd4' in c3.equal:
        merge_sum_value('c3', 'd2', 180, 0)
    
    if 'a2' in c3.sum_value:
        if 90 in c3.sum_value['a2']:
            check = b1.right_angle
            b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
            merge_sum_value('a1', 'c1', 90, 0)
            merge_sum_value('a1', 'c1', 'b1', 1)
        equal_angles('a2', c3, b1)
    if 'b1' in c3.sum_value:
        if 90 in c3.sum_value['b1']:
            check = a2.right_angle
            a2.right_angle = True; a2.angle = 90; set_angle(a2, check)
            merge_sum_value('b2', 'c2', 90, 0)
            merge_sum_value('b2', 'c2', 'a2', 1)
        equal_angles('b1', c3, a2)
    if 'a3' in c3.sum_value:
        for item in c3.sum_value['a3']:
            if type(item) == int:
                merge_sum_value('d3', 'd4', 360-item, 0)
                break
    
    if 'd3' in c3.sum_value:
        if 90 in c3.sum_value['d3']:
            check_perpendicular(sb3, 'sb4', True)
        if 180 in c3.sum_value['d3']:
            equal(c3, 'd1')
        for item in c3.sum_value['d3']:
            if type(item) == int:
                merge_sum_value('a3', 'd4', 360-item, 0)
                break
    
    if 'd4' in c3.sum_value:
        if 90 in c3.sum_value['d4']:
            check_perpendicular(sc3, 'sa4', True)
        if 180 in c3.sum_value['d4']:
            equal(c3, 'd2')
        for item in c3.sum_value['d4']:
            if type(item) == int:
                merge_sum_value('a3', 'd3', 360-item, 0)
                break

    if 'd1' in c3.sum_value and 180 in c3.sum_value['d1'] or 'a1' in c3.sum_value and 180 in c3.sum_value['a1']:
        equal(c3, 'd3')

    if 'd2' in c3.sum_value and 180 in c3.sum_value['d2'] or 'b2' in c3.sum_value and 180 in c3.sum_value['b2']:
        equal(c3, 'd4')

def know_b4():
    check_angles(b4)
    check_right_angle(b4, 'a3', 'c4', sa3, 'sc3')

    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    if 'a3' in b4.equal:
        equal(sa3, 'sb3')
    if 'c4' in b4.equal:
        equal(sb3, 'sc3')
    
    if 'c2' in b4.equal:
        set_parallel('sa3', 'sc4')

    if 'd2' in b4.equal or 'b2' in b4.equal:
        merge_sum_value('b4', 'd4', 180, 0)
    
    if 'd4' in b4.equal:
        set_parallel('sa3', 'sb4')
        merge_sum_value('b4', 'd2', 180, 0)
    
    if 'a3' in b4.sum_value:
        if 90 in b4.sum_value['a3']:
            check = c4.right_angle
            c4.right_angle = True; c4.angle = 90; set_angle(c4, check)
        equal_angles('a3', b4, c4)
    if 'c4' in b4.sum_value:
        if 90 in b4.sum_value['c4']:
            check = a3.right_angle
            a3.right_angle = True; a3.angle = 90; set_angle(a3, check)
            merge_sum_value('c1', 'c2', 90, 0)
            merge_sum_value('c1', 'c2', 'a3', 1)
        equal_angles('c4', b4, a3)
    if 'd2' in b4.sum_value or 'b2' in b4.sum_value:
        if 'd2' in b4.sum_value:
            i = 'd2'
        else:
            i = 'b2'
        if 90 in b4.sum_value[i]:
            check_perpendicular(sa3, 'sb4', True)
            merge_sum_value('b4', i, 90, 0)
        if 180 in b4.sum_value[i]:
            equal(b4, 'd4')
        if i == 'd2':
            for item in b4.sum_value['d2']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('b4', 'b2', item, x)
        else:
            for item in  b4.sum_value['b2']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('b4', 'd2', item, x)

    if 'd4' in b4.sum_value and 180 in b4.sum_value['d4']:
        equal(b4, 'd2')

def know_c4():
    check_angles(c4)
    check_right_angle(c4, 'a3', 'b4', sa3, 'sb3')

    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    if 'a3' in c4.equal:
        equal(sa3, 'sc3')
    if 'b4' in c4.equal:
        equal(sb4, 'sc4')
    
    if 'd1' in c4.equal or 'a1' in c4.equal:
        merge_sum_value('c4', 'd3', 180, 0)
    
    if 'd2' in c4.equal:
        set_parallel('sa3', 'sa4')
        merge_sum_value('c4', 'd1', 180, 0)
    
    if 'c1' in c4.equal:
        set_parallel('sa3', 'sc4')

    if 'a3' in c4.sum_value:
        if 90 in c4.sum_value['a3']:
            check = b4.right_angle
            b4.right_angle = True; b4.angle = 90; set_angle(b4, check)
        equal_angles('a3', c4, b4)
    if 'b4' in c4.sum_value:
        if 90 in c4.sum_value['b4']:
            check = a3.right_angle
            a3.right_angle = True; a3.angle = 90; set_angle(a3, check)
            merge_sum_value('c1', 'c2', 90, 0)
            merge_sum_value('c1', 'c2', 'a3', 1)
        equal_angles('b4', c4, a3)
        
    if 'd1' in c4.sum_value or 'a1' in c4.sum_value:
        if 'a1' in c4.sum_value:
            i = 'a1'
        else:
            i = 'd1'
        if 90 in c4.sum_value[i]:
            check_perpendicular(sa3, 'sa4', True)
        if 180 in c4.sum_value[i]:
            equal(c4, 'd3')
        if i == 'd1':
            for item in c4.sum_value['d1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('c4', 'a1', item, x)
        else:
            for item in c4.sum_value['a1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('c4', 'd1', item, x)

    if 'd3' in c4.sum_value and 180 in c4.sum_value['d3']:
        equal(c4, 'd1')

def know_d1():
    d1_a1(d1, a1, 'c4', sa3, 'sa4')

    check_triangle(d1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(d1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(d1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    
def know_d2():
    d2_b2(d2, b2, 'b4', sa3, 'sb4')

    check_triangle(a1, b1, c1, 'a2', 'd2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a2, b1, c3, 'a2', 'd2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, d2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

def know_d3():
    check_angles(d3)
    check_d_angles(d1, d3, a1, sb3, 'sa4')

    if d3.right_angle:
        merge_sum_value('c1', 'b1', 90, 0)
        merge_sum_value('c1', 'b1', 'a1', 1)

    if 'd1' in d3.equal or 'a1' in d3.equal:
        check = d1.right_angle
        d1.right_angle = True; d1.angle = 90; set_angle(d1, check)
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
        check = d3.right_angle
        d3.right_angle = True; d3.angle = 90; set_angle(d3, check)
        check_perpendicular(sb1, 'sa2', True)
        merge_sum_value('c1', 'b1', 90, 0)
        merge_sum_value('c1', 'b1', 'a1', 1)

    if 'd4' in d3.equal:
        equal(d1, 'd2')

    if 'c4' in d3.equal:
        set_parallel('sa3', 'sa4')
        merge_sum_value('c4', 'd1', 180, 0)

    if 'c3' in d3.sum_value:
        if 90 in d3.sum_value['c3']:
            check_perpendicular(sb3, 'sb4', True)
        if 180 in d3.sum_value['c3']:
            equal(c3, 'd1')
        for item in d3.sum_value['c3']:
                if type(item) == int: 
                    merge_sum_value('a3', 'd4', 360-item, 0)

    if 'a3' in d3.sum_value:
        if 90 in d3.sum_value['a3']:
            check_perpendicular(sa4, 'sc3', True)
        if 180 in d3.sum_value['a3']:
            equal(a3, 'd1')
        for item in  d3.sum_value['a3']:
                if type(item) == int: 
                    merge_sum_value('c3', 'd4', 360-item, 0)
    
    if 'd4' in d3.sum_value:
        for item in  d3.sum_value['d4']:
                if type(item) == int: 
                    merge_sum_value('c3', 'a3', 360-item, 0)

def know_d4():
    check_angles(d4)
    if d4.right_angle:
        merge_sum_value('a2', 'c2', 90, 0)
        merge_sum_value('a2', 'c2', 'b2', 1)
    
    check_d_angles(d2, d4, b2, sc3, 'sb4')

    if 'd2' in d4.equal or 'b2' in d4.equal:
        check = d4.right_angle
        d4.right_angle = True; d4.angle = 90; set_angle(d4, check)
        check = d2.right_angle
        d2.right_angle = True; d2.angle = 90; set_angle(d2, check)
        check = b2.right_angle
        b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
        check_perpendicular(sc3, 'sb4', True)
        merge_sum_value('a2', 'c2', 90, 0)
        merge_sum_value('a2', 'c2', 'b2', 1)

    if 'd3' in d4.equal:
        equal(d1, 'd2')

    if 'b4' in d4.equal:
        set_parallel('sa3', 'sb4')
        merge_sum_value('b4', 'd2', 180, 0)

    if 'c3' in d4.sum_value:
        if 90 in d4.sum_value['c3']:
            check_perpendicular(sc3, 'sa4', True)
        if 180 in d4.sum_value['c3']:
            equal(c3, 'd2')
        for item in  d4.sum_value['c3']:
                if type(item) == int: 
                    merge_sum_value('a3', 'd3', 360-item, 0)

    if 'a3' in d4.sum_value:
        if 90 in d4.sum_value['a3']:
            check_perpendicular(sb4, 'sb3', True)
        if 180 in d4.sum_value['a3']:
            equal(a3, 'd2')
        for item in  d4.sum_value['a3']:
                if type(item) == int: 
                    merge_sum_value('c3', 'd3', 360-item, 0)
    
    if 'd3' in d4.sum_value:
        for item in  d4.sum_value['d3']:
                if type(item) == str: 
                    merge_sum_value('c3', 'a3', 360-item, 0)

def d1_a1(known, a, b, s1, s2):
    check_angles(known)
    check_d_angles(d1, d3, a1, sb3, 'sa4')

    if known.right_angle:
        merge_sum_value('b1', 'c1', 90, 0)
        merge_sum_value('b1', 'c1', 'a1', 1)

    if 'd3' in known.equal:
        check = known.right_angle
        known.right_angle = True; known.angle = 90; set_angle(known, check)
        check_d_angles(d1, d3, a1, sb3, 'sa4')
    
    if 'a3' in known.equal:
        set_parallel('sa4', 'sc3')
        equal(a3, a.name)
        equal(b1, 'c2')
        merge_sum_value('a3', 'd3', 180, 0)
    
    if 'c3' in known.equal:
        set_parallel('sb3', 'sb4')
        equal(c3, a.name)
        equal(c1, 'a2')
        merge_sum_value('c3', 'd3', 180, 0)

    if 'd2' in known.equal or 'b2' in known.equal:
        equal(a, 'd2')
        equal(d3, 'd4')
        merge_sum_value('d1', 'd4', 180, 0)

    if 'd4' in known.equal:
        equal(d3, 'd2')
        merge_sum_value('d3', 'd4', 180, 0)
        merge_sum_value(known.name, 'd2', 180, 0)

    if b in known.sum_value and 90 in known.sum_value[b] or b in a.sum_value and 90 in a.sum_value[b]:
        check_perpendicular(s1, s2, True)
        check = c1.right_angle
        c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
        merge_sum_value('a1', 'b1', 90, 0)
        merge_sum_value('a1', 'b1', 'c1', 1)
    
    if 'c1' in known.sum_value:
        if 90 in known.sum_value['c1']:
            check = b1.right_angle
            b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
            check_perpendicular(sa4, 'sc4', True)
            merge_sum_value('a2', 'c3', 90, 0)
            merge_sum_value('a2', 'c3', 'b1', 1)
        equal_angles('c1', known, b1)

    if 'b1' in known.sum_value:
        equal_angles('b1', known, c1)

    if a.name in known.sum_value and 180 in known.sum_value[a.name]:
        check = d1.right_angle
        d1.right_angle = True; d1.angle = 90; set_angle(d1, check)
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
        check = d3.right_angle
        d3.right_angle = True; d3.angle = 90; set_angle(d3, check)
        merge_sum_value('b1', 'c1', 90, 0)
        merge_sum_value('b1', 'c1', 'a1', 1)

    if 'd2' in known.sum_value or 'b2' in known.sum_value:
        if 'd2' in known.sum_value:
            for item in known.sum_value['d2']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value(a.name, 'b2', item, x)
        else:
            for item in  known.sum_value['b2']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value(a.name, 'd2', item, x)

    if 'd4' in known.sum_value and 180 in known.sum_value['d4']:
        equal(known, 'd2'); equal(d3, 'd4') #; equal(a1, 'c2')
        #set_parallel('sb1', 'sb2'); set_parallel('sa2', 'sc1')
        merge_sum_value('a1', 'd4', 180, 0)
        merge_sum_value('d3', 'd2', 180, 0)

def d2_b2(known, a, b, s1, s2):
    check_angles(known)
    check_d_angles(d2, d4, b2, sc3, 'sb4')

    if known.right_angle:
        merge_sum_value('a2', 'c2', 90, 0)
        merge_sum_value('a2', 'c2', 'b2', 1)

    if 'd4' in known.equal:
        check = known.right_angle
        known.right_angle = True; known.angle = 90; set_angle(known, check)
        check_d_angles(d2, d4, b2, sc3, 'sb4')
    
    if 'a3' in known.equal:
        set_parallel('sb3', 'sb4')
        equal(a3, a.name)
        equal(c1, 'a2')
        merge_sum_value('a3', 'd4', 180, 0)
    
    if 'c3' in known.equal:
        set_parallel('sa4', 'sc3')
        equal(c3, a.name)
        equal(b1, 'c2')
        merge_sum_value('c3', 'd4', 180, 0)

    if 'd1' in known.equal or 'a1' in known.equal:
        equal(a, 'd1')
        equal(d3, 'd4')
        merge_sum_value('d2', 'd3', 180, 0)

    if 'd3' in known.equal:
        equal(d4, 'd1')
        merge_sum_value('d3', 'd4', 180, 0)
        merge_sum_value(known.name, 'd1', 180, 0)

    if b in known.sum_value and 90 in known.sum_value[b] or b in a.sum_value and 90 in a.sum_value[b]:
        check_perpendicular(s1, s2, True)
        check = c2.right_angle
        c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
        merge_sum_value('a2', 'b2', 90, 0)
        merge_sum_value('a2', 'b2', 'c2', 1)

    if 'c2' in known.sum_value:
        if 90 in known.sum_value['c2']:
            check = a2.right_angle
            a2.right_angle = True; a2.angle = 90; set_angle(a2, check)
            check_perpendicular(sb4, 'sc4', True)
            merge_sum_value('b1', 'c3', 90, 0)
            merge_sum_value('b1', 'c3', 'a2', 1)
        equal_angles('c2', known, a2)
    
    if 'a2' in known.sum_value:
        equal_angles('a2', known, c2)
    
    if a.name in known.sum_value and 180 in known.sum_value[a.name]:
        check = d4.right_angle
        d4.right_angle = True; d4.angle = 90; set_angle(d4, check)
        check = d2.right_angle
        d2.right_angle = True; d2.angle = 90; set_angle(d2, check)
        check = b2.right_angle
        b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
        merge_sum_value('a2', 'c2', 90, 0)
        merge_sum_value('a2', 'c2', 'b2', 0)

    if 'd1' in known.sum_value or 'a1' in known.sum_value:
        if 'd1' in known.sum_value:
            for item in known.sum_value['d1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value(a.name, 'a1', item, x)
        else:
            for item in  known.sum_value['a1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value(a.name, 'd1', item, x)

    if 'd3' in known.sum_value and 180 in known.sum_value['d3']:
        equal(known, 'd1'); equal(d3, 'd4') #; equal(a1, 'c2')
        #set_parallel('sb1', 'sb2'); set_parallel('sa2', 'sc1')
        merge_sum_value('d1', 'd4', 180, 0)
        merge_sum_value('d3', 'd2', 180, 0)

def check_d_angles(known, adj, opp, n1, n2):
    if known.right_angle:
        check = adj.right_angle
        adj.right_angle = True; adj.angle = 90; set_angle(adj, check)
        check = opp.right_angle
        opp.right_angle = True; opp.angle = 90; set_angle(opp, check)
        equal(known, adj.name)
        merge_sum_value(known.name, opp.name, 180, 0)
        check_perpendicular(n1, n2, True)

def check_parallel(known, names):
    parallel = False
    if not parallel:
        for name in names:
            if name in known.parallel:
                parallel = True
                break
    if parallel:
        for name in names:
            if name and name not in known.parallel:
                set_parallel(known.name, name)
    return parallel

def equal(a, n2):
    if a and n2 not in a.equal:    
        set_equal(a.name, n2)

def check_perpendicular(a, name, perpendicular):
    edges = [['sb3', 'sa5', 'sb1'], 
        ['sc3', 'sb5', 'sa2'], 
        ['sa4', 'sa6', 'sc1'], 
        ['sb4', 'sb6', 'sc2'],
        ['sc4', 'sa1', 'sb2']]
    
    x = [a.name]
    names = [name]
    for i in edges:
        if a.name in i:
            x = i
        if name in i:
            names = i

    if not perpendicular:
        for name in names:
            if name in a.perpendicular:
                perpendicular = True
                break

    if perpendicular:
        for a in x:
            for name in names:
                if name and name not in globals()[a].perpendicular:
                    set_perpendicular(a, name)
    return perpendicular

def merge_parallel(a, b):
    for item in a.parallel:
        if item != b.name:
            set_parallel(b.name, item)

    for item in b.parallel:
        if item != a.name:
            set_parallel(a.name, item)

def merge_equals(a, b):
    for item in a.equal:
        if item != b.name:
            equal(b, item)

    for item in b.equal:
        if item != a.name:
            equal(a, item)

def merge_sums(a, b):
    for key in list(a.sum_value):
        for value in a.sum_value[key]:
            if key not in b.sum_value:
                set_sum_value(b.name, key, value)
            else:
                if value not in b.sum_value[key]:
                    set_sum_value(b.name, key, value)

    for key in list(b.sum_value):
        for value in b.sum_value[key]:
            if key not in a.sum_value:
                set_sum_value(a.name, key, value)
            else:
                if value not in a.sum_value[key]:
                    set_sum_value(a.name, key, value)

def merge_sum_value(a, b, c, merge):
    if merge == 0:
        #set_sum_value(a, b, c)
        for i in [a]+globals()[a].equal:
            for j in [b]+globals()[b].equal: 
                if i != j:
                    set_sum_value(i, j, c)  
    if merge == 1:
        if type(c) != str:
            return 
        set_sum_value(a, b, c)
        for item in globals()[c].equal:
            if a != b and a != item and b != item:
                set_sum_value(a, b, item)

def merge_fracs(a, b):
    for key in list(a.fraction):
        if key not in b.fraction:
            if a.fraction[key] > 1:
                set_fraction(key, b.name, a.fraction[key])
        
    for key in list(b.fraction):
        if key not in a.fraction:
            if b.fraction[key] > 1:
                set_fraction(a.name, key, b.fraction[key])
        
def merge_fraction(a, b, c):
    for i in [a]+globals()[a].equal:
        for j in [b]+globals()[b].equal: 
            if i != j:
                set_fraction(i, j, c)  

def set_angle(a, check):
    if a.right_angle:
        for angle in a.equal:
            if not globals()[angle].right_angle:
                globals()[angle].right_angle = True; globals()[angle].angle = 90
                globals()['know_'+angle]()
    else:
        for angle in a.equal:
            if globals()[angle].angle != a.angle:
                globals()[angle].angle = a.angle
                globals()['know_'+angle]()
    
    if not check:
        globals()['know_'+a.name]()

def know_sa3():
    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    if check_parallel(sa3, ['sa4', 'sa6', 'sc1']):
        equal(c4, 'd3')
    
    if check_parallel(sa3, ['sb4', 'sb6', 'sc2']):
        equal(b4, 'd4')

    if check_parallel(sa3, ['sc4', 'sa1', 'sb2']):
        equal(c1, 'c4'); equal(b4, 'c2')
    
    if check_perpendicular(sa3, 'sb3', False):
        check = c4.right_angle
        c4.right_angle = True; c4.angle = 90; set_angle(c4, check)
        merge_sum_value('a3', 'b4', 90, 0)
        merge_sum_value('a3', 'b4', 'c4', 1)
        # know_c4()
    
    if check_perpendicular(sa3, 'sc3', False):#['sc1', 'sb3', 'sd4'], False):
        check = b4.right_angle
        b4.right_angle = True; b4.angle = 90; set_angle(b4, check)
        merge_sum_value('a3', 'c4', 90, 0)
        merge_sum_value('a3', 'c4', 'b4', 1)
        # know_b4()
    
    if check_perpendicular(sa3, 'sa4', False):
        merge_sum_value('c4', 'd1', 90, 0)
        merge_sum_value('c4', 'a1', 90, 0)

    if check_perpendicular(sa3, 'sb4', False):
        merge_sum_value('b4', 'd2', 90, 0)
        merge_sum_value('b4', 'b2', 90, 0)

    if 'sb3' in sa3.equal:
        equal(a3, 'b4')
        merge_sum_value('sa5', 'sb1', 'sa3', 1)
    
    if 'sc3' in sa3.equal:
        equal(a3, 'c4')
        merge_sum_value('sb5', 'sa2', 'sa3', 1)

def know_sb3():
    sb3_sa5_sb1(sb3, sa5, sb1)

    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    for i in ['sa4', 'sb4', 'sc4']:
        if i in sb3.equal:
            merge_sum_value('sa5', 'sb1', i, 1)

    if 'sa3' in sb3.equal:
        equal(a3, 'b4')
        merge_sum_value('sa5', 'sb1', 'sa3', 1)

    if 'sc3' in sb3.equal:
        equal(b4, 'c4')
        merge_sum_value('sa5', 'sb1', 'sc3', 1)
        merge_sum_value('sb5', 'sa2', 'sb3', 1)

def know_sa5():
    sb3_sa5_sb1(sa5, sb3, sb1)

    if 'sb1' in sa5.fraction:
        if sa5.fraction['sb1'] > 1:
            set_fraction('sb3', 'sb1', sa5.fraction['sb1']+1)

def know_sb1():
    sb3_sa5_sb1(sb1, sb3, sa5)

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    
    if 'sc1' in sb1.equal:
        equal(b1, 'c1')
    if 'sa1' in sb1.equal:
        equal(a1, 'b1')

    if 'sa5' in sb1.fraction:
        if sb1.fraction['sa5'] > 1:
            set_fraction('sb3', 'sa5', sb1.fraction['sa5']+1)

def know_sc3():
    sc3_sb5_sa2(sc3, sb5, sa2)

    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')
    
    for i in ['sa4', 'sb4', 'sc4']:
        if i in sc3.equal:
            merge_sum_value('sb5', 'sa2', i, 1)

    if 'sa3' in sc3.equal:
        equal(a3, 'c4')
        merge_sum_value('sb5', 'sa2', 'sa3', 1)
    
    if 'sb3' in sc3.equal:
        equal(b4, 'c4')
        merge_sum_value('sb5', 'sa2', 'sb3', 1)
        merge_sum_value('sa5', 'sb1', 'sc3', 1)

def know_sb5():
    sc3_sb5_sa2(sb5, sc3, sa2)

    if 'sa2' in sb5.fraction:
        if sb5.fraction['sa2'] > 1:
            set_fraction('sc3', 'sa2', sb5.fraction['sa2']+1)

def know_sa2():
    sc3_sb5_sa2(sa2, sc3, sb5)

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    if 'sc2' in sa2.equal:
        equal(a2, 'c2')
    if 'sb2' in sa2.equal:
        equal(a2, 'b2')

    if 'sb5' in sa2.fraction:
        if sa2.fraction['sb5'] > 1:
            set_fraction('sc3', 'sb5', sa2.fraction['sb5']+1)

def know_sa4():
    sa4_sa6_sc1(sa4, sa6, sc1)

    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    
    for i in ['sa3', 'sb3', 'sc3']:
        if i in sa4.equal:
            merge_sum_value('sa6', 'sc1', i, 1)

    if 'sb4' in sa4.equal:
        equal(a2, 'b1')
        merge_sum_value('sa6', 'sc1', 'sb4', 1)
        merge_sum_value('sb6', 'sc2', 'sa4', 1)
    
    if 'sc4' in sa4.equal:
        equal(a2, 'c3')
        merge_sum_value('sa6', 'sc1', 'sc4', 1)
        merge_sum_value('sa1', 'sb2', 'sa4', 1)

def know_sa6():
    sa4_sa6_sc1(sa6, sa4, sc1)

    if 'sc1' in sa6.fraction:
        if sa6.fraction['sc1'] > 1:
            set_fraction('sa4', 'sc1', sa6.fraction['sc1']+1)

def know_sc1():
    sa4_sa6_sc1(sc1, sa4, sa6)

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    
    if 'sb1' in sc1.equal:
        equal(b1, 'c1')
    if 'sa1' in sc1.equal:
        equal(a1, 'c1')

    if 'sa6' in sc1.fraction:
        if sc1.fraction['sa6'] > 1:
            set_fraction('sa4', 'sa6', sc1.fraction['sa6']+1)

def know_sb4():
    sb4_sb6_sc2(sb4, sb6, sc2)

    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    
    for i in ['sa3', 'sb3', 'sc3']:
        if i in sb4.equal:
            merge_sum_value('sb6', 'sc2', i, 1)

    if 'sa4' in sb4.equal:
        equal(a2, 'b1')
        merge_sum_value('sb6', 'sc2', 'sa4', 1)
        merge_sum_value('sa6', 'sc1', 'sb4', 1)
    
    if 'sc4' in sb4.equal:
        equal(b1, 'c3')
        merge_sum_value('sb6', 'sc2', 'sc4', 1)
        merge_sum_value('sa1', 'sb2', 'sb4', 1)

def know_sb6():
    sb4_sb6_sc2(sb6, sb4, sc2)

    if 'sc2' in sb6.fraction:
        if sb6.fraction['sc2'] > 1:
            set_fraction('sb4', 'sc2', sb6.fraction['sc2']+1)

def know_sc2():
    sb4_sb6_sc2(sc2, sb4, sb6)

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    if 'sb2' in sc2.equal:
        equal(b2, 'c2')
    if 'sa2' in sc2.equal:
        equal(a2, 'c2')

    if 'sb6' in sc2.fraction:
        if sc2.fraction['sb6'] > 1:
            set_fraction('sb2', 'sb6', sc2.fraction['sb6']+1)

def know_sc4():
    sc4_sa1_sb2(sc4, sa1, sb2)

    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b1, c3, 'a3', 'b4', 'c4', sa4, sb4, sc4, 'sa3', 'sb3', 'sc3', 'ar4', 'ar3')
    
    for i in ['sa3', 'sb3', 'sc3']:
        if i in sc4.equal:
            merge_sum_value('sa1', 'sb2', i, 1)

    if 'sa4' in sc4.equal:
        equal(a2, 'c3')
        merge_sum_value('sa6', 'sc1', 'sc4', 1)
        merge_sum_value('sa1', 'sb2', 'sa4', 1)
    
    if 'sb4' in sc4.equal:
        equal(b1, 'c3')
        merge_sum_value('sb6', 'sc2', 'sc4', 1)
        merge_sum_value('sa1', 'sb2', 'sb4', 1)

def know_sa1():
    sc4_sa1_sb2(sa1, sc4, sb2)

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a1, b1, c1, 'a2', 'b1', 'c3', sa1, sb1, sc1, 'sa4', 'sb4', 'sc4', 'ar1', 'ar4')
    check_triangle(a1, b1, c1, 'a3', 'b4', 'c4', sa1, sb1, sc1, 'sa3', 'sb3', 'sc3', 'ar1', 'ar3')
    
    if 'sc1' in sa1.equal:
        equal(a1, 'c1')
    if 'sb1' in sa1.equal:
        equal(a1, 'b1')

    if 'sb2' in sa1.fraction:
        if sa1.fraction['sb2'] > 1:
            set_fraction('sc4', 'sb2', sa1.fraction['sb2']+1)

def know_sb2():
    sc4_sa1_sb2(sb2, sc4, sa1)

    check_triangle(a1, b1, c1, 'a2', 'b2', 'c2', sa1, sb1, sc1, 'sa2', 'sb2', 'sc2', 'ar1', 'ar2')
    check_triangle(a2, b1, c3, 'a2', 'b2', 'c2', sa4, sb4, sc4, 'sa2', 'sb2', 'sc2', 'ar4', 'ar2')
    check_triangle(a2, b2, c2, 'a3', 'b4', 'c4', sa2, sb2, sc2, 'sa3', 'sb3', 'sc3', 'ar2', 'ar3')

    if 'sc2' in sb2.equal:
        equal(b2, 'c2')
    if 'sa2' in sb2.equal:
        equal(a2, 'b2')

    if 'sa1' in sb2.fraction:
        if sb2.fraction['sa1'] > 1:
            set_fraction('sc4', 'sa1', sb2.fraction['sa1']+1)

def sc4_sa1_sb2(known, a, b):

    if check_parallel(known, ['sa3']):
        equal(c1, 'c4'); equal(b4, 'c2')

    if check_perpendicular(known, 'sb3', False):
        check = c1.right_angle
        c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
        merge_sum_value('b1', 'a1', 90, 0)
        merge_sum_value('b1', 'a1', 'c1', 1)
        merge_sum_value('a3', 'c2', 90, 0)
        merge_sum_value('a3', 'c2', 'c1', 1)
#         #merge_sum_value('a1', 'b1', 'c1', 1)
    
    if check_perpendicular(known, 'sc3', False):
        check = c2.right_angle
        c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
        merge_sum_value('c1', 'a3', 90, 0)
        merge_sum_value('c1', 'a3', 'c2', 1)
        merge_sum_value('a2', 'b2', 90, 0)
        merge_sum_value('a2', 'b2', 'c2', 1)
#         #merge_sum_value('a1', 'c1', 'b1', 1)
    
    if check_perpendicular(known, 'sa4', False):
        check = b1.right_angle
        b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
        merge_sum_value('a2', 'c3', 90, 0)
        merge_sum_value('a2', 'c3', 'b1', 1)
        merge_sum_value('a1', 'c1', 90, 0)
        merge_sum_value('a1', 'c1', 'b1', 1)
#         know_b2()

    if check_perpendicular(known, 'sb4', False):
        check = a2.right_angle
        a2.right_angle = True; a2.angle = 90; set_angle(a2, check)
        merge_sum_value('b1', 'c3', 90, 0)
        merge_sum_value('b1', 'c3', 'a2', 1)
        merge_sum_value('b2', 'c2', 90, 0)
        merge_sum_value('b2', 'c2', 'a2', 1)
#         know_a2()

def sc3_sb5_sa2(known, a, b):
#     if check_parallel(known, ['sc2']):
#         equal(a2, 'd5')

    if check_parallel(known, ['sa4', 'sa6', 'sc1']):
        equal(a3, 'd1'); equal(c3, 'd2'); equal(b1, 'c2')
    
    if check_perpendicular(known, 'sa3', False): 
        check = b4.right_angle
        b4.right_angle = True; b4.angle = 90; set_angle(b4, check)
        merge_sum_value('a3', 'c4', 90, 0)
        merge_sum_value('a3', 'c4', 'b4', 1)
#         #check_perpendicular(a, 'sa3', True)
#         #check_perpendicular(b, 'sa3', True)
#         know_b4()
    
    if check_perpendicular(known, 'sb3', False): 
        check = a3.right_angle
        a3.right_angle = True; a3.angle = 90; set_angle(a3, check)
        merge_sum_value('b4', 'c4', 90, 0)
        merge_sum_value('b4', 'c4', 'a3', 1)
        merge_sum_value('c1', 'c2', 90, 0)
        merge_sum_value('c1', 'c2', 'a3', 1)
        
#         #check_perpendicular(a, 'sb1', True)
#         #check_perpendicular(b, 'sb1', True)
#         know_a1()

    if check_perpendicular(known, 'sb4', False):
        check = d2.right_angle
        d2.right_angle = True; d2.angle = 90; set_angle(d2, check)
        check = d4.right_angle
        d4.right_angle = True; d4.angle = 90; set_angle(d4, check)
        check = b2.right_angle
        b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
        equal(d2, 'd4')
        merge_sum_value('a2', 'c2', 90, 0)
        merge_sum_value('a2', 'c2', 'b2', 1)
#         set_angle(d4)
#         know_d6()
#         #check_perpendicular(a, ['sb2', 'sb4', 'sb5'], True)
#         #check_perpendicular(b, ['sb2', 'sb4', 'sb5'], True)

    if check_perpendicular(known, 'sc4', False):
        merge_sum_value('a2', 'b2', 90, 0)
        check = c2.right_angle
        c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
        merge_sum_value('c1', 'a3', 90, 0)
        merge_sum_value('c1', 'a3', 'c2', 1)  
        merge_sum_value('a2', 'b2', 90, 0)
        merge_sum_value('a2', 'b2', 'c2', 1)     
#         # check_perpendicular(a, ['sc2'], True)
#         # check_perpendicular(b, ['sc2'], True)

def sa4_sa6_sc1(known, a, b):
    if check_parallel(known, ['sa3']):
        equal(c4, 'd3')
    
    if check_parallel(known, ['sc3', 'sb5', 'sa2']):
        equal(a3, 'd1'); equal(c3, 'd2'); equal(b1, 'c2')
    
    if check_perpendicular(known, 'sc4', False):
        check = b1.right_angle
        b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
        merge_sum_value('a2', 'c3', 90, 0)
        merge_sum_value('a2', 'c3', 'b1', 1)
        merge_sum_value('a1', 'c1', 90, 0)
        merge_sum_value('a1', 'c1', 'b1', 1)
#         # check_perpendicular(a, ['sc2'], True)
#         # check_perpendicular(b, ['sc2'], True)
#         know_b2()

    if check_perpendicular(known, 'sb4', False):
        check = c3.right_angle
        c3.right_angle = True; c3.angle = 90; set_angle(c3, check)
        merge_sum_value('a2', 'b1', 90, 0)
        merge_sum_value('a2', 'b1', 'c3', 1)
#         # check_perpendicular(a, ['sb2', 'sb4', 'sb5'], True)
#         # check_perpendicular(b, ['sb2', 'sb4', 'sb5'], True)
#         know_c2()

    if check_perpendicular(known, 'sb3', False):
        check = d1.right_angle
        d1.right_angle = True; d1.angle = 90; set_angle(d1, check)
        check = d3.right_angle
        d3.right_angle = True; d3.angle = 90; set_angle(d3, check)
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
        equal(d1, 'd3')
        merge_sum_value('b1', 'c1', 90, 0)
        merge_sum_value('b1', 'c1', 'a1', 1)
#         set_angle(d1)
#         know_d3()
#         # check_perpendicular(a, ['sb1', 'sa3', 'sc4'], True)
#         # check_perpendicular(a, ['sb1', 'sa3', 'sc4'], True)

    if check_perpendicular(known, 'sa3', False):
        merge_sum_value('c4', 'd1', 90, 0)
#         # check_perpendicular(a, ['sa1'], True)
#         # check_perpendicular(b, ['sa1'], True)

def sb4_sb6_sc2(known, a, b):
# def sb2_sb4_sb5(known, a, b):
    if check_parallel(known, ['sa3']):
        equal(b4, 'd4') 

    if check_parallel(known, ['sb3', 'sa5', 'sb1']):
        equal(a1, 'c3'); equal(a3, 'd2'); equal(c1, 'a2')
    
    if check_perpendicular(known, 'sc4', False):
        check = a2.right_angle
        a2.right_angle = True; a2.angle = 90; set_angle(a2, check)
        merge_sum_value('b1', 'c3', 90, 0)
        merge_sum_value('b1', 'c3', 'a2', 1)
        merge_sum_value('b2', 'c2', 90, 0)
        merge_sum_value('b2', 'c2', 'a2', 1)
#         # check_perpendicular(a, ['sc2'], True)
#         # check_perpendicular(b, ['sc2'], True)
#         know_a2()

    if check_perpendicular(known, 'sa4', False):
        check = c3.right_angle
        c3.right_angle = True; c3.angle = 90; set_angle(c3, check)
        merge_sum_value('a2', 'b1', 90, 0)
        merge_sum_value('a2', 'b1', 'c3', 1)
#         # check_perpendicular(a, ['sa2', 'sa4', 'sa5'], True)
#         # check_perpendicular(a, ['sa2', 'sa4', 'sa5'], True)
#         know_c2()

    if check_perpendicular(known, 'sc3', False):
        check = d2.right_angle
        d2.right_angle = True; d2.angle = 90; set_angle(d2, check)
        check = d4.right_angle
        d4.right_angle = True; d4.angle = 90; set_angle(d4, check)
        check = b2.right_angle
        b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
        equal(d2, 'd4')
        merge_sum_value('a2', 'c2', 90, 0)
        merge_sum_value('a2', 'c2', 'b2', 1)
#         set_angle(d4)
#         know_d6()
#         # check_perpendicular(a, ['sc1', 'sb3', 'sd4'], True)
#         # check_perpendicular(a, ['sc1', 'sb3', 'sd4'], True)

    if check_perpendicular(known, 'sa3', False):
        merge_sum_value('b4', 'd2', 90, 0)
#         # check_perpendicular(a, ['sa1'], True)
#         # check_perpendicular(b, ['sa1'], True)

def sb3_sa5_sb1(known, a, b):
    if check_parallel(known, ['sb4', 'sb6', 'sc2']):
        equal(a3, 'd2'); equal(c3, 'a1'); equal(c1, 'a2')
    
#     if check_parallel(known, ['sc2']):
#         equal(b2, 'd2')
    
    if check_perpendicular(known, 'sa3', False):
        check = c4.right_angle
        c4.right_angle = True; c4.angle = 90; set_angle(c4, check)
        merge_sum_value('a3', 'b4', 90, 0)
        merge_sum_value('a3', 'b4', 'c4', 0)
        # check_perpendicular(a, ['sa3'], True)
        # check_perpendicular(b, ['sa3'], True)
        # know_c4()

    if check_perpendicular(known, 'sc3', False): 
        check = a3.right_angle
        a3.right_angle = True; a3.angle = 90; set_angle(a3, check)
        merge_sum_value('b4', 'c4', 90, 0)
        merge_sum_value('b4', 'c4', 'a3', 1)
        merge_sum_value('c1', 'c2', 90, 0)
        merge_sum_value('c1', 'c2', 'a3', 1)
        # check_perpendicular(a, ['sc1', 'sb3', 'sd4'], True)
        # check_perpendicular(b, ['sc1', 'sb3', 'sd4'], True)
        # know_a3()

    if check_perpendicular(known, 'sa4', False):
        check = d1.right_angle
        d1.right_angle = True; d1.angle = 90; set_angle(d1, check)
        check = d3.right_angle
        d3.right_angle = True; d3.angle = 90; set_angle(d3, check)
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
        equal(d1, 'a1')
        merge_sum_value('b1', 'c1', 90, 0)
        merge_sum_value('b1', 'c1', 'a1', 1)
#         set_angle(d1)
#         know_d3()
#         # check_perpendicular(a, ['sa2', 'sa4', 'sa5'], True)
#         # check_perpendicular(b, ['sa2', 'sa4', 'sa5'], True)

    if check_perpendicular(known, 'sc4', False):
        merge_sum_value('b1', 'a1', 90, 0)
        check = c1.right_angle
        c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
        merge_sum_value('a1', 'b1', 90, 0)
        merge_sum_value('a1', 'b1', 'c1', 1)
        merge_sum_value('a3', 'c2', 90, 0)
        merge_sum_value('a3', 'c2', 'c1', 1)
#         # check_perpendicular(a, ['sc2'], True)
#         # check_perpendicular(b, ['sc2'], True)