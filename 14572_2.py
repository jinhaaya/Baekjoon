import sys

N, K, D = map(int, sys.stdin.readline().split())
students = []
for _ in range(N):
    student = {}
    student['M'], student['d'] = map(int, sys.stdin.readline().split())
    student['A'] = list(map(int, sys.stdin.readline().split()))
    students.append(student)

students.sort(key=lambda x: x['d'])  # Sort only once

left = 0
right = 0
max_efficiency = 0
algorithm_any = [0] + [0] * K
algorithm_all = [0] + [0] * K

while right < N:
    # Update algorithm count for new student
    for a in students[right]['A']:
        algorithm_any[a] = 1
        algorithm_all[a] += 1

    # Shrink the window if the constraint is violated
    while students[right]['d'] - students[left]['d'] > D:
        for a in students[left]['A']:
            algorithm_all[a] -= 1
            if algorithm_all[a] == 0:
                algorithm_any[a] = 0
        left += 1

    # Update max_efficiency
    max_efficiency = max(max_efficiency, (right - left + 1) * (algorithm_any.count(1) - algorithm_all.count(right - left + 1)))

    right += 1

print(max_efficiency)
