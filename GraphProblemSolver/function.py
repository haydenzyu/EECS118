#   Hayden Yu, Sienna Ballot    #
#   EECS 118 Graph Term Project #
#   December 5, 2019            #
# 11. find s where is_path(s, A, B) and color(s, Color, t) and t>C
# C = user input, t = number of edges that has the Color k

import networkx as nx

#s is an array of tuples, ex. [('1','2'), ('2', '4')]
def is_path(s, a, b): #returns true if s is a path between node a and node b
    #s is a set of edges
    #a is the starting point, b is end point
    #starting point 'a' [a, x] trace until [y, b]
    arr = []
    return check_path(s, a, b, arr)

#s is an array of tuples, ex. [('1','2'), ('2', '4')]
def check_path(s, a, b, arr):
    result = False
    for i in s: #i[x, y] -> i[y, y1] -> ... -> i[yn, b]
        if i[0]==a or i[1]==a: #finding starting point
            if i[1] == b or i[0] == b: #found end point
                result = True
                return result
            elif i[0]==a and i[1] not in arr: #[x,y] -> a is x, y becomes a
                a = i[1]
            elif i[1]==a and i[0] not in arr: #[x,y] -> a is y, x becomes a
                a = i[0]
            else: #can't find a
                return False
            
            if result: #result is true
                break
            else: #path hasn't been found, append nodes to discarded nodes array
                arr.append(i[0])
                arr.append(i[1])
                s.remove(i)
                result = check_path(s, a, b, arr)
        else:
            continue
        
    return result

#s is an array of tuples, ex. [('1','2'), ('2', '4')]
def color(s, k, n): #returns true if number of edges of color k in s is n
    cnt = 0
    #count how many edges have the color k
    for i in s:
        #print(i[2])
        if i[2] == k:
            cnt+=1
        else:
            continue

    #result
    if cnt == n:
        return True
    else:
        return False

#s is an array of tuples, ex. [('1','2'), ('2', '4')]
def find_paths(s, a, b, l, l_c, input_color, C, cnt, a_1):
    adj_nodes = list(s.neighbors(a)) #find adjacent nodes to node a
    #print(a+"'s adjacent nodes"+str(adj_nodes))
    if adj_nodes: #if it has adjacent nodes
        for i in adj_nodes: 
            #print(i)
            if i == b: #the adjacent node is b
                l.append(i)
                l_c.append(s[a][i]['color'])
                #print("num of input color: "+str(l_c.count(input_color)))
                if l_c.count(input_color) > C: #t > C
                    f = open("output.txt", "a+")
                    f.write("path_%d:\n" %cnt)
                    cnt += 1
                    arr = []
                    for j in range(len(l)-1): #create a set of edges, write to output
                        tup = (l[j],l[j+1],l_c[j])
                        arr.append(tup)
                        f.write(l[j]+", "+l[j+1]+"\n")
                    #print(arr)
                    print("color() is "+str(color(arr, input_color, l_c.count(input_color))))
                    print("is_path() is "+str(is_path(arr, a_1, b)))
                    l.remove(i)
                    l_c.remove(s[a][i]['color'])
                else:
                    l.remove(i)
                    l_c.remove(s[a][i]['color'])
                return cnt
    
            elif i in l: #the adjacent node is already visited
                continue
            elif i not in l: #the adjacent node hasn't been visited
                l.append(i)
                #print("add color: "+s[a][i]['color'])
                l_c.append(s[a][i]['color'])
                x = i
                cnt = find_paths(s, x, b, l, l_c, input_color, C, cnt, a_1)
                l.remove(i)
                l_c.remove(s[a][i]['color'])
            else: 
                print("no such path")
                break
        else:
            #print("dead end")
            return cnt
