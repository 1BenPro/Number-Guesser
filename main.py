import random

print("Hello, welcome to my guessing game! I am thinking of a number between 1 and 100. Can you guess what it is?")

guess = int(input("Guess a number between 1 and 100: "))

random_number = round(random.uniform(0, 100))
if guess == random_number:
  print("Good job, you guessed the number! The number was ", random_number)
else:
  print("Good try but the number was ", random_number, ", not ", guess)

input("Press enter twice to exit")

if input() == "":
    print("Exiting...")
    exit()