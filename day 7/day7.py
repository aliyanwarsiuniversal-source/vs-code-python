numbers = [10,20,30,67,50]
print(numbers)
total=0
for num in numbers:
    total=total+num
print(total)
average = total/5
print(average)
#task2
numbers = [10,20,30,67,50]
largest=0 
for num in numbers:
    if num > largest:
        largest=num
print(largest)
#task3
secret = "warsi175"
guess=input("enter password: ")
if guess == secret: 
    print("Access Granted")
else:
    print("access denied")