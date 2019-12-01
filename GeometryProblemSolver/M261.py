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

ar1 = Part('ar1'); ar2 = Part('ar2')
sa1 = Part('sa1'); sb1 = Part('sb1'); sc1 = Part('sc1')
sa2 = Part('sa2'); sb2 = Part('sb2'); sc2 = Part('sc2')
sa3 = Part('sa3'); sb3 = Part('sb3')
sa4 = Part('sa4'); sb4 = Part('sb4'); sc4 = Part('sc4'); sd4 = Part('sd4')
sa5 = Part('sa5'); sb5 = Part('sb5')
a1 = Angle('a1'); b1 = Angle('b1'); c1 = Angle('c1')
a2 = Angle('a2'); b2 = Angle('b2'); c2 = Angle('c2')
d1 = Angle('d1'); d2 = Angle('d2'); d3 = Angle('d3')
d4 = Angle('d4'); d5 = Angle('d5'); d6 = Angle('d6')

angles = [a1, b1, c1, a2, b2, c2, d1, d2, d3, d4, d5]

output = {
        'parallel': [],
        'perpendicular': [],
        'equal': [],
        'fraction': [],
        'sum_value': [],
        'similar': [],
        'congruent': []
    }

init = True

# add known relations to output dictionary 
def initialize():
    global init
    if not init:
        return
    init = False

    set_equal('d1', 'd3')
    set_equal('d4', 'd6')
    set_sum_value('d1', 'd2', 180)
    set_sum_value('d2', 'd3', 180)
    set_sum_value('d4', 'd5', 180)
    set_sum_value('d5', 'd6', 180)
    set_sum_value('sa3', 'sc4', 'sb1')
    set_sum_value('sb3', 'sd4', 'sc1')
    set_sum_value('sa4', 'sa5', 'sa2')
    set_sum_value('sb4', 'sb5', 'sb2')

def get_all():
    # Congruent: SSS, SAS, ASA, AAS, HL
    # Similar: AAA
    return output

def is_same_edge(n1, n2):
    edges = [['sb1', 'sa3', 'sc4'], 
        ['sc1', 'sb3', 'sd4'], 
        ['sa2', 'sa4', 'sa5'], 
        ['sb2', 'sb4', 'sb5']]
    for e in edges:
        if n1 in e and n2 in e:
            return True
    return False

#When a “parallel” predicate is given
def set_parallel(name1, name2):
    initialize()
    if name1 in globals()[name2].parallel:
        return
    if is_same_edge(name1, name2) or is_same_edge(name2, name1):
        return
    # add pair to output and add to objects parallel list
    output['parallel'].append([name1, name2]) 
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
    if name1 in globals()[name2].perpendicular:
        return
    output['perpendicular'].append([name1, name2]) 
    x = globals()[name1].perpendicular
    x.append(name2)
    y = globals()[name2].perpendicular
    y.append(name1)

    globals()['know_'+name1]()
    globals()['know_'+name2]()

#true if 2 angles, line segments, or areas are equal
def set_equal(name1, name2): 
    initialize()
    if name1 in globals()[name2].equal:
        return
    output['equal'].append([name1, name2]) 
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
    if name1 in globals()[name2].fraction: # and fraction in globals()[name2].fraction[name1]:
        return
    output['fraction'].append([name1, name2, fraction])
    x = globals()[name1].fraction
    # if key exists in dict, append to list
    #if name2 in x and fraction not in x[name2]:
    #x[name2].append(1/fraction)
    # else create key list pair in dict
    #else:
    x[name2] = fraction
    y = globals()[name2].fraction
    # if name1 in y and fraction not in y[name1]:
    #     y[name1].append(fraction)
    # else:
    y[name1] = 1/fraction

    merge_fraction(name1, name2, fraction)
    merge_fraction(name2, name1, 1/fraction)

    globals()['know_'+name1]()
    globals()['know_'+name2]()

# true if 2 angles, line segments, or areas 
# satisfy relationship name1+name2=sum
def set_sum_value(name1, name2, sum_val):
    initialize()
    if name1 in globals()[name2].sum_value and sum_val in globals()[name2].sum_value[name1]:
        return
    if name1 == name2:
        return

    output['sum_value'].append([name1, name2, sum_val])
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
    output['similar'].append([name1, name2])
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
    output['congruent'].append([name1, name2])
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

def know_ar1():
    return

def know_ar2():
    return

def check_right_angle(angle, name1, name2, s1, s2):
    if angle.right_angle:
        set_sum_value(name1, name2, 90)
        set_sum_value(name1, name2, angle.name)
        check_perpendicular(s1, s2, True)

