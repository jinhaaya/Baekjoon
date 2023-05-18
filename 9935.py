import sys

string = sys.stdin.readline()[:-1]
ex_string = sys.stdin.readline()[:-1]
stack = []
result = []

len_ex_string = len(ex_string)
len_stack = 0

for s in string :
    stack.append(s)
    len_stack += 1
    if s == ex_string[-1] and len_stack >= len_ex_string and stack[-len_ex_string:] == list(ex_string) :
        del stack[-len_ex_string:]
        len_stack -= len_ex_string
    elif s not in ex_string :
        result.append(stack)
        stack = []
        len_stack = 0
if result : 
    for r in result : print(f"{r[0]}", end="")
    print("")
else : print('FRULA')