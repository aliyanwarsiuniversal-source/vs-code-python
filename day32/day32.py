week_a = [12, 7, 15, 9, 15]
week_b = [-3, 4, -8, 0, 6]

def summarize_weeks(temps):
    highest=temps[0]
    lowest=temps[0]
    total=0
    freezing_days=0

    for temp in temps:
        if temp > highest:
            highest=temp

        if temp < lowest:
            lowest=temp

        total += temp

        if temp < 0:
            freezing_days +=1

    return highest,lowest,total,freezing_days,len(temps)

results_a=summarize_weeks(week_a)
results_b=summarize_weeks(week_b)

print("RESULTS OF WEEK A")
print("HIGHEST TEMPERATURE:",results_a[0])
print("LOWEST TEMPERATURE:",results_a[1])
print("TOTAL:",results_a[2])
print("FREEZING DAYS:",results_a[3])
print("TOTAL READINGS:",results_a[4])


print("\nRESULTS OF WEEK B")
print("HIGHEST TEMPERATURE:",results_b[0])
print("LOWEST TEMPERATURE:",results_b[1])
print("TOTAL:",results_b[2])
print("FREEZING DAYS:",results_b[3])
print("TOTAL READINGS:",results_b[4])