# Python writing files (.txt, .json, .csv)
# w , x --> write (x --> If it doesn't already exist)
# a --> append
# r --> read

# import json
import csv

all_employees = [
    ["Name", "Age", "Job"],
    ["Mohit", 20, "Software Engineer"],
    ["Rohit", 22, "Data Engineer"],
    ["", 25, "Software Engineer"],
]


# employee = {
#     "name": "Mohit",
#     "age":  20,
#     "job": "Software Engineer",
# }

# employees = ["Mohit", "Rohit", "Piyush", "Nishit"]



# txt_data = "I Love Doodh and Malai"

file_path = "test.csv"

try:
    with open(file= file_path, mode= "w", newline="") as file:
        # file.write(txt_data + "\n")
        # print(f"txt file '{file_path}' was created")

        # for employee in employees:
        #     file.write(employee + "  ")

        # json.dump(employee, file, indent=4)

        writer = csv.writer(file)
        for row in all_employees:
            writer.writerow(row)

        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

