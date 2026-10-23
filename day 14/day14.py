#TASK 1s
def square_number(a,b):
    return a *a,b*b

result = square_number(5,3)
print(result)

#TASK 2
def addition_number(a,b):
    return a+b

result= addition_number(10,5)
print(result)

#TASK 3
list_number=[5,8,12,15,20]
for num in list_number:
    if num <10:
        print("SAMLL NUMBER")
    else:
        print("LARGE NUMBER")

#TASK 4
distances = [5, 8, 10, 14, 20, 3, 12, 7]
very_close_count = 0
close_count = 0
safe_count = 0
print("DISTANCE MONITORING REPORT")

for distance in distances:

    if distance <= 5:
        print("VERY CLOSE!")
        very_close_count += 1

    elif distance <= 10:
        print("CLOSE!")
        close_count += 1

    else:
        print("SAFE DISTANCE")
        safe_count += 1

print()
print("FINAL REPORT")

print("Total distances checked:", len(distances))
print("Very close distances:", very_close_count)
print("Close distances:", close_count)
print("Safe distances:", safe_count)
s
