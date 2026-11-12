distances = [14, 3, 22, 7, 5, 19, 11, 2, 26, 8]

def analyze_distances(distances):
    very_close_count = 0
    close_count = 0
    safe_count = 0
    shortest = distances[0]

    for distance in distances:
        if distance <= 5:
            very_close_count += 1
        elif distance <= 15:
            close_count += 1
        else:
            safe_count += 1

        if distance < shortest:
            shortest = distance

    return very_close_count, close_count, safe_count, shortest, len(distances)


results = analyze_distances(distances)

print("Very close:", results[0])
print("Close:", results[1])
print("Safe:", results[2])
print("Shortest distance:", results[3])
print("Total readings:", results[4])
