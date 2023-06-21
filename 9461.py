import sys
T = int(sys.stdin.readline())


DP_dict = {1:1, 2:1, 3:1}
def DP(n) :
    if n <= 3 : return 1
    else : 
        if n-2 not in DP_dict : DP_dict[n-2] = DP(n-2)
        if n-3 not in DP_dict : DP_dict[n-3] = DP(n-3)
        return DP_dict[n-2]+DP_dict[n-3]

for _ in range(T) : print(DP(int(sys.stdin.readline())))