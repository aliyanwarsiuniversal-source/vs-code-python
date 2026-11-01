#TASK 1                             
numbers=[12,-5,0,8,-15,20,-3,0,7]
highest=numbers[0]
lowest=numbers[0]
for number in numbers:
    if number >highest:
        highest=number
    if number < lowest:
        lowest=number

print("HIGHEST NUMBER:",highest)
print("LOWEST NUMBER:",lowest)

#TASK 2:                             

numbers = [14, -8, 0, 25, -3, 10, 0, -12, 6, 18]

total_sum = 0
highest = numbers[0]
lowest = numbers[0]

positive_count = 0
negative_count = 0
zero_count = 0
total_count = 0

for number in numbers:
    total_sum += number
    total_count += 1

    if number > highest:
        highest = number

    if number < lowest:
        lowest = number

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("TOTAL SUM:", total_sum)
print("HIGHEST:", highest)
print("LOWEST:", lowest)
print("POSITIVE COUNT:", positive_count)
print("NEGATIVE COUNT:", negative_count)
print("ZERO COUNT:", zero_count)
print("TOTAL COUNT:", total_count)

#TASK 3       
numbers = [16, -4, 22, 0, 9, -11, 5, 0, 30, -7]
def analyze_numbers(numbers):
    total_sum=0
    highest=numbers[0]
    lowest=numbers[0]
    positive_count=0
    negative_count=0
    zero_count=0
    total_count=0
    for number in numbers:
        total_sum+= number
        total_count +=1
        if number > highest:
            highest=number

        if number < lowest:
            lowest=number

        if number > 0:
            positive_count +=1

        elif number < 0:
            negative_count +=1
        else:
            zero_count +=1
    return total_sum, highest, lowest, positive_count, negative_count, zero_count, total_count

results = analyze_numbers(numbers)

print("TOTAL SUM:", results[0])
print("HIGHEST:", results[1])
print("LOWEST:", results[2])
print("POSITIVE COUNT:", results[3])
print("NEGATIVE COUNT:", results[4])
print("ZERO COUNT:", results[5])
print("TOTAL COUNT:", results[6])
