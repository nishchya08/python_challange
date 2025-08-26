import os

#file_path = "stuff/test.txt"
file_path = "/Users/nishchyakataria/Projects/python_challange/stuff/test.txt"
if os.path.exists(file_path):
    print(f"The location {file_path} exists.")
    if os.path.isfile(file_path):
        print(f"The file {file_path} is a file.")
    else:
        print(f"The location {file_path} is not a file.")
else:
    print(f"The location {file_path} does not exist.")

    