import sys

command = {'push_front':0, 'push_back':1, 'pop_front':2, 'pop_back':3, 'size':4, 'empty':5, 'front':6, 'back':7}

N = int(sys.stdin.readline())
deque = []
for _ in range(N) :
    line = list(map(str, sys.stdin.readline().split()))
    op = command[line[0]]
    try : num = int(line[1])
    except : pass

    if op == 0 : deque.insert(0, num)
    elif op == 1 : deque.append(num)
    elif op == 2 : 
        if not deque : print(-1)
        else : print(deque.pop(0))
    elif op == 3 : 
        if not deque : print(-1)
        else : print(deque.pop())
    elif op == 4 : print(len(deque))
    elif op == 5 : 
        if deque : print(0)
        else : print(1)
    elif op == 6 :
        if not deque : print(-1)
        else : print(deque[0])
    elif op == 7 :
        if not deque : print(-1)
        else : print(deque[-1])
    print(line[0], deque)