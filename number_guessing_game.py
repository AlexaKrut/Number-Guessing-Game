import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have limited chances to guess the correct number.")
    print()
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print()

    levels = {1: "Easy", 2: "Medium", 3: "Hard"}
    chances = {1: 10, 2: 5, 3: 3}
    secret_number = random.randint(1, 100)
    count_attempts = 0

    while True:
        print("Enter your choice: ")
        level = int(input())
        if level in [1, 2, 3]:
            attempts = chances.get(level)
            print(f"Great! You have selected the {levels.get(level)} difficulty level.")
            print("Let's start the game!")
            break
        else:
            print("Ooops... There's no such variant. Please, try again.")

    while attempts > 0:
        print("Enter your guess: ")
        guess_number = int(input())
        count_attempts += 1 
        if guess_number == secret_number:
            print(f"Congratulations! You guessed the correct number in {count_attempts} attempts.")
            break
        elif guess_number < secret_number:
            print(f"Incorrect! The number is greater than {guess_number}.")
        elif guess_number > secret_number:
            print(f"Incorrect! The number is less than {guess_number}.") 
        attempts -= 1 

    if attempts == 0:
        print("The Game is Over. You are out of chances.")
    else:
        print("Win!")

if __name__ == '__main__':
    main()
