import sys
from collections import deque

r, c, k = map(int, sys.stdin.readline().split())
row = 3; col = 3
A = []
for _ in range(3) : A.append(list(map(int, sys.stdin.readline().split())))

def R():
    global A, row, col
    max_size = 0
    result_list = [[] for _ in range(row)]
    for i, cur_row in enumerate(A) :
        temp_dict = {}
        temp_list = []
        for num in cur_row:
            if num == 0 :
                pass
            elif num in temp_dict:
                temp_dict[num] += 1
            else:
                temp_dict[num] = 1
        for num in temp_dict:
            temp_list.append([num, temp_dict[num]])
        temp_list.sort(key=lambda x : (x[1], x[0]))
        for a, b in temp_list :
            result_list[i].append(a)
            result_list[i].append(b)
        max_size = max(max_size, len(result_list[i]))
    for cur_row in result_list:
        cur_row += [0 for _ in range(max_size - len(cur_row))]

    A = result_list
    col = len(A[0])

    if col > 100:
        for i, v in enumerate(A):
            A[i] = v[:100]
        col = 100

    return

def transpose() :
    global A, row, col
    temp = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            temp[j][i] = A[i][j]
    row, col = col, row
    A = temp

def C():
    global A, row, col

    transpose()
    R()
    transpose()

    row = len(A)

    return

def check():
    global r, c, k, A, row, col
    if r > row or c > col : return False
    elif A[r-1][c-1] == k : return True
    else : return False


for i in range(101):
    # print(f"//{i}//")
    # for a in A:
    #     print(a)
    if check() :
        print(i)
        exit()
    elif row >= col :
        R()
    else :
        C()

print(-1)
