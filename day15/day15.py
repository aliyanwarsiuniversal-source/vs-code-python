def count_dangers(distances):
    danger_count=0
    for distance in distances:
        if distance <=10:
            danger_count +=1
    return danger_count
obstacles_distance=[12,4,18,9,25,3]
result=count_dangers(obstacles_distance)
print(result)

#TASK 2
numbers = [4, 12, 7, 18, 10, 3]
small_count=0
large_count=0
for number in numbers:
    if number <= 10:
        print("SMALL NUMBERS")
        small_count += 1
    else:
        large_count += 1
        print("LARGE Number")

    print("small number:", small_count)
    print("large number:", large_count)
    print("Total numbers:", len(numbers))

#TASK 3

numbers = [3, 8, 10, 15, 20, 25, 30, 5]

small_count = 0
medium_count = 0
large_count = 0

for number in numbers:

    if number <= 10:
        print("SMALL NUMBER")
        small_count += 1

    elif number <= 20:
        print("MEDIUM NUMBER")
        medium_count += 1

    else:
        print("LARGE NUMBER")
        large_count += 1

print()
print("FINAL REPORT")

print("Small numbers:", small_count)
print("Medium numbers:", medium_count)
print("Large numbers:", large_count)
print("Total numbers:", len(numbers))

#Task 4


   


    
