while True:
    user_word = input("enter a word:")
    if user_word == "quit":
        break
#task 2
def calculator_average():
    #put your old calculator code right here
    #for example:
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    #now do the math and print it
    average = (num1 + num2) /2
    print("the average is:",average)
    #call the function at the very bottom to turn it on (make sure it is not intended)
calculator_average()
#task 3
while True:
    distance = int(input("enter radar distance:"))
    if distance == 0:
        break
    elif distance <10:
        print("ALERT:object too close!")
    elif distance >=10:
        print("path clear")