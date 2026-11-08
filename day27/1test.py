#TASK 1
session_a=[4,0,2,4,0]
session_b=[0,6,1,0]
def summarize_session(points):
    total_points=0
    total_rounds=len(points)
    scoring_rounds=0
    for point in points:
          total_points += point
          
          if point >0:
               scoring_rounds+=1

    return total_points,total_rounds,scoring_rounds

results_a=summarize_session(session_a)
results_b=summarize_session(session_b)

print("SESSION A SUMMARY")
print("Total Points:", results_a[0])
print("Total Rounds:", results_a[1])
print("Scoring Rounds:", results_a[2])

print("\nSESSION B SUMMARY")
print("Total Points:", results_b[0])
print("Total Rounds:", results_b[1])
print("Scoring Rounds:", results_b[2])

#TASK 2
readings = [14, 9, 22, 6, 17, 6]


def summarize_readings(readings):
    highest = readings[0]
    lowest = readings[0]
    total_readings = len(readings)

    for reading in readings:
        if reading > highest:
            highest = reading

        if reading < lowest:
            lowest = reading

    return highest, lowest, total_readings


results = summarize_readings(readings)

print("HIGHEST READING:", results[0])
print("LOWEST READING:", results[1])
print("TOTAL READINGS:", results[2])

#TASK 3
distances = [15, 3, 18, 6, 5, 22, 10, 4, 16, 15, 8, 2]


def summarize_distances(distances):
    very_close_count = 0
    close_count = 0
    safe_count = 0
    shortest = distances[0]
    total_readings = len(distances)

    for distance in distances:

        if distance <= 5:
            very_close_count += 1
        elif distance <= 15:
            close_count += 1
        else:
            safe_count += 1

        if distance < shortest:
            shortest = distance

    return very_close_count, close_count, safe_count, shortest, total_readings


results = summarize_distances(distances)

print("VERY CLOSE COUNT:", results[0])
print("CLOSE COUNT:", results[1])
print("SAFE COUNT:", results[2])
print("SHORTEST DISTANCE:", results[3])
print("TOTAL READINGS:", results[4])