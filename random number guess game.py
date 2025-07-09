import random as r
# Random number guessing game
range_start = 1 
range_end = 100
target_number = r.randint(range_start, range_end)
print(f"\nGuess the number between {range_start} and {range_end} to win.")
lives = 5
while lives > 0:
    try:
        guess = int(input(f"\nEnter the number (Lives left: {lives}): "))
    except ValueError:
        print(" Please enter a valid number .")
        continue

    if guess == target_number:
        print(" Correct! You've guessed the number. You win!")
        break
    elif guess < target_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    lives -= 1

print("\nGame Over! The target number was:", target_number)
print("The number was: " + str(target_number))