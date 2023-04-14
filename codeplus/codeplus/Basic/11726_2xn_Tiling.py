import sys
input = sys.stdin.readline

def tiling(n):
    dp = [0] * 1001
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    return dp[n]


n = int(input())
print(tiling(n))
