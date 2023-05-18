import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

array = []
while True :
    try : array.append(int(sys.stdin.readline()))
    except : break

if len(array) == 1 :
    print(array[0])
    exit()

root_node = Node(array[0])

for a in array[1:] :
    temp_node = root_node
    while True :
        if a < temp_node.data :
            if temp_node.left_child == None :
                temp_node.left_child = Node(a)
                break
            else : temp_node = temp_node.left_child
        elif a > temp_node.data :
            if temp_node.right_child == None :
                temp_node.right_child = Node(a)
                break
            else : temp_node = temp_node.right_child

def postfix(cur_node) :
    if cur_node.left_child != None :
        postfix(cur_node.left_child)
    if cur_node.right_child != None :
        postfix(cur_node.right_child)
    print(cur_node.data)
    
postfix(root_node)