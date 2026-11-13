temperatures = [-8, -3, -12, -5, -3, -9]
def analyze_temperatures(temperatures):
    highest=temperatures[0]
    lowest=temperatures[0]
    total_reading_count=0
    number_of_very_cold_readings_count=0
    total_of_all_temperatures=len(temperatures)

    for temperature in temperatures:
        if temperature > highest:
            highest=temperature
        
        if temperature < lowest:
            lowest=temperature

        if temperature < 0:
            total_reading_count+=1

        if temperature <-5:
            number_of_very_cold_readings_count+=1

    total_reading_count = len(temperatures)

    return highest,lowest,total_reading_count,number_of_very_cold_readings_count,total_of_all_temperatures

results=analyze_temperatures(temperatures)

print("HIGHEST TEM:",results[0])
print("LOWEST TEMP:",results[1])
print("TOTAL READING:",[3])
print("VERY COLD READINGS:",results[4])
print("TOTAL OF TEMPERATURES:",results[5])