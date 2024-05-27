text1 = input()
text2 = input()
dp = [[0 for j in range(len(text2)+1)] for j in range(len(text1) + 1)]
for i in range(len(text1)-1, -1, -1):
    for j in range(len(text2)-1 ,-1, -1):
        if text1[i] == text2[j]:
            dp[i][j] = 1 + dp[i+1][j+1]
        else:
            dp[i][j] = max(dp[i+1][j] , dp[i][j+1])

i, j = 0 , 0
lcs = []


while i < len(text1) and j < len(text2):
    if text1[i] == text2[j]:
        lcs.append(text1[i])
        i+=1
        j+=1
    elif dp[i][j+1] >= dp[i+1][j]:
        j+=1
    else:
        i+=1


print(''.join(lcs))
        