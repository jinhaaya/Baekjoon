import sys

T = int(sys.stdin.readline())
for t in range(T) :
    N = int(sys.stdin.readline())
    dic = {}
    sum_nums = 0
    for _ in range(N) :
        Ai = int(sys.stdin.readline())
        if Ai in dic and dic[Ai] == 1 :
            dic[Ai] = 0
            sum_nums -= 1
        else :
            dic[Ai] = 1
            sum_nums += 1
    print(dic)
    print(f"#{t+1} {sum_nums}")


