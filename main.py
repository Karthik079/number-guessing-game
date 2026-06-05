wn = """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.


Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)"""

print(wn)

d = int(input("Enter your choice: "))

if d == 1:
    print("Great! You have selected the Easy difficulty level.")
    c = 10
elif d == 2:
    print("Great! You have selected the Medium difficulty level.")
    c = 5
elif d == 3:
    print("Great! You have selected the Hard difficulty level.")
    c = 3
else:
    print("Invalid choice. Please select a valid difficulty level." )


import random
number = random.randint(1, 100)
print(number)
i = 0
a = 0

while i < c:
    c -= 1
    a += 1
    guess = int(input("Enter your guess: "))
    if guess == number:
        print(f"Congratulations! You guessed the correct number in {a} attempts.")
        break
    else:
        if number < guess :
          print(f"Incorrect! The number is less than {guess}")
        else:
          print(f"Incorrect! The number is greater than {guess}")

