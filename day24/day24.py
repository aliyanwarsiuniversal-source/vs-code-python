#TASK 1
numbers=[-12,-5,-28,-3,-19,-7]
highest=numbers[0]
lowest=numbers[0]
for number in numbers:
    if number > highest:
        highest=number
    if number < lowest:
        lowest=number

print("HIGHEST NUMBER:",highest)
print("LOWEST NUMBER:",lowest)

#TASK 2
scores=[35,50,72,48,90,55,30,80]
def analyze_scores(scores):
    total_scores=0
    highest=scores[0]
    lowest=scores[0]
    passing_count=0
    failing_count=0
    total_count=0
    for score in scores:
        total_scores += score
        total_count +=1
        if score > highest:
            highest=score
        if score < lowest:
            lowest=score
        if score >=50:
            passing_count+=1
        else:
            failing_count +=1
    return total_scores,highest,lowest,passing_count,failing_count,total_count

results=analyze_scores(scores)
print("TOTAL SCORE:",results[0])
print("HIGHEST SCORE:",results[1])
print("LOWEST SCORE:",results[2])
print("PASSING COUNT:",results[3])
print("FAILING COUNT:",results[4])
print("TOTAL COUNT:",results[5])

#TASK 3
distances=[4,8,15,20,3,12,25,5]
very_close_count=0
close_count=0
safe_count=0
total_count=0
for distance in distances:
    total_count +=1
    if distance <=5:
        very_close_count+=1
    elif distance <=15:
        close_count+=1
    else:
        safe_count+=1


print("VERY CLOSE COUNT:", very_close_count)
print("CLOSE COUNT:", close_count)
print("SAFE COUNT:", safe_count)
print("TOTAL COUNT:", total_count)