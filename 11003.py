import sys
from collections import deque
from queue import PriorityQueue

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
D = [0 for _ in range(N+1)]
window_deque = deque()
sorted_queue = PriorityQueue()
minval = 1000000000

for i in range(1, N+1) :
    sorted_queue.put(D[i])

    if i <= L :
        window_deque.append(D[i])
    else : 
        window_deque.append(D[i])
        sorted_queue.  window_deque.popleft()
        
