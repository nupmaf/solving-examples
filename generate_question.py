import random
import time
import msvcrt
import sys


def generate_question(difficulty):
    num1 = random.randint(1, difficulty * 10)
    num2 = random.randint(1, difficulty * 10)
    operator = random.choice(["+", "-", "*", "/"])
    question = f"{num1} {operator} {num2}"
    
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
        while answer < 0:
            num1 = random.randint(1, difficulty * 10)
            num2 = random.randint(1, difficulty * 10)
            answer = num1 - num2
        question = f"{num1} - {num2}"
    elif operator == "*":
        answer = num1 * num2
    else:
        answer = num1 / num2
        while answer != int(answer) or answer < 1 or num2 == 0:
            num1 = random.randint(1, difficulty * 10)
            num2 = random.randint(1, difficulty * 10)
            answer = num1 / num2
        answer = int(answer)
    
    return question, answer


def wait_for_answer(time_limit):
    print(f"\nУ вас есть {time_limit} секунд, чтобы дать ответ.")
    start_time = time.time()
    user_input = ""
    while time.time() - start_time < time_limit:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            key = key.decode("utf-8")
            if key == 'q':
                return False
            elif key == '\r':
                return int(user_input)
            elif key == '\x08':
                user_input = user_input[:-1]
                print(f"\b \b", end="", flush=True)
            elif key.isnumeric():
                user_input += key
                print(key, end="", flush=True)
        time.sleep(0.1)
    return False


def loading_animation():
    print("Загрузка...")
    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")


def play():
    points = 0
    max_points = 0
    print("Добро пожаловать в игру! Выберите уровень сложности:\n")
    print("1 - Легкий (числа до 10)")
    print("2 - Средний (числа до 50)")
    print("3 - Сложный (числа до 100)")
    print("4 - Очень сложный (числа до 1000)")
    print("5 - Сверхсложный (числа до 10000)")
    difficulty = int(input("Введите число от 1 до 5: "))
    loading_animation()  
    time_limit = 15 if difficulty == 1 else 10  
    
    while True:
        question, answer = generate_question(difficulty)
        print(f"\n{question}")
        user_answer = wait_for_answer(time_limit)
        
        if not user_answer:  
            print(f"\nВы набрали {points} очков из {max_points} возможных!")
            sys.exit()
        
        if user_answer == answer:
            print("Правильно!")
            points += 1
        else:
            print(f"Неправильно! Правильный ответ: {answer}")
            another_chance = input("Хотите попробовать еще раз? (д/н)").lower()
            if another_chance == "н":
                print(f"\nВы набрали {points} очков из {max_points} возможных!")
                sys.exit()
            elif another_chance != "y":
                print("Неверный формат ввода!")
                continue
            user_answer = wait_for_answer(12)
            if not user_answer:
                print(f"\nВы набрали {points} очков из {max_points} возможных!")
                sys.exit()
            if user_answer == answer:
                print(" Правильно! ")
                points += 1
            else:
                print(f" Неправильно! Правильный ответ: {answer}")
        max_points += 1
    
    print(f"\nВы набрали {points} очков из {max_points} возможных!")

play()