N = int(input())

dict = {}

def mat_exp(A, n) :
    if n == 1 :
        dict[1] = A
        return A
    if n in dict : return dict[n]
    if n//2 not in dict : 
        dict[n//2] = mat_exp(A, n//2)
    dict[n] = mat_mul(dict[n//2], dict[n//2])
    if n%2 != 0 :
        dict[n] = mat_mul(dict[n], A)
    return dict[n]


def mat_mul(A, B) :
    res = [[0,0],[0,0]]
    res[0][0] = ((A[0][0]*B[0][0])%1000000007 + (A[0][1]*B[1][0])%1000000007)%1000000007
    res[0][1] = ((A[0][0]*B[0][1])%1000000007 + (A[0][1]*B[1][1])%1000000007)%1000000007
    res[1][0] = ((A[1][0]*B[0][0])%1000000007 + (A[1][1]*B[1][0])%1000000007)%1000000007
    res[1][1] = ((A[1][0]*B[0][1])%1000000007 + (A[1][1]*B[1][1])%1000000007)%1000000007
    return res
    
def cal(A, n) :
    if n%2 == 1 : return 0
    elif n == 2 : return 3
    else : n = n//2
    res1 = mat_exp(A, n-1)
    # return res1[0][0]*3 + res1[0][1]*1
    result = (res1[0][0]*3 % 1000000007 + res1[0][1]*1 % 1000000007) % 1000000007
    if result < 0:
        result += 1000000007
    return result

A = [[4, -1], [1, 0]]

print(cal(A, N))
#print(dict)
