import sys
N = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(N)]
result = 0
stack = []

for a in array :
    # print(f"{a} : {stack} -> ", end = "")
    if not stack :
        pass
    elif a == stack[-1] :
        result += stack.count(a)
        if stack[0] != stack[-1] : result += 1
    elif a < stack[-1] :
        result += 1
    else : 
        result += len(stack)
        while(len(stack) > 0 and a > stack[-1]) :
            stack.pop()
    stack.append(a)
    # print(stack, result)
print(result)