def shop_bill(prices, limit):
    total = 0

    for price in prices:
        if price > limit:
            amount = price * 0.9
        else:
            amount = price

        total = total + amount

    return total


# Example 1
prices_a = [100, 250, 400, 150, 300]
bill_a = shop_bill(prices_a, 200)
final_a = bill_a + 150
print(final_a)

# Example 2
prices_b = [50, 50]
bill_b = shop_bill(prices_b, 50)
final_b = bill_b + 150
print(final_b)

# Example 3
prices_c = []
bill_c = shop_bill(prices_c, 200)
final_c = bill_c + 150
print(final_c)