def resource_allocation(utilities, capacity):
    dp, choice = [0] * (capacity + 1), [0] * (capacity + 1)
    for c in range(1, capacity + 1):
        for r in range(1, min(c, len(utilities) - 1) + 1):
            candidate = utilities[r] + dp[c - r]
            if candidate > dp[c]:
                dp[c], choice[c] = candidate, r
    allocation, c = [], capacity
    while c > 0 and choice[c]:
        r = choice[c]
        allocation.append(r)
        c -= r
    return dp[capacity], allocation
