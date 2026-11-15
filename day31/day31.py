
scores_a = [14, 22, 17, 30, 19]
scores_b = [-6, -2, -9, -4]


def summarize_scores(scores):
    highest = scores[0]
    lowest = scores[0]
    total = 0
    above_10_count = 0

    for score in scores:
        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

        total += score

        if score > 10:
            above_10_count += 1

    total_scores = len(scores)

    return highest, lowest, total, above_10_count, total_scores


results_a = summarize_scores(scores_a)
results_b = summarize_scores(scores_b)


print("SCORES A")
print("Highest:", results_a[0])
print("Lowest:", results_a[1])
print("Total:", results_a[2])
print("Above 10:", results_a[3])
print("Total scores:", results_a[4])

print("\nSCORES B")
print("Highest:", results_b[0])
print("Lowest:", results_b[1])
print("Total:", results_b[2])
print("Above 10:", results_b[3])
print("Total scores:", results_b[4])

#TASK 2
distances = [20, 8, 21, 3, 9, 20, 35, 8, 14, 2]


def analyze_distances(distances):
    very_close = 0
    close = 0
    safe = 0
    shortest = distances[0]

    for distance in distances:
        if distance <= 8:
            very_close += 1
        elif distance <= 20:
            close += 1
        else:
            safe += 1

        if distance < shortest:
            shortest = distance

    return very_close, close, safe, shortest, len(distances)


results = analyze_distances(distances)

print("Very close:", results[0])
print("Close:", results[1])
print("Safe:", results[2])
print("Shortest distance:", results[3])
print("Total readings:", results[4])
