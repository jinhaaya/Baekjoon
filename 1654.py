import sys

def piece(length, lines) :
    num = 0
    for l in lines : num += l//length
    return num


K, N = map(int, sys.stdin.readline().split())
lines = []
for _ in range(K) :
    lines.append(int(sys.stdin.readline()))

length = max(lines)
best_length = 0
left = 1
right = length
mid = (length + 1) // 2
while True :
    left_piece = piece(left, lines)
    mid_piece = piece(mid, lines)
    right_piece = piece(right, lines)
    # print(f"{left}({left_piece}), {mid}({mid_piece}), {right}({right_piece})")
    
    if right_piece >= N :
        best_length = right
        break
    elif mid_piece >= N :
        if mid + 1 >= right :
            best_length = mid
            break
        left = mid
        mid = (left + right) // 2
        continue
    else :
        right = mid
        mid = (left + right) // 2
        continue

print(best_length)