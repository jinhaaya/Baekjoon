import sys
from collections import deque

N = int(sys.stdin.readline())
nums = deque(list(map(int, sys.stdin.readline().split())))
ops = deque(list(map(int, sys.stdin.readline().split())))

def cal(a, op, b) :
    if op == 0 : return a+b
    elif op == 1 : return a-b
    elif op == 2 : return a*b
    else : 
        if a < 0 : return -(-a//b)
        else : return a//b


def DFS_max() :
    if len(nums) == 2 :
        return cal(nums[0], ops.index(1), nums[1])
    else :
        max_val = -1000000001
        for i in range(4) :
            if ops[i] != 0 :
                ops[i] -= 1
                a = nums.popleft()
                b = nums.popleft()
                nums.appendleft(cal(a, i, b))
                max_val = max(max_val, DFS_max())
                nums.popleft()
                nums.appendleft(b)
                nums.appendleft(a)
                ops[i] += 1
        return max_val

def DFS_min() :
    if len(nums) == 2 :
        return cal(nums[0], ops.index(1), nums[1])
    else :
        min_val = 1000000001
        for i in range(4) :
            if ops[i] != 0 :
                ops[i] -= 1
                a = nums.popleft()
                b = nums.popleft()
                nums.appendleft(cal(a, i, b))
                min_val = min(min_val, DFS_min())
                nums.popleft()
                nums.appendleft(b)
                nums.appendleft(a)
                ops[i] += 1
        return min_val

print(DFS_max())
print(DFS_min())