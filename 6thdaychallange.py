# To check Pallindrome for string

def is_pal(n):
    # To remove spaces and convert to lowercase for case-insensitive comparison
    n =n.replace(" ", "").lower()
    return n == n[::-1]

# Exampe usage
input_string= "ab a"
if is_pal(input_string):
    print("String is a pal")
else:
    print("String is not a pal")