# 0/1 Knapsack - Bottom-Up and Top-Down DP

# Items
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50


# -------------------------
# 1. Bottom-Up Approach
# -------------------------
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # dp[i][w] = maximum value using first i items
    # with weight capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# -------------------------
# 2. Top-Down Approach
# -------------------------
def knapsack_top_down(weights, values, capacity):
    n = len(weights)

    # Memoization table
    memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

    def solve(i, w):
        # No items or no capacity
        if i == 0 or w == 0:
            return 0

        # Already calculated
        if memo[i][w] != -1:
            return memo[i][w]

        # If item is too heavy, don't select it
        if weights[i - 1] > w:
            memo[i][w] = solve(i - 1, w)

        else:
            # Maximum of selecting or not selecting the item
            select = values[i - 1] + solve(
                i - 1, w - weights[i - 1]
            )

            not_select = solve(i - 1, w)

            memo[i][w] = max(select, not_select)

        return memo[i][w]

    return solve(n, capacity)


# -------------------------
# Main Program
# -------------------------

bottom_up_result = knapsack_bottom_up(
    weights, values, capacity
)

top_down_result = knapsack_top_down(
    weights, values, capacity
)

print("Bottom-Up DP Result:", bottom_up_result)
print("Top-Down DP Result:", top_down_result)
