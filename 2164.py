from collections import deque
N = int(input())

queue = deque()
if N % 2 == 1 :
    queue.append(N)
for i in range(2, N+1-N%2, 2) :
    queue.append(i)

while queue :
    a = queue.popleft()
    if not queue : break
    a = queue.popleft()
    queue.append(a)
print(a)