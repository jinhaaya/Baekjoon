import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
cost = [[0,0,0]]
cost_dict = {}
for _ in range(N) :
    cost.append(list(map(int, sys.stdin.readline().split())))

# recent_color : 0(red) 1(green) 2(blue)

def DP(cur_color, depth) :
    global cost

    cur_cost = cost[depth][cur_color]

    if depth == N-1 :
        if cur_color == 0 : return cur_cost + min(cost[-1][1], cost[-1][2])
        elif cur_color == 1 : return cur_cost + min(cost[-1][0], cost[-1][2])
        elif cur_color == 2 : return cur_cost + min(cost[-1][0], cost[-1][1])
        
    else :
        if cur_color == 0 :
            if (depth+1, 1) not in cost_dict :
                cost_dict[(depth+1, 1)] = DP(1, depth+1)
            if (depth+1, 2) not in cost_dict :
                cost_dict[(depth+1, 2)] = DP(2, depth+1)
            return cur_cost + min(cost_dict[(depth+1, 1)], cost_dict[(depth+1, 2)])
        elif cur_color == 1 :
            if (depth+1, 0) not in cost_dict :
                cost_dict[(depth+1, 0)] = DP(0, depth+1)
            if (depth+1, 2) not in cost_dict :
                cost_dict[(depth+1, 2)] = DP(2, depth+1)
            return cur_cost + min(cost_dict[(depth+1, 0)], cost_dict[(depth+1, 2)])
        elif cur_color == 2 :
            if (depth+1, 0) not in cost_dict :
                cost_dict[(depth+1, 0)] = DP(0, depth+1)
            if (depth+1, 1) not in cost_dict :
                cost_dict[(depth+1, 1)] = DP(1, depth+1)
            return cur_cost + min(cost_dict[(depth+1, 0)], cost_dict[(depth+1, 1)])

print(min(DP(0, 0), DP(1, 0), DP(2, 0)))