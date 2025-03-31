import math
import random

def lcm(a, b, c):
    return math.lcm(a, b, c)

def play_game():
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")
    print("Find the smallest common multiple of given numbers.\n")
    
    while True:
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = lcm(*numbers)
        
        print(f"Question: {numbers[0]} {numbers[1]} {numbers[2]}")
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == 'exit':
            print(f"Goodbye, {name}!")
            break
        
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n")
            print("Let's try again!")

if __name__ == "__main__":
    play_game()
