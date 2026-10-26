temperatures=[25,32,38,29,41,35]
normal_count=0
high_count=0
for temperature in temperatures:
    print("temperature:",temperature)
    if temperature>35:
        print("HIGH TEMPERATURE")
        high_count+=1
    else:
        print("NORMAL TEMPERATURE")
        normal_count+=1

print("total temperature:",len(temperatures))
print("high temperature:",high_count)
print("normal temperature:",normal_count)

#TASK 2
def calculate_average(number):
    total=sum(number)
    count=len(number)
    average=total/count
    return average
scores = [10, 20, 30, 40, 50]
result=calculate_average(scores)
print("Average score:",result)

#TASK 3

scores = [75, 90, 65, 95, 80]

highest_score =0

for score in scores:
    if score > highest_score:
        highest_score = score

print("Highest score:", highest_score)

#TASK 4
def analyze_distances(distances):
    safe_count = 0
    close_count = 0
    very_close_count = 0

    for distance in distances:
        if distance <= 5:
            print(distance, "very close")
            very_close_count += 1
        elif distance <= 15:
            print(distance, "close")
            close_count += 1
        else:
            print(distance, "safe")
            safe_count += 1

    print("Very Close Count:", very_close_count)
    print("Close Count:", close_count)
    print("Safe Count:", safe_count)
    print("Total Distances:", len(distances))


distances = [25, 8, 15, 4, 30, 12, 6, 40]

analyze_distances(distances)
