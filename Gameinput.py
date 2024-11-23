import random

def guess_the_number():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Randomly select a number in the given range
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    # Define the maximum number of attempts
    max_attempts = 10
    attempts = 0
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess the number.")

    # Loop to give the user multiple attempts
    while attempts < max_attempts:
        # Take user input
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts += 1
        
        # Check if the guess is correct
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low! Try guessing a higher number.")
        else:
            print("Too high! Try guessing a lower number.")
        
        # Check if the user has run out of attempts
        if attempts == max_attempts:
            print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {number_to_guess}.")

# Run the game
guess_the_number()
