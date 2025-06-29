# Generate random numbers in python
import random
# number = random.randint(1, 6)
# print(number)

# options = ["paper","scissor","pen"]
# option = random.choice(options)
# print(option)

# cards = ["A","C","1","D","E","4","8"]
# random.shuffle(cards)
# print(cards)
low = 1
high = 20
guesses = 0
number = random.randint(low, high)
while True:
    guess = int(input("Guess a number between {low} and {high}: "))
    guesses += 1
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print(f"Your guess is correct")
        break
print(f"You guessed {guesses} times.")