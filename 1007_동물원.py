#동물원
#https://www.acmicpc.net/problem/1309
import sys
sys.stdin = open("input.txt","r")
n=int(input())
dp=[[0]*3 for _ in range(n+1)]
dp[1][0],dp[1][1],dp[1][2]=1,1,1
mod=9901
for i in range(2,n+1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2])%mod
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2])%mod
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1])%mod
print(sum(dp[n])%mod)
