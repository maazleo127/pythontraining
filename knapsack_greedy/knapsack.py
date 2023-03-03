def fractional_knapsack(capacity, weights, values):
    n = len(weights)
    ratios = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratios.sort(reverse=True)
    total_value = 0

    for ratio, weight, value in ratios:
        if capacity == 0:
            break
        amount = min(weight, capacity)
        total_value += amount * ratio
        capacity -= amount

    return total_value
