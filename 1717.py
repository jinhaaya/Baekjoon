import sys

class Node:
    def __init__(self, num):
        self.data = num
        self.parent = self

    def union(self, other):
        root_a = self.root().data
        root_b = other.root().data
        if root_a != root_b :
            self.root().parent = other.root()

    def root(self):
        temp = self
        while temp.data != temp.parent.data:
            temp = temp.parent
        return temp

n, m = map(int, sys.stdin.readline().split())
nodes = [Node(i) for i in range(n + 1)]

for _ in range(m):
    operator, a, b = map(int, sys.stdin.readline().split())
    if operator == 0:
        nodes[a].union(nodes[b])
    elif operator == 1:
        if nodes[a].root().data == nodes[b].root().data:
            print("YES")
        else:
            print("NO")
