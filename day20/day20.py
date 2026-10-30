#Task 1:                                Score Analysis with a Changed List
scores = [42, 75, 30, 90, 55, 48, 82, 25, 65]

pass_count = 0
fail_count = 0

highest = scores[0]
lowest = scores[0]

for score in scores:

    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

total_scores = len(scores)

print("Passing scores:", pass_count)
print("Failing scores:", fail_count)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total scores:", total_scores)

#Task 2:                                 List Summary Function
numbers=[18,7,25,4,12,30,9]
def analyze_numbers(numbers):
    total=0
    highest=numbers[0]
    lowest=numbers[0]
    count=len(numbers)
    for number in numbers:
        total+=number

        if number> highest:
            highest=number

        if number < lowest:
            lowest=number
    
    return total,highest,lowest,count

total,highest,lowest,count=analyze_numbers(numbers)
print("TOTAL SUM:",total)
print("HIGHEST NUMBER:",highest)
print("LOWEST NUMBER:",lowest)
print("COUNT:",count)

#Task 3:                              corrected the code given too me
scores = [45, 72, 30, 90, 55, 38, 82]

highest = scores[0]
lowest = scores[0]

for score in scores:

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

print("Highest:", highest)
print("Lowest:", lowest)

#Task 4:                           Autonomous-Car Distance Monitor
distances = [5, 12, 3, 18, 15, 2, 9, 25, 5, 14]

def analyze_distances(distances):
    very_close = 0
    close = 0
    safe = 0

    for distance in distances:
        if distance <= 5:
            very_close += 1

        elif distance <= 15:
            close += 1

        else:
            safe += 1

    total = len(distances)

    return very_close, close, safe, total


very_close, close, safe, total = analyze_distances(distances)

print("VERY CLOSE:", very_close)
print("CLOSE:", close)
print("SAFE:", safe)
print("TOTAL:", total)