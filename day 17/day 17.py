#TASK 1                               Finding the Highest Score
scores = [45, 78, 92, 67, 88]

highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print("Highest score:", highest)

#TASK 2                              Predicting and Counting Distance Categories
distances = [3, 7, 12, 18, 5, 10, 20, 15, 2, 16]

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

print("VERY CLOSE:", very_close)
print("CLOSE:", close)
print("SAFE:", safe)

#TASK 3                           Find the Lowest Score
scores = [75, 90, 65, 95, 80, 55, 72]
lowest=scores[0]
for score in scores:
    if score<lowest:
        lowest=score

print("LOWEST SCORE:",lowest)

#TASK 4                        Build a List Summary Function
numbers=[12,5,18,7,20,9]
def list_summary(numbers):
    total=sum(numbers)
    smallest=numbers[0]
    count=len(numbers)
    for number in numbers:
        if number < smallest:
            smallest = number

    return total,smallest,count
total,smallest,count=list_summary(numbers)
print("total:",total)
print("smallest number:",smallest)
print("number of items:",count)

#TASK 5                       Car Distance Monitoring System

distances = [5, 8, 10, 14, 20, 3, 12, 7]

def analyze_distances(distances):
    very_close_count = 0
    close_count = 0
    safe_count = 0

    for distance in distances:
        if distance <= 5:
            very_close_count += 1
            print("Emergency braking")

        elif distance <= 15:
            close_count += 1
            print("Slow down, an obstacle is coming")

        else:
            safe_count += 1
            print("Keep driving")

    total_readings = len(distances)

    return very_close_count, close_count, safe_count, total_readings


very_close, close, safe, total = analyze_distances(distances)

print("VERY CLOSE:", very_close)
print("CLOSE:", close)
print("SAFE:", safe)
print("TOTAL READINGS:", total)