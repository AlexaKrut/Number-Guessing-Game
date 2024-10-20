import random
import time

def get_level():
    levels = {1: "Легкий", 2: "Средний", 3: "Сложный"}
    chances = {1: 10, 2: 5, 3: 3}
    
    while True:
        print("Пожалуйста, выберите уровень сложности:")
        print("1. Легкий (10 попыток)")
        print("2. Средний (5 попыток)")
        print("3. Сложный (3 попытки)")
        print()
        level = int(input("Введите ваш выбор: "))
        
        if level in levels:
            return levels[level], chances[level]
        else:
            print("Упс... Такого варианта нет. Пожалуйста, попробуйте снова.")

def play_game(secret_number, attempts):
    count_attempts = 0
    start_time = time.time()

    while attempts > 0:
        guess_number = int(input("Введите вашу догадку: "))
        count_attempts += 1
        
        if guess_number == secret_number:
            print(f"Поздравляем! Вы угадали правильное число за {count_attempts} попыток.")
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Это заняло {execution_time:.2f} секунд.")
            return count_attempts
        elif guess_number < secret_number:
            print(f"Неправильно! Число больше, чем {guess_number}.")
        else:
            print(f"Неправильно! Число меньше, чем {guess_number}.")
        
        attempts -= 1

    print("Игра окончена. У вас закончились попытки.")
    print()
    return None

def quit_the_game():
    print("Хотите продолжить? да или нет")
    answer = input()
    return answer.lower() == 'да'

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я думаю о числе от 1 до 100.")
    print()
    
    best_attempts = float('inf')

    while True:
        level, attempts = get_level()
        print(f"Отлично! Вы выбрали уровень сложности {level}.")
        print("Давайте начнем игру!")
        print()

        secret_number = random.randint(1, 100)
        current_attempts = play_game(secret_number, attempts)

        if current_attempts is not None:
            if current_attempts < best_attempts:
                best_attempts = current_attempts
                print(f"Новый лучший результат! Вы угадали число за {best_attempts} попыток.")
            else:
                print(f"Ваш лучший результат остается {best_attempts} попыток.")

        if not quit_the_game():
            break

if __name__ == '__main__':
    main()