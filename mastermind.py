import random

def evaluate_guess(code, guess):
    """Evaluate the player's guess against the code."""
    correct_place = 0
    correct_digit_wrong_place = 0
    
    code_count = {}
    guess_count = {}

    # Check for correct digits in the correct place
    for i in range(len(code)):
        if code[i] == guess[i]:
            correct_place += 1
        else:
            code_count[code[i]] = code_count.get(code[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

    # Check for correct digits in the wrong place
    for digit in guess_count:
        if digit in code_count:
            correct_digit_wrong_place += min(code_count[digit], guess_count[digit])

    return correct_place, correct_digit_wrong_place

def mastermind():
    """Run the Mastermind game."""
    code = "0828"
    attempts = 0

    print("Welcome to Mastermind with Numbers!")
    print("Try to guess the 4-digit code. A digit may repeat.")
    print("Hints will be given after each attempt:")
    print("- 'X correct digits in correct place'")
    print("- 'X correct digits in wrong place'")

    while True:
        guess = input("Enter your 4-digit guess: ")

        # Validate the guess
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue

        attempts += 1
        correct_place, correct_digit_wrong_place = evaluate_guess(code, guess)

        if correct_place == 4:
            print(f"Congratulations! You cracked the code {code} in {attempts} attempts.")
            break
        else:
            print(f"{correct_place} digit(s) in the correct place.")
            print(f"{correct_digit_wrong_place} digit(s) correct but in the wrong place.")

if __name__ == "__main__":
    mastermind()
