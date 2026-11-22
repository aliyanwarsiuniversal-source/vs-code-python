prices_a = [250, 80, 400, 80, 150]
prices_b = [0, 500, 99, 100]

def summarize_prices(prices):
    cheapest=prices[0]
    highest=prices[0]
    expensive_count=0
    total=0

    for price in prices:
        if price < cheapest:
            cheapest=price

        if price > highest:
            highest=price

        if price >=100:
            expensive_count+=1

        total += price

    return cheapest,highest,expensive_count,total,len(prices)

results_a=summarize_prices(prices_a)
results_b=summarize_prices(prices_b)

print("LIST A:",)
print("CHEAPEST:",results_a[0])
print("HIGHEST:",results_a[1])
print("EXPENSIVE COUNT:",results_a[2])
print("TOTAL:",results_a[3])
print("COUNT OF PRICES:",results_a[4])


print("\nLIST B:",)
print("CHEAPEST:",results_b[0])
print("HIGHEST:",results_b[1])
print("EXPENSIVE COUNT:",results_b[2])
print("TOTAL:",results_b[3])
print("COUNT OF PRICES:",results_b[4])


