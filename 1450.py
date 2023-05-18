import sys

N, C = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))

def knapsack(weight, C) :
    if len(weight) == 0 :
        return 1
    elif len(weight) == 1 :
        if weight[0] > C :
            return 1
        else :
            return 2
    else :
        if weight[0] > C :
            return 1
        else :
            return knapsack(weight[1:], C-weight[0]) + knapsack(weight[1:], C)


weight.sort(reverse=True)
print(knapsack(weight, C))