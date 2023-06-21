import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
OKS = [-1 for _ in range(N)]
stack = [A[-1]]
for i in range(N-2, -1, -1) :
    # print(A[i], stack)
    if A[i] == stack[-1] :
        if len(stack) == 1 : pass
        else : OKS[i] = stack[-2]
    elif A[i] < stack[-1] :
        OKS[i] = stack[-1]
        stack.append(A[i])
    elif A[i] > stack[-1] :
        while(len(stack) > 0 and A[i] >= stack[-1]) :
            stack.pop()
        stack.append(A[i])
        if len(stack) == 1 : OKS[i] = -1
        else : OKS[i] = stack[-2]

for oks in OKS :
    print(oks, end = " ")
print("")