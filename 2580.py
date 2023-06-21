import sys

def possible_num(sudoku, y, x) :
    dup = [0,0,0,0,0,0,0,0,0,0]

    for i in range(9) :
        dup[sudoku[y][i]] = 1
        dup[sudoku[i][x]] = 1

    for i in range((y//3)*3, (y//3)*3+3) :
        for j in range((x//3)*3 ,(x//3)*3+3) :
            dup[sudoku[i][j]] = 1

    result = []
    for i, r in enumerate(dup[1:]) :
        if r == 0 : result.append(i+1)

    return result

def DFS(n) :
    global sudoku
    global empty
    if len(empty) == n :
        for row in sudoku :
            for e in row : print(e, end=" ")
            print("")
        exit()

    y, x = empty[n]
    possible_nums = possible_num(sudoku, y, x)
    if not possible_nums : return

    # for j, i in empty[n:] :
    #     if not possible_num(sudoku, j, i) : return
        
    for p in possible_nums :
        sudoku[y][x] = p
        DFS(n+1)
        sudoku[y][x] = 0

sudoku = []
empty = []
for _ in range(9) : sudoku.append(list(map(int, sys.stdin.readline().split())))
for y in range(9) :
    for x in range(9) :
        if sudoku[y][x] == 0 : empty.append([y, x])

DFS(0)