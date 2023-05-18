import sys

n = int(sys.stdin.readline())
nums = []
next_push_num = 1
stacks = []
output = []

for _ in range(n) :
    nums.append(int(sys.stdin.readline()))

for num in nums :
    if num in stacks : 
        if stacks[-1] != num : 
            print('NO')
            exit()
        elif stacks[-1] == num :
            stacks.pop()
            output.append('-')
    else :
        while True :
            stacks.append(next_push_num)
            output.append('+')
            if next_push_num == num : 
                next_push_num += 1
                break
            next_push_num += 1
        stacks.pop()
        output.append('-')

for o in output :
    print(o)
