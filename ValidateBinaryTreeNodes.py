# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import collections
def isFormattedCorrectly(string):
    
    exp = r'\([A-Z],[A-Z]\)'
    
    return re.search(exp, string)
    

    
def bfs(root, parent_to_children, child_to_parent, node_set):
    visited = [0 for i in range(len(node_set))]
    
    visited = set()
    Queue = collections.deque([root])
    
    while Queue :
        temp = Queue.popleft()
        
        visited.add(temp)
        
        for child in parent_to_children[temp]:
            if child in visited:
                print("E5")
                return False
            Queue.append(child)
    
    if len(visited) == len(node_set):
        return True
    else:
        print("E4")
        return False

    
def main(root, parent_to_children, child_to_parent, node_set):
    
    if bfs(root, parent_to_children, child_to_parent, node_set):
        print(build_expression(root, parent_to_children))

    
    

def build_expression(root, parent_to_children):

    if root is None:
        return ""
    
    if len(parent_to_children[root]) == 0:
        return "({})".format(root)
    

    if len(parent_to_children[root]) == 2:

        return "({}{}{})".format(root, build_expression(min(parent_to_children[root]), parent_to_children), build_expression(max(parent_to_children[root]), parent_to_children))
    else:
        return "({}{})".format(root, build_expression(parent_to_children[root][0], parent_to_children))
    


input_string = input()

returned = False
if input_string != input_string.strip():
    returned = True
    print("E1")

input_list = []
if not returned:
    input_list = input_string.split(" ")
    
    for element in input_list:
        if not isFormattedCorrectly(element):
            print("E1")
            returned = True
            break

parent_to_children = collections.defaultdict(list)
child_to_parent ={}
node_set = set()
if not returned:
    
    for t in input_list:
        parent = t.split(",")[0][1]
        child = t.split(",")[1][0]
            
        if child not in parent_to_children[parent]:
            parent_to_children[parent].append(child)
            child_to_parent[child] = parent

            node_set.add(parent)
            node_set.add(child)
        else:
            print("E2")
            returned = True
            break

        if len(parent_to_children[parent]) > 2:
            print("E3")
            returned = True
            break


root = None
if not returned:
    
    for node in node_set:
        
        if not root and parent_to_children[node] and node not in child_to_parent:
            root = node
            continue
        if root and parent_to_children[node] and node not in child_to_parent:
            print("E4")
            returned = True
            break
    

if not returned:
    main(root, parent_to_children, child_to_parent, node_set)