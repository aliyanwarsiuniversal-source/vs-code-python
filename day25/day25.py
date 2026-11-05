#TASK 1
points=[4,0,7,4,0,3]
total_points=0
rounds_played=len(points)
rounds_ponits=0
for point in points:
    total_points += point
    if point > 0:
        rounds_ponits+=1

print("TOTAL POINTS:",total_points)
print("ROUNDS PLAYED:",rounds_played)
print("ROUNDS WITH POINTS:",rounds_ponits)

#TASK 2
group_a=[48,60,75,60]
group_b=[50,82,45,82,55]
def sumarize_scores(scores):
    highest=scores[0]
    lowest=scores[0]
    passing_count=0
    for score in scores:
        if score > highest:
            highest=score
        if score < lowest:
            lowest=score
        if score >=50:
            passing_count +=1

    return highest,lowest,passing_count

results_a=sumarize_scores(group_a)
results_b=sumarize_scores(group_b)

print("GROUP A SUMMARY")
print("HIGHEST SCORE:",results_a[0])
print("LOWEST SCORE:",results_a[1])
print("PASSING COUNT:",results_a[2])

print("GROUP B SUMMARY")
print("HIGHEST SCORE:",results_b[0])
print("LOWEST SCORE:",results_b[1])
print("PASSING COUNT:",results_b[2])
#TASK 3
def analyze_distance(distances):
    very_close=0
    close=0
    safe=0
    for distance in distances:
        if distance <=5:
            very_close+=1
        elif distance <=15:
            close+=1
        else:
            safe +=1

    total_count=len(distances)
    return very_close,close,safe

distances=[15,4,20,5,9,16,3,15]
very_close, close, safe, total_count = analyze_distance(distances)
print("Very Close:", very_close)
print("Close:", close)
print("Safe:", safe)
print("Total Readings:", total_count)
print("Very Close:", very_close)
print("Close:", close)
print("Safe:", safe)
print("Total Readings:", total_count)