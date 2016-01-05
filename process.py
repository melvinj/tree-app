import json
import copy

"""
Script to hold all functionality required to process the json tree

Supported APIs: getList

TODO(melvin): Provide an API to modify the tree based on a request
"""

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

# Does dfs with spouse and children both
def dfs2(family, start, visited=None):
    global c
    #print "Count: %d, node: %s" %(c, start['name'])
    c += 1
    if visited is None:
        print "None here"
        visited = []
    visited.append(start['name'])
    if 'children' in start:
        # get spouse and do dfs
        spouse = start['children'][0]
        child = spouse['children'][0]
        dfs2(family, child, visited)
        # check if children exist and do dfs
        if len(start['children']) == 2:
            current = start['children'][1]
            for child in current['children']:
                dfs2(family, child, visited)
    return visited 

def dfs3(family, start, name, visited=None):
    global c
    c += 1
    if visited is None:
        print "None here"
        visited = []
    if start['name'] == name:
        print "Here "
        modfifyObject(family, )
        return family
    visited.append(start['name'])
    if 'children' in start:
        # get spouse and do dfs
        spouse = start['children'][0]
        child = spouse['children'][0]
        dfs3(family, child, name, visited)
        # check if children exist and do dfs
        if len(start['children']) == 2:
            current = start['children'][1]
            for child in current['children']:
                dfs3(family, child, name, visited)

# returns a list of all names in the tree
def getList(filename):
    Fjson = open(filename, 'r')

    family = json.load(Fjson)
    vis1 = []
    dfs2(family, family, vis1)
    
    return vis1


l = getList('family.json')
print len(l)
print l

# returns the object denoted by the given name in the json
def getObjectForName(filename, name):
    Fjson = open(filename, 'r')

    family = json.load(Fjson)
    vis1 = []

    n = dfs3(family, family, name, vis1)
    print "Node here ", n
    print family


getObjectForName('family.json', 'Kevin Chandran')
