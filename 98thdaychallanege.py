import os

file_path = "stuff/test.txt"
if os.path.exists(file_path):
    print(f"The location {file_path} exists.")
else:
    print(f"The location {file_path} does not exist.")