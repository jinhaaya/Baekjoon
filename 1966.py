import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T) :
    N, M = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    queue = deque()
    for i in range(N) :
        priority = a[i]
        queue.append([i, priority])
    result = 1
    while True :
        max_val = max(queue, key = lambda x : x[1])[1]
        q = queue.popleft()
        if q[1] == max_val :
            if q[0] == M : break
            else : result += 1
        else :
            queue.append(q)
    print(result)
