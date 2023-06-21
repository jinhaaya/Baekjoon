import sys

N = int(sys.stdin.readline())
stairs = [0] + [int(sys.stdin.readline()) for _ in range(N)]
scores_1 = [0 for _ in range(N+1)]
scores_2 = [0 for _ in range(N+1)]
scores_2[-1] = stairs[-1]

for i in range(N-1, -1, -1) :
    if scores_2[i+1] != 0 :
        scores_1[i] = stairs[i] + scores_2[i+1]
    if i+2 <= N and scores_1[i+2] + scores_2[i+2] != 0 :
        scores_2[i] = stairs[i] + max(scores_1[i+2], scores_2[i+2])

print(max(scores_1[0],scores_1[1], scores_2[0], scores_2[1]))