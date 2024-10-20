import random

def get_level():
    levels = {1: "Easy", 2: "Medium", 3: "Hard"}
    chances = {1: 10, 2: 5, 3: 3}
    
    while True:
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        level = int(input("Enter your choice: "))
        
        if level in levels:
            return levels[level], chances[level]
        else:
            print("Ooops... There's no such variant. Please, try again.")

def play_game(secret_number, attempts):
    count_attempts = 0

    while attempts > 0:
        guess_number = int(input("Enter your guess: "))
        count_attempts += 1
        
        if guess_number == secret_number:
            print(f"Congratulations! You guessed the correct number in {count_attempts} attempts.")
            return True
        elif guess_number < secret_number:
            print(f"Incorrect! The number is greater than {guess_number}.")
        else:
            print(f"Incorrect! The number is less than {guess_number}.")
        
        attempts -= 1

    print("The Game is Over. You are out of chances.")
    return False

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    level, attempts = get_level()
    print(f"Great! You have selected the {level} difficulty level.")
    print("Let's start the game!")

    secret_number = random.randint(1, 100)
    play_game(secret_number, attempts)

if __name__ == '__main__':
    main()
