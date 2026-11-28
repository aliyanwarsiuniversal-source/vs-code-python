def delivery_fee(bill):
    if bill > 1000:
        return 0
    else:
        return 100


def final_bill(bill):
    fee=delivery_fee(bill)
    total=bill+fee
    return total

print(final_bill(1200))
print(final_bill(800))
print(final_bill(1000))