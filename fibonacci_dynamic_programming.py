def memo(n, dp):
    if n <= 1: return n
    if dp[n] != -1: return dp[n]
    dp[n] = memo(n-1, dp) + memo(n-2, dp)
    return dp[n]

def tab(n):
    dp = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input("Enter n: "))
print("Memoization:", memo(n, [-1]*(n+1)))
print("Tabulation:", tab(n))
