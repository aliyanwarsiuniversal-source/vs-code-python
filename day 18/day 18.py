#Task 1 —                        Passing and Failing Score Counters
scores=[45,60,72,38,90,50,29,65]
pass_count=0
fail_count=0
for score in scores:
    if score >=50:
        print(" YOU ARE PASS")
        pass_count+=1
    else:
        print("YOU ARE FAIL")
        fail_count+=1

total=len(scores)
print("pass count:",pass_count)
print("fail count:",fail_count)
print("TOTAL count:",total)

# Task 2 —                     Find the Highest Score Without max()
scores = [45, 60, 72, 38, 90, 50, 29, 65]

highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print("Highest score:", highest_score)

#TASK 3              Functions, Parameters, return, for loops, Running Totals, Highest-Value Tracking, and len()

numbers = [12, 5, 23, 8, 17, 3]

def analyze_numbers(numbers):
    total_sum = 0
    highest_number = numbers[0]

    for number in numbers:
        total_sum += number

        if number > highest_number:
            highest_number = number

    count = len(numbers)

    return total_sum, highest_number, count


total, highest, count = analyze_numbers(numbers)

print("Total sum:", total)
print("Highest number:", highest)
print("Count of numbers:", count)

#TASK 4                  Autonomous-Car Distance Monitoring System


distances = [3, 7, 12, 18, 4, 25, 9, 15, 2, 30]

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


very_close, close, safe, total = analyze_distances(distances)

print("VERY CLOSE:", very_close)
print("CLOSE:", close)
print("SAFE:", safe)
print("TOTAL DISTANCES:", total)
