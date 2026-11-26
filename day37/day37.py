def count_prices_higher_than_limit(prices,limit):
    count=0

    for price in prices:
        if price > limit:
            count+=1

    return count


prices_a = [100, 250, 400, 150, 300]
prices_b = [50, 50, 50]
prices_c = []

print(count_prices_higher_than_limit(prices_a , 200))
print(count_prices_higher_than_limit(prices_b , 50))
print(count_prices_higher_than_limit(prices_c , 100))