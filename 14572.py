import sys

N, K, D = map(int, sys.stdin.readline().split())
students = []
for _ in range(N) :
    dict = {}
    dict['M'], dict['d'] = map(int, sys.stdin.readline().split())
    dict['A'] = list(map(int, sys.stdin.readline().split()))
    students.append(dict)

students.sort(key=lambda x : x['d'], reverse=False) 

left = 0
right = 0

def efficiency(l, r) :
    algorithm_any = [0] * (K+1)
    algorithm_all = [0] * (K+1)
    for i in range(l, r+1) :
        for a in students[i]['A'] :
            algorithm_any[a] = 1
            algorithm_all[a] += 1
    return (r-l+1) * (algorithm_any.count(1) - algorithm_all.count(r-l+1))

max_efficiency = 0 #efficiency(left, right)
while right <= N-1 :

    if students[right]['d'] - students[left]['d'] > D :
        left += 1
        continue
    while right < N-1 and students[right+1]['d'] - students[left]['d'] <= D :
        right += 1
    # print(f"left : {left}, right : {right}")
    max_efficiency = max(max_efficiency, efficiency(left, right))
    right += 1

print(max_efficiency)
