import sys
import itertools

N = int(sys.stdin.readline())

S = []
for _ in range(N) : S.append(list(map(int, sys.stdin.readline().split())))

def generate_binary_combinations(n):
    if n % 2 != 0:
        return []  # Number of bits should be even

    bits = n // 2
    combinations = []
    
    for combination in itertools.combinations(range(n), bits):
        binary = ['0'] * n
        for index in combination:
            binary[index] = '1'
        combinations.append(''.join(binary))

    return combinations    

combination = generate_binary_combinations(N)

min_val = 1000000
for c in combination :
    a = []; b = []
    for idx, team in enumerate(str(c)) :
        if int(team) == 1 :
            a.append(idx)
        else :
            b.append(idx)

    a_sum = 0
    for idx in range(len(a)) :
        for i in range(idx) :
            a_sum += S[a[i]][a[idx]] + S[a[idx]][a[i]]
    b_sum = 0
    for idx in range(len(b)) :
        for i in range(idx) :
            b_sum += S[b[i]][b[idx]] + S[b[idx]][b[i]]
    
    min_val = min(min_val, abs(a_sum-b_sum))

print(min_val)