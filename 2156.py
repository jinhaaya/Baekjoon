import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())

cost = []
for _ in range(N) : cost.append(int(sys.stdin.readline()))
DP_dict = {}

def DP(len_cost) :

    if len_cost == 1 : return cost[-1]
    elif len_cost == 2 : return sum(cost[-2:])
    elif len_cost == 3 : return sum(cost[-3:]) - min(cost[-3:])

    next = []
    if len_cost-1 not in DP_dict : DP_dict[len_cost-1] = DP(len_cost-1)
    if len_cost-2 not in DP_dict : DP_dict[len_cost-2] = DP(len_cost-2)
    if len_cost-3 not in DP_dict : DP_dict[len_cost-3] = DP(len_cost-3)
    next.append(DP_dict[len_cost-1])
    next.append(cost[-len_cost] + DP_dict[len_cost-2])
    next.append(cost[-len_cost] + cost[-len_cost+1] + DP_dict[len_cost-3])
    return max(next)

print(DP(len(cost)))