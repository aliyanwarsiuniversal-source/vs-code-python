session_a = [0, 5, 2, 0, 5]
session_b = [3, 0, 4, 1]


def summarize_session(points):
    total_points = 0
    rounds_played = len(points)
    rounds_with_points = 0

    for point in points:
        total_points += point

        if point > 0:
            rounds_with_points += 1

    return total_points, rounds_played, rounds_with_points


results_a = summarize_session(session_a)
results_b = summarize_session(session_b)


print("SESSION A SUMMARY")
print("Total Points:", results_a[0])
print("Rounds Played:", results_a[1])
print("Rounds With Points:", results_a[2])

print("\nSESSION B SUMMARY")
print("Total Points:", results_b[0])
print("Rounds Played:", results_b[1])
print("Rounds With Points:", results_b[2])

#TASK 2
distances=[16,5,12,4,15,21,5,8,3,18,6,25,15,2,10,30]
def summarize_distances(distances):
    very_close_count=0
    close_count=0
    safe_count=0
    lowest=distances[0]
    total_count=len(distances)
    for distance in distances:
        if distance <=5:
            very_close_count +=1
        elif distance <=15:
            close_count+=1
        else:
            safe_count+=1
        
        if distance < lowest:
            lowest=distance

    return very_close_count,close_count,safe_count,lowest,total_count

results=summarize_distances(distances)
print("VERY CLOSE COUNT:",results[0])
print("CLOSE COUNT:",results[1])
print("SAFE COUNT:",results[2])
print("LOWEST DISTANCES:",results[3])
print("TOTAL READINGS:",results[4])
