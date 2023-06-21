N = int(input())
if N == 1 :
    print(9)
    exit()

dp = [[1 for _ in range(10)] for _ in range(N)] 

for i in range(N-2, -1, -1) :
    dp[i][0] = dp[i+1][1]
    for j in range(1, 9) :
        dp[i][j] = (dp[i+1][j-1] + dp[i+1][j+1]) % 1000000000
    dp[i][9] = dp[i+1][8]

print(sum(dp[0][1:])%1000000000)