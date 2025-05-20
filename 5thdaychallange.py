# To check Pallindrome for Number
def is_pal(n):
    # Convert number to string for easy manipulation
    num_str=str(n)
    return num_str == num_str[::-1]

# Example usage
input_number=12322
if is_pal(input_number):
    print("The number is a pallindrome")
else:
    print("The number is not a pallindrome")