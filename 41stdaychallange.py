# Validate user input Excercise
# Username is not more than 12 characters
# Username should not create any space
# Username should not having any digit
username =input("Enter your username: ")
if len(username) > 12:
     print("Your username is too long")
elif not username.find(" ") == -1:
    print("Username can't create any space")
elif not username.isalpha():
    print("Username can't be alphanumeric")
else:
    print(f"Welcome {username}")