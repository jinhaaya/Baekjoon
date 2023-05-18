import sys

str = sys.stdin.readline()
q = int(sys.stdin.readline())
for i in range(q) :
    ch, l, r = sys.stdin.readline().split()
    l = int(l); r = int(r)
    cnt = 0
    for j in range(l, r+1) :
        if str[j] == ch : cnt += 1
    print(cnt)