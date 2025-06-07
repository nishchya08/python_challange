# How to print Bold text in Python

variable = 'this is bold'

print('this is NOT bold ' + '\033[1m' +
      variable + '\033[0m' + ' this is NOT bold')
name= 'Nishchya'
print('Nishchya ' + '\033[1m' + name + '\033[0m' + ' Nishchya')

# F- String

First_name='Nishchya'
print(f"Hello {First_name}")
Food='Pizza'
print(f"you like{Food}")
email='nik123@gmail.com'
print(f"your email is {email}")

# Intergers
age=33
print(f"Your age is {age}")

#Boolean

is_student = True
if is_student:
    print("Student")
else:
    print("Teacher")