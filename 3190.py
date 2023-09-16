import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]
# apple = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    board[y-1][x-1] = 2
board[0][0] = 1

L = int(sys.stdin.readline())
direction = ['N']
prev_x = 0
x = 0
for _ in range(L):
    prev_x = x
    x, c = sys.stdin.readline().split()
    x = int(x)
    direction += ['N' for _ in range(x-prev_x-1)]
    if c == 'L':
        direction += ['L']
    elif c == 'D':
        direction += ['D']
second = 0
cur_dir = 1  # 0:up, 1:right, 2:down, 3:left
cur_point = [0, 0]
snake = deque()
snake.append([0, 0])

last = x
while True:
    # print(second, cur_point, cur_dir, direction[second])
    # for i in range(len(board)):print(board[i])
    if second > last:
        pass
    elif direction[second] == 'L':
        cur_dir = (cur_dir-1) % 4
    elif direction[second] == 'D':
        cur_dir = (cur_dir+1) % 4
    second += 1

    if cur_dir == 0:
        cur_point[0] -= 1
    elif cur_dir == 1:
        cur_point[1] += 1
    elif cur_dir == 2:
        cur_point[0] += 1
    elif cur_dir == 3:
        cur_point[1] -= 1
    # print(second, cur_point, cur_dir)
    # print('----------------------')

    if cur_point[0] < 0 or cur_point[0] >= N or cur_point[1] < 0 or cur_point[1] >= N:
        print(second)
        exit()
    elif board[cur_point[0]][cur_point[1]] == 1:
        print(second)
        exit()
    else:
        if board[cur_point[0]][cur_point[1]] != 2:
            y, x = snake.popleft()
            board[y][x] = 0
        board[cur_point[0]][cur_point[1]] = 1
        snake.append([cur_point[0], cur_point[1]])

