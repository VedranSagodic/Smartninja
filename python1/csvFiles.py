import csv

with open("tableText.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        print(f"{row[0]} is {row[2]} and {row[1]} years old.")

