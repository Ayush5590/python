print(" You need to guess the number that opens the door.")
lives = 3

while lives > 0:
    try:
        guess = int(input(f"\nEnter your guess (Lives left: {lives}): "))
    except ValueError:
        print(" Please enter a valid integer.")
        continue

    if guess % 3 == 0 and guess % 5 == 0:
        print(" Correct The door opens.")
        break
    else:
        if guess % 3 == 0 and guess % 5 != 0:
            print("Hint: Your number is divisible by 3!")
        elif guess % 5 == 0 and guess % 3 != 0:
            print("Hint: Your number is divisible by 5!")
        else:
            print("No hint: Try a number divisible by 3 or 5.")
        lives -= 1

if lives == 0:
    print("\n You've used all your lives. Game over!")