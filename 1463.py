import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
DP_dict = {}

if N == 1 :
    print(0)
    exit()

def DP(n) :
    if n == 1 :
        return 0

    next_nums = []
    next_val = []
    if n%3 == 0 : next_nums.append(n//3)
    if n%2 == 0 : next_nums.append(n//2)
    if n%6 != 0 : next_nums.append(n-1)

    # print(n, next_nums, depth)

    for next_num in next_nums :
        if next_num not in DP_dict :
            DP_dict[next_num] = DP(next_num)
        next_val.append(DP_dict[next_num])
    del(next_nums)
    return 1+min(next_val)

print(DP(N))