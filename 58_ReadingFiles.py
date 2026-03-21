# Reading the files (.txt , .json, .csv)

# import json
import csv

# file_path = "test.txt"
file_path = "test.csv"


try:
    with open(file_path, "r") as file:

        content = csv.reader(file)
        for line in content:
            # print(line)
            print(line[0])
        # content = json.load(file)

        # content = file.read()

        # print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
