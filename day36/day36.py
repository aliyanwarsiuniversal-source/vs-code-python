def count_above_average(prices):
    if len(prices) == 0:
        return 0

    total = 0
    count = 0

    for price in prices:
        total += price

    average = total / len(prices)

    for price in prices:
        if price > average:
            count += 1

    return count


prices_a = [100, 200, 300]
prices_b = [50, 50, 50]
prices_c = []

print(count_above_average(prices_a))
print(count_above_average(prices_b))
print(count_above_average(prices_c))

    