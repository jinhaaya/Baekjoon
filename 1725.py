import sys

def include_mid(N, len_N) :
    if len_N == 1 : return N[0]

    mid = len_N//2
    left = mid; right = mid
    min_height = N[mid]
    max_val = N[mid]
    width = 1

    while True :
        if right == len_N-1 and left == 0 :
            break

        if left == 0 or (right != len_N-1 and N[left-1] < N[right+1]) :
            right += 1
            width += 1
            min_height = min(min_height, N[right])
        elif right == len_N-1 or (left != 0 and N[left-1] >= N[right+1]) :
            left -= 1
            width += 1
            min_height = min(min_height, N[left])
        max_val = max(max_val, width * min_height)
        # print(N, len_N, left, right, min_height, max_val)
    return max_val

def devide_conquer(N, len_N) :
    if len_N == 1 : return N[0]
    else :
        N_left = N[0:len_N//2]
        N_right = N[len_N//2:]
        return max(include_mid(N, len_N), devide_conquer(N_left, len_N//2), devide_conquer(N_right, len_N-len_N//2))
        

len_N = int(sys.stdin.readline())
N = []
for _ in range(len_N) :
    N.append(int(sys.stdin.readline()))

print(devide_conquer(N, len_N))