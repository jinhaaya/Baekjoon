import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
freq = {}
for a in A :
    if a in freq : freq[a] += 1
    else : freq[a] = 1

NGF = [-1 for _ in range(N)]
stack = [A[-1]]
for i in range(N-2, -1, -1) :
    # print(A[i], stack)
    if freq[A[i]] == freq[stack[-1]] :
        if len(stack) == 1 : 
            stack.pop()
            stack.append(A[i])
        else :
            NGF[i] = stack[-2]
            stack.pop()
            stack.append(A[i])
    elif freq[A[i]] < freq[stack[-1]] :
        NGF[i] = stack[-1]
        stack.append(A[i])
    elif freq[A[i]] > freq[stack[-1]] :
        while len(stack) > 0 and freq[A[i]] >= freq[stack[-1]] :
            stack.pop()
        stack.append(A[i])
        if len(stack) == 1 : NGF[i] = -1
        else : NGF[i] = stack[-2]

for ngf in NGF :
    print(ngf, end = " ")
print("")