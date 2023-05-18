import sys
sys.setrecursionlimit(2000000)

A, B = map(int, sys.stdin.readline().split())

queue = []

def BFS(num_and_rank) :
    cur_num = num_and_rank[0]
    rank = num_and_rank[1]

    if cur_num == B :
        print(rank)
        exit()

    if cur_num * 2 <= B :
        queue.insert(0, [cur_num * 2, rank+1])
    if cur_num * 10 + 1 <= B :
        queue.insert(0, [cur_num * 10 + 1, rank+1])
    # print(cur_num, queue)

    if len(queue) == 0 :
        print(-1)
        exit()

    BFS(queue.pop())

BFS([A, 1])