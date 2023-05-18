import sys

class Node:
    def __init__(self, num):
        self.data = num
        self.parent = self
        self.depth = 0

    def union(self, other):
        self.root().parent = other.root()

    def root(self):
        temp = self
        while temp.data != temp.parent.data:
            temp = temp.parent
        return temp
    
    def parent_list(self):
        temp_list = [self.data]
        temp = self
        while temp.data != temp.parent.data:
            temp = temp.parent
            temp_list.append(temp.data)
        return temp_list


T = int(sys.stdin.readline())
for testcase in range(T) :
    N = int(sys.stdin.readline())

    # Creaining Nodes
    nodes = [None]
    for n in range(N) :
        nodes.append(Node(n+1))

    # Link child and parent
    for n in range(N-1) :
        A, B = map(int, sys.stdin.readline().split())
        nodes[B].parent = nodes[A]
    
    A, B = map(int, sys.stdin.readline().split())
    A_parent_list = nodes[A].parent_list()
    B_parent_list = nodes[B].parent_list()
    for a in A_parent_list :
        if a in B_parent_list :
            print(a)
            break
