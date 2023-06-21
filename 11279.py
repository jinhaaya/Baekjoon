#FAIL

import sys

def insert_sort(array, n) :
    len_array = len(array)
    if len_array == 0: return [n]
    else :
        if n >= array[0] : return [n]+array
        elif n <= array[-1] : return array+[n]
        left = 0
        middle = len_array//2
        right = len_array - 1
        while True :    
            if array[middle] == n :
                array.insert(middle, n)
                return array
            elif array[middle] > n :
                if left+1 >= middle :
                    array.insert(middle, n)
                    return array
                else :
                    right = middle
                    middle = (left+right)//2
            elif array[middle] < n :
                if right-1 <= middle :
                    array.insert(middle+1, n)
                    return array
                else :
                    left = middle
                    middle = (left+right)//2
            


N = int(sys.stdin.readline())
array = []
for _ in range(N) :
    n = int(sys.stdin.readline())

    if n == 0 :
        if not array : print(0)
        else : print(array.pop(0))
    else :
        array = insert_sort(array, n)
