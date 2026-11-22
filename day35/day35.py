def average_price(prices):
    if len(prices) == 0:
        return 0

    total = 0

    for price in prices:
        total += price

    return total / len(prices)


prices_a = [250, 80, 400, 80, 150]
prices_b = [0, 500, 99, 100]
prices_c = []

print(average_price(prices_a))
print(average_price(prices_b))
print(average_price(prices_c))