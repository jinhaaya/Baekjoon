import sys
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for b in B :
    mid = len(A) // 2
    left = 0
    right = len(A)-1

    if A[-1] == b :
        print(1)
        continue

    elif right <= 4 :
        if b in A : print(1)
        else : print(0)
        continue

    while True :
        if A[mid] == b :
            print(1)
            break
        elif right - left <= 1 and A[left] != b and A[right] != b :
            print(0)
            break
        elif A[mid] > b :
            right = mid - 1
            mid = (left + right) // 2
        else :
            left = mid + 1
            mid = (left + right) // 2
        # print(f"A[{left}]={}")
