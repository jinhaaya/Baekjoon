import sys

class Node:
    def __init__(self, alphabet):
        self.data = alphabet
        self.left_child = None
        self.right_child = None

n = int(sys.stdin.readline())
nodes = [Node(chr(i+65)) for i in range(n)] # nodes[0] = A, nodes[1] = B, ...

for _ in range(n) :
    s, l, r = map(str, sys.stdin.readline().split())
    if l != '.' :
        nodes[ord(s)-65].left_child = nodes[ord(l)-65]
        # print(f"{nodes[ord(s)-65].data} left child : {nodes[ord(l)-65].data}")
    if r != '.' :
        nodes[ord(s)-65].right_child = nodes[ord(r)-65]
        # print(f"{nodes[ord(s)-65].data} right child : {nodes[ord(r)-65].data}")

def preorder(node) :
    print(node.data, end = "")
    if node.left_child != None :
        preorder(node.left_child)
    if node.right_child != None :
        preorder(node.right_child)

def inorder(node) :
    if node.left_child != None :
        inorder(node.left_child)
    print(node.data, end = "")
    if node.right_child != None :
        inorder(node.right_child)

def postorder(node) :
    if node.left_child != None :
        postorder(node.left_child)
    if node.right_child != None :
        postorder(node.right_child)
    print(node.data, end = "")

preorder(nodes[0])
print("")
inorder(nodes[0])
print("")
postorder(nodes[0])
print("")