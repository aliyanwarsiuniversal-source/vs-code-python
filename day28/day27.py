
readings = [-8, 12, -3, 0, 17, -6, 9, 4]

def analyze_readings(readings):
    highest = readings[0]
    lowest = readings[0]

    positive_count = 0
    negative_count = 0
    zero_count = 0

    for reading in readings:
        if reading > highest:
            highest = reading

        if reading < lowest:
            lowest = reading

        if reading > 0:
            positive_count += 1
        elif reading < 0:
            negative_count += 1
        else:
            zero_count += 1

    return highest, lowest, positive_count, negative_count, zero_count


results = analyze_readings(readings)

print("Highest:", results[0])
print("Lowest:", results[1])
print("Positive:", results[2])
print("Negative:", results[3])
print("Zero:", results[4])




