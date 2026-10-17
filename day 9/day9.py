for numbers in range (1,51):
    if numbers % 5==0:
     print (numbers)

#task2: FizzBuzz
for numbers in range(1, 21):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("fly higher")
    elif numbers % 3 == 0:
        print("Code")
    elif numbers % 5 == 0:
        print("Logic")
    else:
        print(numbers)

#task 3: server load monitor
cpu_load =[20,85,45,92,30,99,15]
for load in cpu_load:
    if load > 90: 
     print("CRITICAL: Server crash imminent! Load:")
    if load > 80: 
     print("WARNING: High headwinds. Load: ")
    if load >100:
       print("shuting down the system.load:")