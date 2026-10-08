def knapsack_01(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i, item in enumerate(items, 1):
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]
            if item["weight"] <= c:
                dp[i][c] = max(
                    dp[i][c],
                    item["value"] + dp[i - 1][c - item["weight"]]
                )
    selected, c = [], capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            selected.append(items[i - 1])
            c -= items[i - 1]["weight"]
    selected.reverse()
    return dp[n][capacity], selected
