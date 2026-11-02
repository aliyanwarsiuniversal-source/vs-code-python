#TASK 1
scores=[45,82,67,30,95,50,73,18,88,60]
total=0
highest=scores[0]
lowest=scores[0]
passing_count=0
failing_count=0
total_students=0
for score in scores:
    total += score
    total_students +=1
    if score > highest:
        highest=score
    if score < lowest:
        lowest=score
    if score >=50:
        passing_count +=1
    else:
        failing_count +=1

average=total/total_students
print("HIGHEST SCORE:",highest)
print("LOWEST SCORE:",lowest)
print("TOTAL:",total)
print("PASSING COUNT:",passing_count)
print("FAILING COUNT:",failing_count)
print("TOTAL STUDENTS:",total_students)
print("AVERAGE:",average)

#TASK 2
def analyze_numbers(numbers):
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

    return total_sum, highest, lowest, positive_count, negative_count, zero_count, total_count


numbers = [14, -8, 0, 25, -3, 10, 0, -12, 6, 18]

reults = analyze_numbers(numbers)

print("TOTAL SUM:", reults[0])
print("HIGHEST:", reults[1])
print("LOWEST:", reults[2])
print("POSITIVE COUNT:", reults[3])
print("NEGATIVE COUNT:", reults[4])
print("ZERO COUNT:", reults[5])
print("TOTAL COUNT:", reults[6])

#TASK 3
distances = [2, 6, 11, 18, 4, 25, 9, 15, 3, 30, 7, 20]

very_close_count = 0
close_count = 0
safe_count = 0
total_count = 0

for distance in distances:
    total_count += 1

    if distance <= 5:
        very_close_count += 1
    elif distance <= 15:
        close_count += 1
    else:
        safe_count += 1

very_close_percentage = (very_close_count / total_count) * 100
close_percentage = (close_count / total_count) * 100
safe_percentage = (safe_count / total_count) * 100

print("VERY CLOSE COUNT:", very_close_count)
print("CLOSE COUNT:", close_count)
print("SAFE COUNT:", safe_count)
print("TOTAL COUNT:", total_count)

print("VERY CLOSE PERCENTAGE:", very_close_percentage, "%")
print("CLOSE PERCENTAGE:", close_percentage, "%")
print("SAFE PERCENTAGE:", safe_percentage, "%")