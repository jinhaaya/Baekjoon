import sys
sys.setrecursionlimit(100000)

array = []
while True :
    try : array.append(int(sys.stdin.readline()))
    except : break

if len(array) == 1 :
    print(array[0])
    exit()

tree = [0 for _ in range(10002)]
tree[1] = array[0]
for a in array[1:] :
    cur_node = 1
    while True :
        if tree[cur_node] == 0 :
            tree[cur_node] = a
            break
        elif a < tree[cur_node] :
            cur_node *= 2
        elif a > tree[cur_node] :
            cur_node *= 2
            cur_node += 1

def postfix(cur_node) :
    if tree[cur_node*2] != 0 :
        postfix(cur_node*2)
    if tree[cur_node*2+1] != 0 :
        postfix(cur_node*2+1)
    print(tree[cur_node])
    
postfix(1)