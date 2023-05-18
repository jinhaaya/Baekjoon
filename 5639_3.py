import sys
sys.setrecursionlimit(100000)

array = []
while True :
    try : array.append(int(sys.stdin.readline()))
    except : break

if len(array) == 1 :
    print(array[0])
    exit()

tree = {}
tree[array[0]] = [0,0]
for a in array[1:] :
    cur = array[0]
    while True :
        if cur > a :
            if tree[cur][0] == 0 :
                tree[cur][0] = a
                tree[a] = [0,0]
                break
            else :
                cur = tree[cur][0]
        else :
            if tree[cur][1] == 0 :
                tree[cur][1] = a
                tree[a] = [0,0]
                break
            else :
                cur = tree[cur][1]


def postfix(cur_node) :
    if tree[cur_node][0] != 0 :
        postfix(tree[cur_node][0])
    if tree[cur_node][1] != 0 :
        postfix(tree[cur_node][1])
    print(cur_node)
    
postfix(array[0])