import sys
sys.setrecursionlimit(10000)


def init(node, start, end): 
    if start == end :
        tree[node] = nums[start]
        return tree[node]
    else :
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]


def change(node, start, end, idx, diff) :
    if idx < start or idx > end : return
    tree[node] += diff
    if start == end : return
    change(node*2, start, (start+end)//2, idx, diff)
    change(node*2+1, (start+end)//2+1, end, idx, diff)


def sums(node, start, end, left, right) :
    if left > end or right < start :
        return 0
    if left <= start and end <= right :
        return tree[node]
 
    return sums(node*2, start, (start+end)//2, left, right) + sums(node*2 + 1, (start+end)//2+1, end, left, right)


N, M, K = map(int,sys.stdin.readline().split())
nums = []
tree = [0 for _ in range(4*N)]
for _ in range(N): nums.append(int(sys.stdin.readline()))
init(1, 0, N-1)

for _ in range(M+K) :
    a, b, c = map(int,sys.stdin.readline().split())
    if a == 1 :
        b -= 1
        change(1, 0, N-1, b, c-nums[b])
        nums[b] = c
    elif a == 2 :
        print(sums(1, 0, N-1, b-1, c-1))