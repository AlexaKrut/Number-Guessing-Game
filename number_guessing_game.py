import random
import time

def get_level():
    levels = {1: "Easy", 2: "Medium", 3: "Hard"}
    chances = {1: 10, 2: 5, 3: 3}
    
    while True:
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        print()
        level = int(input("Enter your choice: "))
        
        if level in levels:
            return levels[level], chances[level]
        else:
            print("Ooops... There's no such variant. Please, try again.")

def play_game(secret_number, attempts):
    count_attempts = 0
    start_time = time.time()

    while attempts > 0:
        guess_number = int(input("Enter your guess: "))
        count_attempts += 1
        
        if guess_number == secret_number:
            print(f"Congratulations! You guessed the correct number in {count_attempts} attempts.")
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"It took {execution_time:.2f} seconds.")
            return count_attempts  # Возвращаем количество попыток
        elif guess_number < secret_number:
            print(f"Incorrect! The number is greater than {guess_number}.")
        else:
            print(f"Incorrect! The number is less than {guess_number}.")
        
        attempts -= 1

    print("The Game is Over. You are out of chances.")
    print()
    return None  # Возвращаем None, если не угадали

def quit_the_game():
    print("Would you like to continue? yes or no")
    answer = input()
    return answer.lower() == 'yes'

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print()
    
    best_attempts = float('inf')  # Инициализируем лучший результат как бесконечность

    while True:
        level, attempts = get_level()
        print(f"Great! You have selected the {level} difficulty level.")
        print("Let's start the game!")
        print()

        secret_number = random.randint(1, 100)
        current_attempts = play_game(secret_number, attempts)

        # Проверяем, угадал ли игрок число
        if current_attempts is not None:
            # Если угадал, проверяем, обновляется ли лучший результат
            if current_attempts < best_attempts:
                best_attempts = current_attempts
                print(f"New best result! You guessed the number in {best_attempts} attempts.")
            else:
                print(f"Your best result remains {best_attempts} attempts.")

        if not quit_the_game():
            break

if __name__ == '__main__':
    main()