marks_a = [45, 33, 78, 33, 90]
marks_b = [0, 12, 40, 7]

def summarize_marks(marks):
    highest=marks[0]
    lowest=marks[0]
    total=0
    passing=0

    for mark in marks:
        if mark > highest:
            highest=mark

        if mark < lowest:
            lowest=mark

        total += mark

        if mark >=40:
            passing+=1

    return highest,lowest,total,passing,len(marks)

results_a=summarize_marks(marks_a)
results_b=summarize_marks(marks_b)

print("MARKS A")
print("HIGHEST:",results_a[0])
print("LOWEST:",results_a[1])
print("TOTAL:",results_a[2])
print("PASSING MARKS:",results_a[3])
print("TOTAL MARKS:",results_a[4])

print("\nMARKS B")
print("HIGHEST:",results_b[0])
print("LOWEST:",results_b[1])
print("TOTAL:",results_b[2])
print("PASSING MARKS:",results_b[3])
print("TOTAL MARKS:",results_b[4])