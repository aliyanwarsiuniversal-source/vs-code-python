# TASK 1 : functions introductions
def add_numbers (a,b):
    total = a+b
    return total

answer = add_numbers(20,7)
print(answer)
# variation of TASK 1 :    Multiplication
def multiply_numbers(a,b):
    total = a*b 
    return total

answer = multiply_numbers (10,5)
print(answer)

#  variation of TASK 1 :   Subtraction
def subtract_numbers(a,b):
    total=a-b 
    return total

answer= subtract_numbers (90,5)
print(answer) 

#  variation of TASK 1 :   Division
def divide_numbers(a,b):
    total=a/b 
    return total

answer= divide_numbers (60,5)
print(answer) 


# TASK 2: Scope and Arguments Practice

threshold = 10

def check_number(numbers):
    for number in numbers:
        if number > threshold:
            result = "greater than 10"
            print(number, result)
        else:
            result = "10 or less"
            print(number, result)


my_numbers = [5, 12, 8, 20, 3]
check_number(my_numbers)


# TASK 2: Variation 1 - Even and Odd

def check_even_odd(numbers):
    for number in numbers:
        if number % 2 == 0:
            result = "even"
        else:
            result = "odd"

        print(number, result)


my_numbers = [2, 7, 10, 15, 22]
check_even_odd(my_numbers)



# TASK 2: Variation 2 - Pass and Fail

passing_score = 50

def check_scores(scores):
    for score in scores:
        if score >= passing_score:
            result = "Pass"
        else:
            result = "Fail"

        print(score, result)


student_scores = [35, 60, 48, 90, 50]
check_scores(student_scores)



# TASK 2: Variation 4 - Variable Scope

message = "I am global"

def show_numbers(numbers):
    result = "I am local"

    for number in numbers:
        if number > 10:
            print(number, message, result)
        else:
            print(number, "10 or less")


my_numbers = [5, 12, 20]
show_numbers(my_numbers)

print(message)



# TASK 3: Nvidia Radar Function

def check_radar(distances):
    for distance in distances:
        if distance <= 10:
            print("Alert! Too Close")
        else:
            print("Keep driving")


obstacles_distance = [15, 8, 20, 4, 12]
check_radar(obstacles_distance)



# TASK 4: The Highest Score Finder

scores = [45, 82, 19, 99, 56]

largest = 0

for score in scores:
    if score > largest:
        largest = score

print("The highest score is:", largest)



# TASK 5: Modular Braking System

def apply_brakes():
    print("BRAKES APPLIED! Slow down!")


def check_radar(distances):
    for distance in distances:
        print("Obstacle distance:", distance)

        if distance <= 10:
            print("ALERT! Too close!")
            apply_brakes()
        else:
            print("Keep driving")


# First radar scan
scan_one = [15, 8, 20]

# Second radar scan
scan_two = [4, 12, 6]

check_radar(scan_one)
check_radar(scan_two)

