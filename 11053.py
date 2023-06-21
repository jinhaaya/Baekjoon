import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

DP_dict = {N-1 : 1}
def DP(step) :
    if step == N-1 :
        return 1
    if step+1 in DP_dict :
        

