import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
queue = [i+1 for i in range(N)]
nums = deque(list(map(int, sys.stdin.readline().split())))
result = 0

while nums :
    a = nums.popleft()
    idx = queue.index(a)
    if idx <= len(queue)//2 :
        queue = queue[idx+1:] + queue[:idx]
        result += idx
    else :
        queue =  queue[idx+1:] + queue[:idx]
        result += len(queue) - idx + 1
print(result)