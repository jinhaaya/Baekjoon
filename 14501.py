import sys

N = int(sys.stdin.readline())
T = []
P = []
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t); P.append(p)

memo = [-1 for _ in range(N)]

def DP(cur_day):
    global T, P
    if cur_day >= N:
        return 0
    if memo[cur_day] != -1:
        return memo[cur_day]
    elif cur_day + T[cur_day] > N:
        memo[cur_day] = DP(cur_day+1)
    else:
        memo[cur_day] = max(P[cur_day] + DP(cur_day+T[cur_day]), DP(cur_day+1))
    return memo[cur_day]

print(DP(0))