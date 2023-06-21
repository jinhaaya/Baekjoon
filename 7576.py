import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
array = []
queue = deque()
for _ in range(N) : array.append(list(map(int, sys.stdin.readline().split())))
flag = 0
for n in range(N) :
    for m in range(M) :
        if array[n][m] == 1 : 
            queue.append((n, m))
        elif array[n][m] == 0 : 
            flag += 1
if flag == 0 :
    print(0)
    exit()


def BFS() :
    global flag
    while True :
        if not queue : 
            if flag != 0 :
                print(-1)
                exit()
            else :
                result = 0
                for a in array : result = max(result, max(a))
                print(result - 1)
                exit()


        n, m = queue.popleft()
        next = array[n][m] + 1
        
        if n != 0 and array[n-1][m] == 0 :
            array[n-1][m] = next
            flag -= 1
            queue.append((n-1, m))
        if n != N-1 and array[n+1][m] == 0 :
            array[n+1][m] = next
            flag -= 1
            queue.append((n+1, m))
        if m != 0 and array[n][m-1] == 0 :
            array[n][m-1] = next
            flag -= 1
            queue.append((n, m-1))
        if m != M-1 and array[n][m+1] == 0 :
            array[n][m+1] = next
            flag -= 1
            queue.append((n, m+1))

BFS()