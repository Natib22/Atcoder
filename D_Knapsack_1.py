x , amount= map(int, input().split())

weight = []
value = []
for _ in range(x):
    input1, input2 = map(int, input().split())
    weight.append(input1)
    value.append(input2)


dp = [[0 for i in range(amount + 1)] for j in range(x + 1)]


for i in range(1 , x+1):
    for j in range(amount + 1):
        wei , val = weight[i-1] , value[i-1]
        if wei <= j:
            dp[i][j] = max(val + dp[i-1][j-wei] , dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[x][amount])