def know_a1():
    # if a1 = 90, then b1+c1 = 90 because a1+b1+c1 = 180
    check_right_angle(a1, 'b1', 'c1', sb1, 'sc1')

    if 'c1' in a1.equal:
        equal(sa1, 'sc1')
    if 'b1' in a1.equal:
        equal(sa1, 'sb1')
    # if 'c2' in a1.equal:
    
    if 'd1' in a1.equal or 'd3' in a1.equal:
        set_parallel('sc1', 'sa2')
        merge_sum_value('a1', 'd2', 180, 0)
    
    if 'd4' in a1.equal or 'd6' in a1.equal:
        set_parallel('sb1', 'sb2')
        merge_sum_value('a1', 'd5', 180, 0)
    
    if 'd2' in a1.equal:
        merge_sum_value('a1', 'd1', 180, 0)

    if 'd5' in a1.equal:
        merge_sum_value('a1', 'd4', 180, 0)
    
    if 'b1' in a1.sum_value and 90 in a1.sum_value['b1']:
        check = c1.right_angle
        c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
    if 'c1' in a1.sum_value and 90 in a1.sum_value['c1']:
        check = b1.right_angle
        b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
    if 'c2' in a1.sum_value:
        for item in a1.sum_value['c2']:
            if type(item) == int:
                merge_sum_value('d2', 'd5', 360-item, 0)
                break
    
    if 'd2' in a1.sum_value:
        if 90 in a1.sum_value['d2']:
            check_perpendicular(sa2, 'sc1', True)
            # check_perpendicular(sa4, 'sc1', 'sb3', 'sd4'], True)
            # check_perpendicular(sa5, 'sc1', 'sb3', 'sd4'], True)
        if 180 in a1.sum_value['d2']:
            equal(a1, 'd1')
        for item in a1.sum_value['d2']:
            if type(item) == int:
                merge_sum_value('c2', 'd5', 360-item, 0)
                break
    
    if 'd5' in a1.sum_value:
        if 90 in a1.sum_value['d5']:
            check_perpendicular(sb1, 'sb2', True)
            # check_perpendicular(sa3, ['sb2', 'sb4', 'sb5'], True)
            # check_perpendicular(sc4, ['sb2', 'sb4', 'sb5'], True)
        if 180 in a1.sum_value['d5']:
            equal(a1, 'd4')
        for item in a1.sum_value['d5']:
            if type(item) == int:
                merge_sum_value('c2', 'd2', 360-item, 0)
                break

    if 'd1' in a1.sum_value and 180 in a1.sum_value['d1'] or 'd3' in a1.sum_value and 180 in a1.sum_value['d3']:
        equal(a1, 'd2')

    if 'd4' in a1.sum_value and 180 in a1.sum_value['d4'] or 'd6' in a1.sum_value and 180 in a1.sum_value['d6']:
        equal(a1, 'd5')

def know_b1():
    # if b1 = 90, then b1+c1 = 90 because a1+b1+c1 = 180
    # check_corner_angle(b1, 'a1', 'c1')
    check_right_angle(b1, 'a1', 'c1', sa1, 'sc1')

    if 'a1' in b1.equal:
        equal(sa1, 'sb1')
    if 'c1' in b1.equal:
        equal(sb1, 'sc1')
    # if 'c2' in a1.equal:
    
    if 'd4' in b1.equal or 'd6' in b1.equal:
        merge_sum_value('b1', 'd5', 180, 0)
    
    if 'd5' in b1.equal:
        set_parallel('sa1', 'sb2')
        merge_sum_value('b1', 'd4', 180, 0)
    
    if 'a1' in b1.sum_value and 90 in b1.sum_value['a1']:
        check = c1.right_angle
        c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
    if 'c1' in b1.sum_value and 90 in b1.sum_value['c1']:
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
    
    if 'd4' in b1.sum_value or 'd6' in b1.sum_value:
        if 'd4' in b1.sum_value:
            i = 'd4'
        else:
            i = 'd6'
        if 90 in b1.sum_value[i]:
            check_perpendicular(sa1, 'sb2', True)
            merge_sum_value('b1', i, 90, 0)
        if 180 in b1.sum_value[i]:
            equal(b1, 'd5')
        if i == 'd4':
            for item in b1.sum_value['d4']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('b1', 'd6', item, x)
        else:
            for item in  b1.sum_value['d6']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('b1', 'd4', item, x)

    if 'd5' in b1.sum_value and 180 in b1.sum_value['d5']:
        equal(b1, 'd4')

