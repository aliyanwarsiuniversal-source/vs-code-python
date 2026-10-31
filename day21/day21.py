#TASK 1:                                                FINDING THE NUMBER COUNT
numbers=[12,-5,0,8,-15,20,-3,0,7]
lowest=numbers[0]
higest=numbers[0]

total=0
positive_count=0
negativie_count=0
zero_count=0
total_elements=0
for number in numbers:
    if number >higest:
        higest=number
    
    if number<lowest:
        lowest=number
    
    total+=number
    total_elements+=1
    if number >  0:
        positive_count+=1
    elif number < 0:
        negativie_count+=1
    else:
        zero_count+=1

print("HIGHEST NUMBER:",higest)
print("LOWEST NUMBER:",lowest)
print("sum:",total)
print("POSITIVE NUMBER:",positive_count)
print("NEGATIVE NUMBER:",negativie_count)
print("ZEROS:",zero_count)
print("TOTAL ELEMENT:",total_elements)

#TASK 2:                                            Autonomous Car Distance Analysi  
distances = [3, 7, 12, 18, 4, 25, 9, 15, 2, 30]

very_close = 0
close = 0
safe = 0
total = 0

for distance in distances:

    if distance <= 5:
        very_close += 1

    elif distance <= 15:
        close += 1

    else:
        safe += 1

    total += 1

print("Very Close:", very_close)
print("Close:", close)
print("Safe:", safe)
print("Total:", total)

