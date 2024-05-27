N = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(N) ]
ans[-2] = abs(arr[-1] - arr[-2])


for i in range(N-3 , -1 , -1):
    val = arr[i]
    ans[i] = min(ans[i+1] + abs(arr[i+1] - val) , ans[i+2] + abs(arr[i+2] - val) )
   



print(ans[0])