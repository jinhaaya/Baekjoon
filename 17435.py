import sys

m = int(sys.stdin.readline())
f = list(map(int, sys.stdin.readline().split()))
f.insert(0,0)

f_list = {}
for i in range(1, m+1) :
    f_list[i] = [[i]]
# f_list[i] = [[f0(i), f1(i)), f2(i)) .... f7(i)], [f5(i), f6(i), f7(i)]] where f7(i) = f4(i)


for i in range(1, m+1) :
    while True :
        f_next = f[f_list[i][0][-1]]
        if f_next in f_list[i][0] :
            f_list[i].append(f_list[i][0][f_list[i][0].index(f_next):])
            break
        else : f_list[i][0].append(f_next)
# print(f_list)

Q = int(sys.stdin.readline())
for _ in range(Q) :
    n, x = map(int, sys.stdin.readline().split())
    # print(f_list[x][n%len(f_list[x])])
    if n < len(f_list[x][0]) :
        print(f_list[x][0][n])
    else :
        print(f_list[x][1][(n-len(f_list[x][0]))%len(f_list[x][1])])