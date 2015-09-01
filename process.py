import json



c = 0

def dfs(family, start, visited=None):
    global c
    #print "Count: %d, node: %s" %(c, start['name'])
    c += 1
    if visited is None:
        print "None here"
        visited = []
    visited.append(start['name'])
    if 'children' in start and len(start['children']) == 2:
        current = start['children'][1]
        for child in current['children']:
            dfs(family, child, visited)
    return visited 


#print family
def getList(filename):
    Fjson = open(filename, 'r')

    family = json.load(Fjson)
    vis1 = []
    dfs(family, family, vis1)
    
    return vis1

#print getList()
