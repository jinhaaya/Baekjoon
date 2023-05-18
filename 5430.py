import sys

T = int(sys.stdin.readline())
for _ in range(T) :
    P = sys.stdin.readline()
    N = int(sys.stdin.readline())
    try :
        array =  list(map(int, sys.stdin.readline().replace('[', ',').replace(']', ',').split(',')[1:-1]))
    except :
        array = []

    front_pop = 0
    back_pop = 0

    cur_R_num = 0
    for p in P :
        if p == 'R' : cur_R_num += 1
        elif p == 'D' :
            if cur_R_num%2 == 0 : front_pop += 1
            else : back_pop += 1
    
    if len(array) < front_pop + back_pop : print('error')
    else :
        if cur_R_num%2 == 0 : 
            array = array[front_pop:len(array)-back_pop]
        else :
            array = array[front_pop:len(array)-back_pop]
            array.reverse()
        print('[', end = '')
        for i, a in enumerate(array):
            print(a, end='')
            if i != len(array)-1 : print(',', end='')
        print(']')