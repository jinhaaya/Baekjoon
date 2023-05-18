import sys

m = int(sys.stdin.readline())
f = list(map(int, sys.stdin.readline().split()))
f.insert(0, 0)

f_list = {}
for i in range(1, m + 1):
    f_list[i] = [[i]]

for i in range(1, m + 1):
    f_set = set(f_list[i][0]) # create a set for faster membership testing
    while True:
        f_next = f[f_list[i][0][-1]]
        if f_next in f_set:
            f_list[i].append(f_list[i][0][f_list[i][0].index(f_next):])
            break
        else:
            f_list[i][0].append(f_next)
            f_set.add(f_next)

Q = int(sys.stdin.readline())
for _ in range(Q):
    n, x = map(int, sys.stdin.readline().split())
    if n < len(f_list[x][0]):
        print(f_list[x][0][n])
    else:
        print(f_list[x][1][(n - len(f_list[x][0])) % len(f_list[x][1])])
