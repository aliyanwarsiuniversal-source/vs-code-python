#Task 1:                           Score Classification
scores=[35,50,68,42,90,25,75,50,61]
pass_count=0
fail_count=0
for score in scores:
    if score >=50:
        pass_count+=1
    else:
        fail_count+=1
total_count=len(scores)
print("pass:",pass_count)
print("fail:",fail_count)
print("TOTAL:",total_count)

#Task 2:                 Find the Highest and Lowest Values
numbers=[14,5,28,9,3,21,7]
highest=numbers[0]
lowest=numbers[0]
for number in numbers:
    if number > highest:
        highest=number

    if number in numbers:
        lowest=number
print("HIGHEST NUMBER:",highest)
print("LOWEST NUMBER:",lowest)

#Task 3:                 Return Multiple Results
numbers = [12, 5, 23, 8, 17, 3]
def analyze_numbers(numbers):
    total_sum=0
    highest=number[0]
    lowest=number[0]
    for number in numbers:
        total_sum+=number
        if number>highest:
            highest=number

        if number<lowest:
            lowest=number
    count=len(number)
    return total_sum,highest,lowest,count

total_sum,highest,lowest,count=analyze_numbers(numbers)
print("TOTAL SUM:",total_sum)
print("HIGEST NUMBER:",highest)
print("LOWSET NUMBER:",lowest)
print("count:",count)

#Task 4:                Autonomous-Car Distance Analysis
distances = [5, 12, 3, 18, 15, 2, 9, 25, 5, 14]

def analyze_distances(distances):
    very_close_count = 0
    close_count = 0
    safe_count = 0

    for distance in distances:
        if distance <= 5:
            very_close_count += 1
        elif distance <= 15:
            close_count += 1
        else:
            safe_count += 1

    total_count = len(distances)

    return very_close_count, close_count, safe_count, total_count


very_close_count, close_count, safe_count, total_count = analyze_distances(distances)

print("Very close:", very_close_count)
print("Close:", close_count)
print("Safe:", safe_count)
print("Total distances:", total_count)