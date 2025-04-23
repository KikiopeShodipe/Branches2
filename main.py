import random
# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100. Can you guess it?")
while True:
    # Get user input
    try:
        user_input = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    # Check the guess
    if user_input == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_input < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")