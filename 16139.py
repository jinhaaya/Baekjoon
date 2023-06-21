import sys

S = sys.stdin.readline()
q = int(sys.stdin.readline())

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
prefix_sum = {}
len_S = len(S)
for a in alphabet :
    prefix_sum[a] = [0 for _ in range(len_S-1)] # prefix['x'][5] : x in S[0]~S[5]

prefix_sum[S[0]][0] = 1
if len_S > 1 :
    for i, s in enumerate(S[1:-1]) :
        for a in alphabet :
            if a != s :
                prefix_sum[a][i+1] = prefix_sum[a][i]
            else :
                prefix_sum[s][i+1] = prefix_sum[s][i] + 1

for _ in range(q) :
    ch, l, r = map(str, sys.stdin.readline().split())
    if int(l) == 0 : print(prefix_sum[ch][int(r)])
    else : print(prefix_sum[ch][int(r)] - prefix_sum[ch][int(l)-1])