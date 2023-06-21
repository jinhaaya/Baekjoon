import sys

N, C = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))

def knapsack(start, end, C) :
    global weight
    if end-start == 0 :
        if weight[start] > C :
            return 1
        else :
            return 2
    else :
        



weight.sort(reverse=True)
print(knapsack(0, len(weight)-1, C))