#python writing files (.txt, .json, .csv)

import json
import csv
# employee = {
#     "name" : "Nishchya",
#     "age" : 35,
#     "job" : "Sofware Engineer"
# }


employees = [["Name", "Age", "Job"],
             ["Nishchya", 35, "Software Engineer"],
            ["Rajesh", 30, "Data Scientist"],
            ["Aditi", 28, "Product Manager"]]


#employees = ["John Doe", "Jane Smith", "Emily Davis"]
#txt_data = " I love italian pizza"
file_path = "/Users/nishchyakataria/Desktop/Nishchya/output.txt"

# with open(file_path, 'w') as file:
#     for employee in employees:
#         file.write(employee + "\n")
#     print(f"txt file '{file_path}' was created ")

# try:
#     with open(file_path, 'w') as file:
#         json.dump(employee, file, indent=4)
#         print(f"txt file '{file_path}' was created ")
# except FileExistsError:
#     print("That file already exist")

try:
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was crr=eated")
except FileExistsError:
    print("That file already exist")


    
