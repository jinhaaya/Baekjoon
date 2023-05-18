N = int(input())
dict = {}
dict[0] = 1
dict[2] = 3

def dp(n) :
    if n%2 != 0 : return 0
    # dp(n) = dp(n-2) + 2(dp(n-2) + dp(n-4) + ... + dp(0))
    if n-2 in dict : dp_n_2 = dict[n-2]
    else : dp_n_2 = dp(n-2)
    sum_dp = 0
    for i in range(0, n-1, 2) :
        if i in dict : sum_dp += dict[i]
        else : sum_dp += dp(i)
    dict[n] = 2 * sum_dp + dp_n_2
    return dict[n]

print(dp(N))
