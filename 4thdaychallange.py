# To check number is pallindrome

def reverse_string(s):
    return s[::-1]

# Example usage with Indexing

input_string="Hello, World"
reversed_string= reverse_string(input_string)
print("original string:", input_string)
print("Reversed string:", reversed_string)


# Without Indexing

def reversed_string(s):
    rever_str=""
    for char in s:
        rever_str= char+rever_str
    return rever_str
# Example usage
input_str="Deeksha"
reve_st=reversed_string(input_str)
print("Original string:", input_str)
print("Reversed string:", reve_st)

