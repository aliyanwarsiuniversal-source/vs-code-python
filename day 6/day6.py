car_speeds=[120,50,80,120,10]
for speed in car_speeds:
    print(speed)
#task 2
while True:
         command = input("enter command :")
         if command=="stop" or command == "exit":
                break
         print("system is running...")
#task 3
student_marks = [45,82,30,95,60]
for marks in student_marks:
       if marks>=50:
              print("pass")
       else:
              print("fail")      
#task4
sensor_readings = [80, 45, 20, 8, 100]

for distance in sensor_readings:
    if distance > 50:
        print(distance, "m -> Safe: Keep driving!")
    elif distance > 10:
        print(distance, "m -> Warning: Slow down!")
    else:
        print(distance, "m -> Emergency: Apply brake!")