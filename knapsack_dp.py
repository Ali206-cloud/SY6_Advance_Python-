def bottom_up(w, v, c):
    dp = [0] * (c + 1)
    for i in range(len(w)):
        for j in range(c, w[i] - 1, -1):
            dp[j] = max(dp[j], v[i] + dp[j - w[i]])
    return dp[c]


def top_down(w, v, c, memo={}):
    if c == 0 or not w:
        return 0
    if (len(w), c) in memo:
        return memo[(len(w), c)]

    if w[-1] > c:
        ans = top_down(w[:-1], v[:-1], c, memo)
    else:
        ans = max(
            v[-1] + top_down(w[:-1], v[:-1], c-w[-1], memo),
            top_down(w[:-1], v[:-1], c, memo)
        )

    memo[(len(w), c)] = ans
    return ans


# Input
n = int(input("Number of items: "))
w = list(map(int, input("Weights: ").split()))
v = list(map(int, input("Values: ").split()))
c = int(input("Capacity: "))

print("Bottom-Up:", bottom_up(w, v, c))
print("Top-Down:", top_down(w, v, c))
