import sys

string = list(sys.stdin.readline())
string = string[:-1]
stack = []

def postfix(string) :
    result = ''

    for idx, s in enumerate(string) :
        if ord('A') <= ord(s) and ord(s) <= ord('Z') :
            result += s
        elif s == '(' :
            stack.append('(')
        elif s == ')' :
            while True :
                op = stack.pop()
                if op != '(' : result += op
                else : break
        elif s == '*' or s == '/' :
            while True :
                if stack and (stack[-1] == '*' or stack[-1] == '/') :
                    result += stack.pop()
                else : break
            stack.append(s)
        elif s == '+' or s == '-' :
            while True :
                if stack and stack[-1] != '(' :
                    result += stack.pop()
                else :
                    break
            stack.append(s)

    while stack :
        result += stack.pop()
    return result

print(postfix(string))