#step1 user se mark input lo
marks =int(input("enter your marks: "))
#step2 conditions check karo 
if marks>=90:
        print("grade: A+)(outstanding!)")
elif marks >=75:
        print("grade: A)(very good!)")
elif marks >=50:
        print("grade: b)(needs practice!)")
else:
        print("grade: f)(work harder!)")

#task2 
for num in range(1,11):
        if num % 2 == 0:
                print(num,"is even")
        else:
                print(num,"is odd")