#TASK 1:
def add_three_numbers(a, b, c):
    total = a + b + c
    return total

answer = add_three_numbers(10, 20, 30)
print(answer)

#Task 2


numbers = [3, 15, 7, 22, 10, 18]

for number in numbers:
    if number > 10:
        print(number)

#Task 2 :

numbers = [12, 5, 27, 9, 18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("The largest number is:", largest)

