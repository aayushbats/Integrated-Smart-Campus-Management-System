def matrix_chain_cost(dimensions):
    n = len(dimensions) - 1
    if n <= 1:
        return 0, []
    dp = [[0] * n for _ in range(n)]
    split = [[None] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = (
                    dp[i][k] + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )
                if cost < dp[i][j]:
                    dp[i][j], split[i][j] = cost, k
    return dp[0][n - 1], split
