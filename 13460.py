import sys
from collections import deque
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
board = []
O = []
R = []
B = []
for i in range(N):
    temp = list(sys.stdin.readline())
    board.append(temp[:-1])
    if 'O' in temp:
        O = [i, temp.index('O')]
    if 'R' in temp:
        R = [i, temp.index('R')]
    if 'B' in temp:
        B = [i, temp.index('B')]
board[R[0]][R[1]]='.'
board[B[0]][B[1]]='.'

def mark_rb(r, b):
    global board, O
    board[r[0]][r[1]]='R'
    board[b[0]][b[1]]='B'
    board[O[0]][O[1]]='O'
    return
def remove_rb(r, b):
    global board
    board[r[0]][r[1]]='.'
    board[b[0]][b[1]]='.'
    board[O[0]][O[1]]='O'
    return

def able_direction(r, b):
    result = ['U','R','D','L']
    rU = board[r[0]-1][r[1]]
    bU = board[b[0]-1][b[1]]
    rD = board[r[0]+1][r[1]]
    bD = board[b[0]+1][b[1]]
    rR = board[r[0]][r[1]+1]
    bR = board[b[0]][b[1]+1]
    rL = board[r[0]][r[1]-1]
    bL = board[b[0]][b[1]-1]
    mark_rb(r, b)
    # for k in board:
    #     for j in k:print(j, end="")
    #     print("")
    if (rU != '.' and rU != 'O') and (bU != '.' and bU != 'O'):
        result.remove('U')
    if (rD != '.' and rD != 'O') and (bD != '.' and bD != 'O'):
        result.remove('D')
    if (rR != '.' and rR != 'O') and (bR != '.' and bR != 'O'):
        result.remove('R')
    if (rL != '.' and rL != 'O') and (bL != '.' and bL != 'O'):
        result.remove('L')
    remove_rb(r, b)

    return result

def tilt_one(dir, ball):
    global board, O
    ball_temp = ball.copy()

    if dir == 'U':
        while True:
            if board[ball_temp[0] - 1][ball_temp[1]] == 'O':
                return O
            elif board[ball_temp[0] - 1][ball_temp[1]] == '.':
                ball_temp[0] -= 1
            else:
                return ball_temp
    elif dir == 'D':
        while True:
            if board[ball_temp[0] + 1][ball_temp[1]] == 'O':
                return O
            elif board[ball_temp[0] + 1][ball_temp[1]] == '.':
                ball_temp[0] += 1
            else:
                return ball_temp
    elif dir == 'L':
        while True:
            if board[ball_temp[0]][ball_temp[1] - 1] == 'O':
                return O
            elif board[ball_temp[0]][ball_temp[1] - 1] == '.':
                ball_temp[1] -= 1
            else:
                return ball_temp
    elif dir == 'R':
        while True:
            if board[ball_temp[0]][ball_temp[1] + 1] == 'O':
                return O
            elif board[ball_temp[0]][ball_temp[1] + 1] == '.':
                ball_temp[1] += 1
            else:
                return ball_temp
def tilt(dir, r, b):
    global board
    prev_r, prev_b = r, b
    mark_rb(r, b)
    if dir == 'U':
        if r[0] <= b[0]:
            r = tilt_one(dir, r)
            board[prev_r[0]][prev_r[1]] = '.'
            board[r[0]][r[1]] = 'R'
            if r==O: board[r[0]][r[1]] = 'O'
            b = tilt_one(dir, b)
            board[prev_b[0]][prev_b[1]] = '.'
            board[b[0]][b[1]] = 'B'
            if b==O: board[b[0]][b[1]] = 'O'
        else:
            b = tilt_one(dir, b)
            board[prev_b[0]][prev_b[1]] = '.'
            board[b[0]][b[1]] = 'B'
            if b==O: board[b[0]][b[1]] = 'O'
            r = tilt_one(dir, r)
            board[prev_r[0]][prev_r[1]] = '.'
            board[r[0]][r[1]] = 'R'
            if r==O: board[r[0]][r[1]] = 'O'
    elif dir == 'D':
        if r[0] >= b[0]:
            r = tilt_one(dir, r)
            board[prev_r[0]][prev_r[1]] = '.'
            board[r[0]][r[1]] = 'R'
            if r==O: board[r[0]][r[1]] = 'O'
            b = tilt_one(dir, b)
            board[prev_b[0]][prev_b[1]] = '.'
            board[b[0]][b[1]] = 'B'
            if b==O: board[b[0]][b[1]] = 'O'
        else:
            b = tilt_one(dir, b)
            board[prev_b[0]][prev_b[1]] = '.'
            board[b[0]][b[1]] = 'B'
            if b==O: board[b[0]][b[1]] = 'O'
            r = tilt_one(dir, r)
            board[prev_r[0]][prev_r[1]] = '.'
            board[r[0]][r[1]] = 'R'
            if r==O: board[r[0]][r[1]] = 'O'
    elif dir == 'L':
        if r[1] <= b[1]:
            r = tilt_one(dir, r)
            board[prev_r[0]][prev_r[1]] = '.'
            board[r[0]][r[1]] = 'R'
            if r==O: board[r[0]][r[1]] = 'O'
            b = tilt_one(dir, b)
            board[prev_b[0]][prev_b[1]] = '.'
            board[b[0]][b[1]] = 'B'
            if b==O: board[b[0]][b[1]] = 'O'
        else:
            b = tilt_one(dir, b)
            board[prev_b[0]][prev_b[1]] = '.'
            board[b[0]][b[1]] = 'B'
            if b==O: board[b[0]][b[1]] = 'O'
            r = tilt_one(dir, r)
            board[prev_r[0]][prev_r[1]] = '.'
            board[r[0]][r[1]] = 'R'
            if r==O: board[r[0]][r[1]] = 'O'
    elif dir == 'R':
        if r[1] >= b[1]:
            r = tilt_one(dir, r)
            board[prev_r[0]][prev_r[1]] = '.'
            board[r[0]][r[1]] = 'R'
            if r==O: board[r[0]][r[1]] = 'O'
            b = tilt_one(dir, b)
            board[prev_b[0]][prev_b[1]] = '.'
            board[b[0]][b[1]] = 'B'
            if b==O: board[b[0]][b[1]] = 'O'
        else:
            b = tilt_one(dir, b)
            board[prev_b[0]][prev_b[1]] = '.'
            board[b[0]][b[1]] = 'B'
            if b==O: board[b[0]][b[1]] = 'O'
            r = tilt_one(dir, r)
            board[prev_r[0]][prev_r[1]] = '.'
            board[r[0]][r[1]] = 'R'
            if r==O: board[r[0]][r[1]] = 'O'

    remove_rb(r, b)
    return r, b


Q = deque()
def BFS(D, R, B):
    # termination condition
    if R == O and B != O:
        print(D)
        exit()
    if D >= 11:
        print(-1)
        exit()

    for dir in able_direction(R, B):
        temp_R, temp_B = tilt(dir, R, B)
        if temp_B == O: continue
        if [D, temp_R, temp_B] in Q: continue
        Q.append([D+1, temp_R, temp_B])
    # print("--------")
    # print(R, B, able_direction(R, B))
    # print(Q)
    # print("--------")
    while Q:
        d, r, b = Q.popleft()
        # print(f"d:{d}, R:{R}, B:{B}, r={r}, b={b}")
        # print("-----------")
        BFS(d, r, b)
    print(-1)
    exit()

print(BFS(0, R, B))