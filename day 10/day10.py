#task 1 :
user_password = input("Enter your password: ")
if user_password == "aliyanwarsi00":
    print("granted access")
else:
    print("access denied ")

#task 2 :
obstacles_distance=[15,8,20,4,12]
for distance in obstacles_distance:
    if distance <= 10:
        print("ALERT! Too close!")
    else:
        print("keep driving")

# task 3 :
network_traffic = ["safe","safe","glitch","safe","malware","safe"]
for packet in network_traffic:
    if packet == "glitch":
        print("Minor glitch detected. Skipping...")
        continue  # This tells Python to skip the rest of the code and go to the next packet
    elif packet =="malware":
        print("critical threat:malware found!shutting down firewall...")
        break
    else:
        print("Connection secure.")