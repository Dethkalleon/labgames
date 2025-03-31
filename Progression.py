import math
import random

def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, correct_answer

def play_game():
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")
    print("What number is missing in the progression?\n")
    
    while True:
        progression, correct_answer = generate_progression()
        
        print(f"Question: {' '.join(map(str, progression))}")
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == 'exit':
            print(f"Goodbye, {name}!")
            break
        
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n")
            print("Let's try again!")
    
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    play_game()