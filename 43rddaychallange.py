
email = input("Enter your email")

index = email.index("@")
username = email[:index]
domain = email[index+1:]
print(f"Your username is {username} and domain is {domain}")


email = input("Enter your email: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")