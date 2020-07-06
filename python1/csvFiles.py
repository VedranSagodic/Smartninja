import csv

with open("homework.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimeter)
    next(csv_reader)

    for row in csv_reader:
        print(f"")

