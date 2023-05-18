import sys

M = int(sys.stdin.readline())
S = [0 for _ in range(21)]

for _ in range(M) :
    line = list(map(str,sys.stdin.readline().split()))
    command = line[0]
    try : num = int(line[1])
    except : pass
    
    if command == 'add' :
        S[num] = 1
    elif command == 'remove' :
        S[num] = 0
    elif command == 'check' :
        print(S[num])
    elif command == 'toggle' :
        S[num] = 1-S[num]
    elif command == 'all' :
        S = [1 for _ in range(21)]
    elif command == 'empty' :
        S = [0 for _ in range(21)]
