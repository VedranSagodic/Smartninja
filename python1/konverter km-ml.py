
print("Hello user. Convert kilometers in miles")

while True:

    km = int(input ("Number of kilometers: "))
    km = float(km)

    miles = km * 0.621371

    print("This is number of miles for your kilometers " + str(miles))

    choice = input("would you like to do another conversion (yes/no): ")

    if choice.lower() != "Yes" and choice.lower() != "yes":
        break