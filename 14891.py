import sys
from collections import deque

wheel = [list(sys.stdin.readline()) for _ in range(4)]
for i in range(4):
    for j in range(8):
        wheel[i][j] = int(wheel[i][j])
    wheel[i] = deque(wheel[i])
wheel = deque(wheel)


for i in range(4):
    wheel[i].pop()
K = int(sys.stdin.readline())
rotate = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

def rotation(num, dir): # rotate 1 tick
    global wheel
    if dir == 1:
        wheel[num].appendleft(wheel[num].pop())
    else:
        wheel[num].append(wheel[num].popleft())

def NS(a, b):
    global wheel
    if wheel[a][2] != wheel[b][6]: return True
    else: return False

def rotate_2(num, dir): # find which wheel to rotate
    global wheel
    result = [[num, dir]]

    if num == 0:
        if NS(0, 1):
            result.append([1,-dir])
            if NS(1, 2):
                result.append([2, dir])
                if NS(2, 3):
                    result.append([3, -dir])
    elif num == 1:
        if NS(0, 1):
            result.append([0, -dir])
        if NS(1, 2):
            result.append([2, -dir])
            if NS(2, 3):
                result.append([3, dir])
    elif num == 2:
        if NS(1, 2):
            result.append([1, -dir])
            if NS(0, 1):
                result.append([0, dir])
        if NS(2, 3):
            result.append([3, -dir])
    if num == 3:
        if NS(2, 3):
            result.append([2, -dir])
            if NS(1, 2):
                result.append([1, dir])
                if NS(0, 1):
                    result.append([0, -dir])
    return result

for num, dir in rotate:
    num -= 1
    for num_2, dir_2 in rotate_2(num, dir):
        rotation(num_2, dir_2)
score = wheel[0][0] + 2*wheel[1][0] + 4*wheel[2][0] + 8*wheel[3][0]
print(score)