def know_c1():
    # if c1 = 90, then b1+c1 = 90 because a1+b1+c1 = 180
    # check_corner_angle(c1, 'a1', 'b1')
    check_right_angle(c1, 'a1', 'b1', sa1, 'sb1')

    if 'a1' in c1.equal:
        equal(sa1, 'sc1')
    if 'b1' in c1.equal:
        equal(sb1, 'sc1')
    
    if 'd1' in c1.equal or 'd3' in c1.equal:
        merge_sum_value('c1', 'd2', 180, 0)
    
    if 'd2' in c1.equal:
        set_parallel('sa1', 'sa2')
        merge_sum_value('c1', 'd1', 180, 0)

    if 'a1' in c1.sum_value and 90 in c1.sum_value['a1']:
        check = b1.right_angle
        b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
    if 'b1' in c1.sum_value and 90 in c1.sum_value['b1']:
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
    
    if 'd1' in c1.sum_value or 'd3' in c1.sum_value:
        if 'd3' in c1.sum_value:
            i = 'd3'
        else:
            i = 'd1'
        if 90 in c1.sum_value[i]:
            check_perpendicular(sa1, 'sa2', True)
        if 180 in c1.sum_value[i]:
            equal(c1, 'd2')
        if i == 'd1':
            for item in  c1.sum_value['d1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('c1', 'd3', item, x)
        else:
            for item in  c1.sum_value['d3']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('c1', 'd1', item, x)

    if 'd2' in b1.sum_value and 180 in b1.sum_value['d2']:
        equal(c1, 'd1')

def know_a2():
    # check_corner_angle(a2, 'b2', 'c2')
    check_right_angle(a2, 'b2', 'c2', sb2, 'sc2')

    if 'b2' in a2.equal:
        equal(sa2, 'sb2')
    if 'c2' in a2.equal:
        equal(sa2, 'sc2')
    
    if 'd4' in a2.equal or 'd6' in a2.equal:
        merge_sum_value('a2', 'd5', 180, 0)
    
    if 'd5' in a2.equal:
        set_parallel('sc2', 'sc1')
        merge_sum_value('a2', 'd4', 180, 0)
    
    if 'b2' in a2.sum_value and 90 in a2.sum_value['b2']:
        check = c2.right_angle
        c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
    if 'c2' in a2.sum_value and 90 in a2.sum_value['c2']:
        check = b2.right_angle
        b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
    
    if 'd4' in a2.sum_value or 'd6' in a2.sum_value:
        if 'd4' in a2.sum_value:
            i = 'd4'
        else:
            i = 'd6'
        if 90 in a2.sum_value[i]:
            check_perpendicular(sc1, 'sc2', True)
        if 180 in a2.sum_value[i]:
            equal(a2, 'd5')
        if i == 'd4':
            for item in  a2.sum_value['d4']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('a2', 'd6', item, x)
        else:
            for item in  a2.sum_value['d6']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('a2', 'd4', item, x)

    if 'd5' in a2.sum_value and 180 in a2.sum_value['d5']:
        equal(a2, 'd4')

def know_b2():
    # check_corner_angle(b2, 'a2', 'c2')
    check_right_angle(b2, 'a2', 'c2', sa2, 'sc2')

    if 'a2' in b2.equal:
        equal(sa2, 'sb2')
    if 'c2' in b2.equal:
        equal(sb2, 'sc2')
    
    if 'd1' in b2.equal or 'd3' in b2.equal:
        merge_sum_value('b2', 'd2', 180, 0)
    
    if 'd2' in b2.equal:
        set_parallel('sc2', 'sb1')
        merge_sum_value('b2', 'd1', 180, 0)

    if 'a2' in b2.sum_value and 90 in b2.sum_value['a2']:
        check = c2.right_angle
        c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
    if 'c2' in b2.sum_value and 90 in b2.sum_value['c2']:
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
    
    if 'd1' in b2.sum_value or 'd3' in b2.sum_value:
        if 'd3' in b2.sum_value:
            i = 'd3'
        else:
            i = 'd1'
        if 90 in b2.sum_value[i]:
            check_perpendicular(sb1, 'sc2', True)
        if 180 in b2.sum_value[i]:
            equal(b2, 'd2')
        if i == 'd1':
            for item in  b2.sum_value['d1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('b2', 'd3', item, x)
        else:
            for item in  b2.sum_value['d3']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value('b2', 'd1', item, x)

    if 'd2' in b2.sum_value and 180 in b2.sum_value['d2']:
        equal(c2, 'd1')

def know_c2():
    # check_corner_angle(c2, 'a2', 'b2')
    check_right_angle(c2, 'a2', 'b2', sa2, 'sb2')

    if 'a2' in c2.equal:
        equal(sa2, 'sc2')
    if 'b2' in c2.equal:
        equal(sb2, 'sc2')
    
    if 'd1' in c2.equal or 'd3' in c2.equal:
        set_parallel('sb1', 'sb2')
        merge_sum_value('c2', 'd2', 180, 0)
    
    if 'd4' in c2.equal or 'd6' in c2.equal:
        set_parallel('sa2', 'sc1')
        merge_sum_value('c2', 'd5', 180, 0)
    
    if 'd2' in c2.equal:
        merge_sum_value('c2', 'd1', 180, 0)

    if 'd5' in c2.equal:
        merge_sum_value('c2', 'd4', 180, 0)
    
    if 'a2' in c2.sum_value and 90 in c2.sum_value['a2']:
        check = b2.right_angle
        b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
    if 'b2' in c2.sum_value and 90 in c2.sum_value['b2']:
        check = a2.right_angle
        a2.right_angle = True; a2.angle = 90; set_angle(a2, check)
    if 'a1' in c2.sum_value:
        for item in c2.sum_value['a1']:
            if type(item) == int:
                merge_sum_value('d2', 'd5', 360-item, 0)
                break
    
    if 'd2' in c2.sum_value:
        if 90 in c2.sum_value['d2']:
            check_perpendicular(sb1, 'sb2', True)
        if 180 in c2.sum_value['d2']:
            equal(c2, 'd1')
        for item in c2.sum_value['d2']:
            if type(item) == int:
                merge_sum_value('a1', 'd5', 360-item, 0)
                break
    
    if 'd5' in c2.sum_value:
        if 90 in c2.sum_value['d5']:
            check_perpendicular(sc1, 'sa2', True)
        if 180 in c2.sum_value['d5']:
            equal(c2, 'd4')
        for item in c2.sum_value['d5']:
            if type(item) == int:
                merge_sum_value('a1', 'd2', 360-item, 0)
                break

    if 'd1' in c2.sum_value and 180 in c2.sum_value['d1'] or 'd3' in c2.sum_value and 180 in c2.sum_value['d3']:
        equal(c2, 'd2')

    if 'd4' in c2.sum_value and 180 in c2.sum_value['d4'] or 'd6' in c2.sum_value and 180 in c2.sum_value['d6']:
        equal(c2, 'd5')

def check_d_angles(known, adj, opp, n1, n2):
    if known.right_angle:
        check = adj.right_angle
        adj.right_angle = True; adj.angle = 90; set_angle(adj, check)
        check = opp.right_angle
        opp.right_angle = True; opp.angle = 90; set_angle(opp, check)
        equal(known, adj.name)
        merge_sum_value(known.name, opp.name, 180, 0)
        check_perpendicular(n1, n2, True)

def d1_d3(known, a, b, s1, s2):
    check_d_angles(d1, d2, d3, sb1, 'sa2')

    if 'd2' in known.equal:
        check = known.right_angle
        known.right_angle = True; known.angle = 90; set_angle(known, check)
        check_d_angles(d1, d2, d3, sb1, 'sa2')
    
    if 'a1' in known.equal:
        set_parallel('sa2', 'sc1')
        equal(a1, a.name)
        merge_sum_value('a1', 'd2', 180, 0)
    
    if 'c2' in known.equal:
        set_parallel('sb1', 'sb2')
        equal(c2, a.name)
        merge_sum_value('c2', 'd2', 180, 0)

    if 'd4' in known.equal or 'd6' in known.equal:
        equal(a, 'd4')
        equal(d2, 'd5')
        merge_sum_value('d1', 'd5', 180, 0)

    if 'd5' in known.equal:
        equal(d2, 'd4')
        merge_sum_value('d2', 'd5', 180, 0)
        merge_sum_value(known.name, 'd4', 180, 0)

    if b in d1.sum_value and 90 in d1.sum_value[b]:
        check_perpendicular(s1, s2, True)
    
    if a.name in known.sum_value and 180 in known.sum_value[a.name]:
        check = d1.right_angle
        d1.right_angle = True; d1.angle = 90; set_angle(d1, check)
        check = d2.right_angle
        d2.right_angle = True; d2.angle = 90; set_angle(d2, check)
        check = d3.right_angle
        d3.right_angle = True; d3.angle = 90; set_angle(d3, check)

    if 'd4' in known.sum_value or 'd6' in known.sum_value:
        if 'd4' in known.sum_value:
            for item in known.sum_value['d4']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value(a.name, 'd4', item, x)
        else:
            for item in  known.sum_value['d6']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value(a.name, 'd6', item, x)

    if 'd5' in known.sum_value and 180 in known.sum_value['d5']:
        equal(known, 'd4'); equal(d2, 'd5') #; equal(a1, 'c2')
        #set_parallel('sb1', 'sb2'); set_parallel('sa2', 'sc1')
        merge_sum_value('d3', 'd5', 180, 0)
        merge_sum_value('d2', 'd4', 180, 0)

def d4_d6(known, a, b, s1, s2):
    check_d_angles(d4, d5, d6, sc1, 'sb2')

    if 'd5' in known.equal:
        check = known.right_angle
        known.right_angle = True; known.angle = 90; set_angle(known, check)
        check_d_angles(d4, d5, d6, sc1, 'sb2')
    
    if 'a1' in known.equal:
        set_parallel('sb1', 'sb2')
        equal(a1, a.name)
        merge_sum_value('a1', 'd5', 180, 0)
    
    if 'c2' in known.equal:
        set_parallel('sa2', 'sc1')
        equal(c2, a.name)
        merge_sum_value('c2', 'd5', 180, 0)

    if 'd1' in known.equal or 'd3' in known.equal:
        equal(a, 'd1')
        equal(d2, 'd5')
        merge_sum_value('d4', 'd2', 180, 0)

    if 'd2' in known.equal:
        equal(d5, 'd1')
        merge_sum_value('d2', 'd5', 180, 0)
        merge_sum_value(known.name, 'd1', 180, 0)

    if b in d1.sum_value and 90 in d1.sum_value[b]:
        check_perpendicular(s1, s2, True)
    
    if a.name in known.sum_value and 180 in known.sum_value[a.name]:
        check = d4.right_angle
        d4.right_angle = True; d4.angle = 90; set_angle(d4, check)
        check = d5.right_angle
        d5.right_angle = True; d5.angle = 90; set_angle(d5, check)
        check = d6.right_angle
        d6.right_angle = True; d6.angle = 90; set_angle(d6, check)

    if 'd1' in known.sum_value or 'd3' in known.sum_value:
        if 'd1' in known.sum_value:
            for item in known.sum_value['d1']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value(a.name, 'd1', item, x)
        else:
            for item in  known.sum_value['d3']:
                if type(item) == str: 
                    x = 1
                else:
                    x = 0
                merge_sum_value(a.name, 'd3', item, x)

    if 'd2' in known.sum_value and 180 in known.sum_value['d2']:
        equal(known, 'd1'); equal(d2, 'd5') #; equal(a1, 'c2')
        #set_parallel('sb1', 'sb2'); set_parallel('sa2', 'sc1')
        merge_sum_value('d1', 'd5', 180, 0)
        merge_sum_value('d2', 'd4', 180, 0)

def know_d1():
    d1_d3(d1, d3, 'c1', sa1, 'sb1')

def know_d2():
    check_d_angles(d1, d2, d3, sb1, 'sa2')

    if 'd1' in d2.equal or 'd3' in d2.equal:
        check = d1.right_angle
        d1.right_angle = True; d1.angle = 90; set_angle(d1, check)
        check = d2.right_angle
        d2.right_angle = True; d2.angle = 90; set_angle(d2, check)
        check = d3.right_angle
        d3.right_angle = True; d3.angle = 90; set_angle(d3, check)
        check_perpendicular(sb1, 'sa2', True)

    if 'd5' in d2.equal:
        equal(d1, 'd4')

    if 'c2' in d2.sum_value:
        if 90 in d2.sum_value['c2']:
            check_perpendicular(sb1, 'sb2', True)
        if 180 in d2.sum_value['c2']:
            equal(c2, 'd1')
        for item in d2.sum_value['c2']:
                if type(item) == int: 
                #     x = 1
                # else:
                #     x = 0
                    merge_sum_value('a1', 'd5', 360-item, 0)

    if 'a1' in d2.sum_value:
        if 90 in d2.sum_value['a1']:
            check_perpendicular(sa2, 'sc1', True)
        if 180 in d2.sum_value['a1']:
            equal(a1, 'd1')
        for item in  d2.sum_value['a1']:
                if type(item) == int: 
                #     x = 1
                # else:
                #     x = 0
                    merge_sum_value('c2', 'd5', 360-item, 0)
    
    if 'd5' in d2.sum_value:
        for item in  d2.sum_value['d5']:
                if type(item) == int: 
                #     x = 1
                # else:
                #     x = 0
                    merge_sum_value('c2', 'a1', 360-item, 0)
       
def know_d3():
    d1_d3(d3, d1, 'b2', sb1, 'sc2')

def know_d4():
    d4_d6(d4, d6, 'b1', sa1, 'sb2')

def know_d5():
    check_d_angles(d4, d5, d6, sc1, 'sb2')

    if 'd4' in d5.equal or 'd6' in d5.equal:
        check = d4.right_angle
        d4.right_angle = True; d4.angle = 90; set_angle(d4, check)
        check = d5.right_angle
        d5.right_angle = True; d5.angle = 90; set_angle(d5, check)
        check = d6.right_angle
        d6.right_angle = True; d6.angle = 90; set_angle(d6, check)
        check_perpendicular(sb3, 'sb5', True)

    if 'd2' in d5.equal:
        equal(d1, 'd4')

    if 'c2' in d5.sum_value:
        if 90 in d5.sum_value['c2']:
            check_perpendicular(sc1, 'sa2', True)
        if 180 in d5.sum_value['c2']:
            equal(c2, 'd4')
        for item in  d5.sum_value['c2']:
                if type(item) == int: 
                #     x = 1
                # else:
                #     x = 0
                    merge_sum_value('a1', 'd2', 360-item, 0)

    if 'a1' in d5.sum_value:
        if 90 in d5.sum_value['a1']:
            check_perpendicular(sb2, 'sb1', True)
        if 180 in d5.sum_value['a1']:
            equal(a1, 'd4')
        for item in  d5.sum_value['a1']:
                if type(item) == int: 
                #     x = 1
                # else:
                #     x = 0
                    merge_sum_value('c2', 'd2', 360-item, 0)
    
    if 'd5' in d5.sum_value:
        for item in  d5.sum_value['d5']:
                if type(item) == str: 
                #     x = 1
                # else:
                #     x = 0
                    merge_sum_value('c2', 'a1', 360-item, 0)

def know_d6():
    d4_d6(d6, d4, 'a2', sc1, 'sc2')

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

def check_sum(a, name, val):
    if name not in a.sum_value or val not in a.sum_value[name]:
        return True
    return False

def check_perpendicular(a, name, perpendicular):
    edges = [['sb1', 'sa3', 'sc4'], 
        ['sc1', 'sb3', 'sd4'], 
        ['sa2', 'sa4', 'sa5'], 
        ['sb2', 'sb4', 'sb5']]
    
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

def know_sa1():
    if check_parallel(sa1, ['sa2', 'sa5', 'sa4']):
        equal(c1, 'd2')
    
    if check_parallel(sa1, ['sb2', 'sb4', 'sb5']):
        equal(b1, 'd5')
    
    if check_perpendicular(sa1, 'sb1', False):
        check = c1.right_angle
        c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
        merge_sum_value('a1', 'b1', 90, 0)
        merge_sum_value('a1', 'b1', 'c1', 1)
    
    if check_perpendicular(sa1, 'sc1', False):#['sc1', 'sb3', 'sd4'], False):
        check = b1.right_angle
        b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
        merge_sum_value('a1', 'c1', 90, 0)
        merge_sum_value('a1', 'c1', 'b1', 1)
    
    if check_perpendicular(sa1, 'sa2', False):
        merge_sum_value('c1', 'd1', 90, 0)
        merge_sum_value('c1', 'd3', 90, 0)

    if check_perpendicular(sa1, 'sb2', False):
        merge_sum_value('b1', 'd4', 90, 0)
        merge_sum_value('b1', 'd6', 90, 0)

    if 'sb1' in sa1.equal:
        equal(a1, 'b1')
        merge_sum_value('sa3', 'sc4', 'sa1', 1)
    
    if 'sc1' in sa1.equal:
        equal(a1, 'c1')
        merge_sum_value('sb3', 'sd4', 'sa1', 1)

def know_sb1():
    sb1_sa3_sc4(sb1, sa3, sc4)
    
def know_sc1():
    sc1_sb3_sd4(sc1, sb3, sd4)
    
def know_sa2():
    sa2_sa4_sa5(sa2, sa4, sa5)

def know_sb2():
    sb2_sb4_sb5(sb2, sb4, sb5)

def know_sc2():
    if check_parallel(sc2, ['sb1', 'sa3', 'sc4']):
        equal(b2, 'd2')

    if check_parallel(sc2, ['sc1', 'sd4', 'sb3']):
        equal(a2, 'd5')

    if check_perpendicular(sc2, 'sb1', False):
        merge_sum_value('b2', 'd1', 90, 0)
        #merge_sum_value('a1', 'b1', 'c1', 1)
    
    if check_perpendicular(sc2, 'sc1', False):
        merge_sum_value('a2', 'd4', 90, 0)
        #merge_sum_value('a1', 'c1', 'b1', 1)
    
    if check_perpendicular(sc2, 'sa2', False):
        check = b2.right_angle
        b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
        merge_sum_value('a2', 'c2', 90, 0)
        merge_sum_value('a2', 'c2', 'b2', 1)
        # know_b2()

    if check_perpendicular(sc2, 'sb2', False):
        check = a2.right_angle
        a2.right_angle = True; a2.angle = 90; set_angle(a2, check)
        merge_sum_value('b2', 'c2', 90, 0)
        merge_sum_value('b2', 'c2', 'a2', 1)
        # know_a2()

    if 'sa2' in sc2.equal:
        equal(a2, 'c2')
        merge_sum_value('sa4', 'sa5', 'sc2', 1)
    
    if 'sb2' in sc2.equal:
        equal(b2, 'c2')
        merge_sum_value('sb4', 'sb5', 'sc2', 1)

def know_sa3():
    sb1_sa3_sc4(sa3, sb1, sc4)

def know_sb3():
    sc1_sb3_sd4(sb3, sc1, sd4)

def know_sa4():
    sa2_sa4_sa5(sa4, sa2, sa5)
    
def know_sb4():
    sb2_sb4_sb5(sb4, sb2, sb5)
    
def know_sc4():
    sb1_sa3_sc4(sc4, sb1, sa3)
    
def know_sd4():
    sc1_sb3_sd4(sd4, sc1, sb3)
    
def know_sa5():
    sa2_sa4_sa5(sa5, sa2, sa4)
    
def know_sb5():
    sb2_sb4_sb5(sb5, sb2, sb4)

def sc1_sb3_sd4(known, a, b):
    if check_parallel(known, ['sc2']):
        equal(a2, 'd5')

    if check_parallel(known, ['sa2', 'sa5', 'sa4']):
        equal(a1, 'd1'); equal(c2, 'd4')
    
    if check_perpendicular(known, 'sa1', False): 
        check = b1.right_angle
        b1.right_angle = True; b1.angle = 90; set_angle(b1, check)
        merge_sum_value('a1', 'c1', 90, 0)
        merge_sum_value('a1', 'c1', 'b1', 1)
        #check_perpendicular(a, 'sa1', True)
        #check_perpendicular(b, 'sa1', True)
        # know_b1()
    
    if check_perpendicular(known, 'sb1', False): 
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
        merge_sum_value('b1', 'c1', 90, 0)
        merge_sum_value('b1', 'c1', 'a1', 1)
        #check_perpendicular(a, 'sb1', True)
        #check_perpendicular(b, 'sb1', True)
        # know_a1()

    if check_perpendicular(known, 'sb2', False):
        check = d4.right_angle
        d4.right_angle = True; d4.angle = 90; set_angle(d4, check)
        check = d5.right_angle
        d5.right_angle = True; d5.angle = 90; set_angle(d5, check)
        check = d6.right_angle
        d6.right_angle = True; d6.angle = 90; set_angle(d6, check)
        equal(d4, 'd5')
        # set_angle(d4)
        # know_d6()
        #check_perpendicular(a, ['sb2', 'sb4', 'sb5'], True)
        #check_perpendicular(b, ['sb2', 'sb4', 'sb5'], True)

    if check_perpendicular(known, 'sc2', False):
        merge_sum_value('a2', 'd4', 90, 0)
        # check_perpendicular(a, ['sc2'], True)
        # check_perpendicular(b, ['sc2'], True)
    
    if known.name == 'sc1':
        for i in ['sa2', 'sb2', 'sc2']:
            if i in sc1.equal:
                merge_sum_value('sb3', 'sd4', i, 1)

        if 'sa1' in sc1.equal:
            equal(a1, 'c1')
            merge_sum_value('sb3', 'sd4', 'sa1', 1)
        
        if 'sb1' in sc1.equal:
            equal(b1, 'c1')
            merge_sum_value('sb3', 'sd4', 'sb1', 1)
            merge_sum_value('sa3', 'sc4', 'sc1', 1)

    if known.name == 'sb3':
        if 'sd4' in sb3.fraction:
            print(sb3.fraction['sd4'])
            if sb3.fraction['sd4'] > 1:
                set_fraction('sc2', 'sd4', sb3.fraction['sd4']+1)

    if known.name == 'sd4':
        if 'sb3' in sd4.fraction:
            print(sd4.fraction['sb3'])
            if sd4.fraction['sb3'] > 1:
                set_fraction('sc2', 'sb3', sd4.fraction['sb3']+1)

def sa2_sa4_sa5(known, a, b):
    if check_parallel(known, ['sa1']):
        equal(c1, 'd2')
    
    if check_parallel(known, ['sc1', 'sd4', 'sb3']):
        equal(a1, 'd1'); equal(c2, 'd4')
    
    if check_perpendicular(known, 'sc2', False):
        check = b2.right_angle
        b2.right_angle = True; b2.angle = 90; set_angle(b2, check)
        merge_sum_value('a2', 'c2', 90, 0)
        merge_sum_value('a2', 'c2', 'b2', 1)
        # check_perpendicular(a, ['sc2'], True)
        # check_perpendicular(b, ['sc2'], True)
        # know_b2()

    if check_perpendicular(known, 'sb2', False):
        check = c2.right_angle
        c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
        merge_sum_value('a2', 'b2', 90, 0)
        merge_sum_value('a2', 'b2', 'c2', 1)
        # check_perpendicular(a, ['sb2', 'sb4', 'sb5'], True)
        # check_perpendicular(b, ['sb2', 'sb4', 'sb5'], True)
        # know_c2()

    if check_perpendicular(known, 'sb1', False):
        check = d1.right_angle
        d1.right_angle = True; d1.angle = 90; set_angle(d1, check)
        check = d2.right_angle
        d2.right_angle = True; d2.angle = 90; set_angle(d2, check)
        check = d3.right_angle
        d3.right_angle = True; d3.angle = 90; set_angle(d3, check)
        equal(d1, 'd2')
        # set_angle(d1)
        # know_d3()
        # check_perpendicular(a, ['sb1', 'sa3', 'sc4'], True)
        # check_perpendicular(a, ['sb1', 'sa3', 'sc4'], True)

    if check_perpendicular(known, 'sa1', False):
        merge_sum_value('c1', 'd1', 90, 0)
        # check_perpendicular(a, ['sa1'], True)
        # check_perpendicular(b, ['sa1'], True)

    if known.name == 'sa2':
        for i in ['sa1', 'sb1', 'sc1']:
            if i in sa2.equal:
                merge_sum_value('sa4', 'sa5', i, 1)

        if 'sb2' in sa2.equal:
            equal(a2, 'b2')
            merge_sum_value('sa4', 'sa5', 'sb2', 1)
            merge_sum_value('sb4', 'sb5', 'sa2', 1)
        
        if 'sc2' in sa2.equal:
            equal(a2, 'c2')
            merge_sum_value('sa4', 'sa5', 'sc2', 1)

    if known.name == 'sa4':
        if 'sa5' in sa4.fraction:
            print(sa4.fraction['sa5'])
            if sa4.fraction['sa5'] > 1:
                set_fraction('sa2', 'sa5', sa4.fraction['sa5']+1)

    if known.name == 'sa5':
        if 'sa4' in sa5.fraction:
            print(sa5.fraction['sa4'])
            if sa5.fraction['sa4'] > 1:
                set_fraction('sa2', 'sa4', sa5.fraction['sa4']+1)

def sb2_sb4_sb5(known, a, b):
    if check_parallel(known, ['sa1']):
        equal(b1, 'd5') 

    if check_parallel(known, ['sb1', 'sa3', 'sc4']):
        equal(a1, 'd4'); equal(c2, 'd1')
    
    if check_perpendicular(known, 'sc2', False):
        check = a2.right_angle
        a2.right_angle = True; a2.angle = 90; set_angle(a2, check)
        merge_sum_value('b2', 'c2', 90, 0)
        merge_sum_value('b2', 'c2', 'a2', 1)
        # check_perpendicular(a, ['sc2'], True)
        # check_perpendicular(b, ['sc2'], True)
        # know_a2()

    if check_perpendicular(known, 'sa2', False):
        check = c2.right_angle
        c2.right_angle = True; c2.angle = 90; set_angle(c2, check)
        merge_sum_value('a2', 'b2', 90, 0)
        merge_sum_value('a2', 'b2', 'c2', 1)
        # check_perpendicular(a, ['sa2', 'sa4', 'sa5'], True)
        # check_perpendicular(a, ['sa2', 'sa4', 'sa5'], True)
        # know_c2()

    if check_perpendicular(known, 'sc1', False):
        check = d4.right_angle
        d4.right_angle = True; d4.angle = 90; set_angle(d4, check)
        check = d5.right_angle
        d5.right_angle = True; d5.angle = 90; set_angle(d5, check)
        check = d6.right_angle
        d6.right_angle = True; d6.angle = 90; set_angle(d6, check)
        equal(d4, 'd5')
        # set_angle(d4)
        # know_d6()
        # check_perpendicular(a, ['sc1', 'sb3', 'sd4'], True)
        # check_perpendicular(a, ['sc1', 'sb3', 'sd4'], True)

    if check_perpendicular(known, 'sa1', False):
        merge_sum_value('b1', 'd4', 90, 0)
        # check_perpendicular(a, ['sa1'], True)
        # check_perpendicular(b, ['sa1'], True)

    if known.name == 'sb2':
        for i in ['sa1', 'sb1', 'sc1']:
            if i in sb2.equal:
                merge_sum_value('sb4', 'sb5', i, 1)

        if 'sa2' in sb2.equal:
            equal(a2, 'b2')
            merge_sum_value('sb4', 'sb5', 'sa2', 1)
            merge_sum_value('sa4', 'sa5', 'sb2', 1)
        
        if 'sc2' in sb2.equal:
            equal(b2, 'c2')
            merge_sum_value('sb4', 'sb5', 'sc2', 1)

    if known.name == 'sb4':
        if 'sb5' in sb4.fraction:
            print(sb4.fraction['sb5'])
            if sb4.fraction['sb5'] > 1:
                set_fraction('sb2', 'sb5', sb4.fraction['sb5']+1)

    if known.name == 'sb5':
        if 'sb4' in sb5.fraction:
            print(sb5.fraction['sb4'])
            if sb5.fraction['sb4'] > 1:
                set_fraction('sb2', 'sb4', sb5.fraction['sb4']+1)

def sb1_sa3_sc4(known, a, b):
    if check_parallel(known, ['sb2', 'sb4', 'sb5']):
        equal(a1, 'd4'); equal(c2, 'd1')
    
    if check_parallel(known, ['sc2']):
        equal(b2, 'd2')
    
    if check_perpendicular(known, 'sa1', False): #and check_sum(a1, 'b1', 90):
        check = c1.right_angle
        c1.right_angle = True; c1.angle = 90; set_angle(c1, check)
        merge_sum_value('a1', 'b1', 90, 0)
        merge_sum_value('a1', 'b1', 'c1', 0)
        # check_perpendicular(a, ['sa1'], True)
        # check_perpendicular(b, ['sa1'], True)
        # know_c1()

    if check_perpendicular(known, 'sc1', False): #and check_sum(b1, 'c1', 90):
        check = a1.right_angle
        a1.right_angle = True; a1.angle = 90; set_angle(a1, check)
        merge_sum_value('b1', 'c1', 90, 0)
        merge_sum_value('b1', 'c1', 'a1', 1)
        # check_perpendicular(a, ['sc1', 'sb3', 'sd4'], True)
        # check_perpendicular(b, ['sc1', 'sb3', 'sd4'], True)
        # know_a1()

    if check_perpendicular(known, 'sa2', False):
        check = d1.right_angle
        d1.right_angle = True; d1.angle = 90; set_angle(d1, check)
        check = d2.right_angle
        d2.right_angle = True; d2.angle = 90; set_angle(d2, check)
        check = d3.right_angle
        d3.right_angle = True; d3.angle = 90; set_angle(d3, check)
        equal(d1, 'd2')
        # set_angle(d1)
        # know_d3()
        # check_perpendicular(a, ['sa2', 'sa4', 'sa5'], True)
        # check_perpendicular(b, ['sa2', 'sa4', 'sa5'], True)

    if check_perpendicular(known, 'sc2', False):
        merge_sum_value('b2', 'd3', 90, 0)
        # check_perpendicular(a, ['sc2'], True)
        # check_perpendicular(b, ['sc2'], True)

    if known.name == 'sb1':
        for i in ['sa2', 'sb2', 'sc2']:
            if i in sb1.equal:
                merge_sum_value('sa3', 'sc4', i, 1)
        if 'sa1' in sb1.equal:
            equal(a1, 'b1')
            merge_sum_value('sa3', 'sc4', 'sa1', 1)

        if 'sc1' in sb1.equal:
            equal(b1, 'c1')
            merge_sum_value('sa3', 'sc4', 'sc1', 1)
            merge_sum_value('sb3', 'sd4', 'sb1', 1)

    if known.name == 'sa3':
        if 'sc4' in sa3.fraction:
            print(sa3.fraction['sc4'])
            if sa3.fraction['sc4'] > 1:
                set_fraction('sb1', 'sc4', sa3.fraction['sc4']+1)

    if known.name == 'sc4':
        if 'sa3' in sc4.fraction:
            print(sc4.fraction['sa3'])
            if sc4.fraction['sa3'] > 1:
                set_fraction('sb1', 'sa3', sc4.fraction['sa3']+1)