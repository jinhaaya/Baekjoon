import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N) :
    arr.append(list(map(int, sys.stdin.readline().split())))

dict_max = {}
dict_min = {}

def dp_MAX(arr, idx) :
    if len(arr) == 1 :
        if idx == 0 : return arr[0][0]
        elif idx == 1 : return arr[0][1]
        elif idx == 2 : return arr[0][2]
    else :
        if (len(arr)-1, 0) not in dict_max : dict_max[(len(arr)-1, 0)] = dp_MAX(arr[1:], 0)
        if (len(arr)-1, 1) not in dict_max : dict_max[(len(arr)-1, 1)] = dp_MAX(arr[1:], 1)
        if (len(arr)-1, 2) not in dict_max : dict_max[(len(arr)-1, 2)] = dp_MAX(arr[1:], 2)

        if idx == 0 : 
            if (len(arr), 0) not in dict_max :
                dict_max[(len(arr), 0)] = arr[0][idx] + max(dict_max[(len(arr)-1, 0)], dict_max[(len(arr)-1, 1)])
            return dict_max[len(arr), 0]
        elif idx == 1 : 
            if (len(arr), 1) not in dict_max :
                dict_max[(len(arr), 1)] = arr[0][idx] + max(dict_max[(len(arr)-1, 0)], dict_max[(len(arr)-1, 1)], dict_max[(len(arr)-1, 2)])
            return dict_max[(len(arr), 1)]
        elif idx == 2 : 
            if (len(arr), 2) not in dict_max :
                dict_max[(len(arr), 2)] = arr[0][idx] + max(dict_max[(len(arr)-1, 1)], dict_max[(len(arr)-1, 2)])
            return dict_max[(len(arr), 2)]

def dp_MIN(arr, idx) :
    if len(arr) == 1 :
        if idx == 0 : return arr[0][0]
        elif idx == 1 : return arr[0][1]
        elif idx == 2 : return arr[0][2]
    else :
        if (len(arr)-1, 0) not in dict_min : dict_min[(len(arr)-1, 0)] = dp_MIN(arr[1:], 0)
        if (len(arr)-1, 1) not in dict_min : dict_min[(len(arr)-1, 1)] = dp_MIN(arr[1:], 1)
        if (len(arr)-1, 2) not in dict_min : dict_min[(len(arr)-1, 2)] = dp_MIN(arr[1:], 2)

        if idx == 0 : 
            if (len(arr), 0) not in dict_min :
                dict_min[(len(arr), 0)] = arr[0][idx] + min(dict_min[(len(arr)-1, 0)], dict_min[(len(arr)-1, 1)])
            return dict_min[len(arr), 0]
        elif idx == 1 : 
            if (len(arr), 1) not in dict_min :
                dict_min[(len(arr), 1)] = arr[0][idx] + min(dict_min[(len(arr)-1, 0)], dict_min[(len(arr)-1, 1)], dict_min[(len(arr)-1, 2)])
            return dict_min[(len(arr), 1)]
        elif idx == 2 : 
            if (len(arr), 2) not in dict_min :
                dict_min[(len(arr), 2)] = arr[0][idx] + min(dict_min[(len(arr)-1, 1)], dict_min[(len(arr)-1, 2)])
            return dict_min[(len(arr), 2)]


print(max(dp_MAX(arr, 0), dp_MAX(arr, 1), dp_MAX(arr, 2)), end = " ")
del dict_max
print(min(dp_MIN(arr, 0), dp_MIN(arr, 1), dp_MIN(arr, 2)))
del dict_min