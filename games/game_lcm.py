import random
import math

def generate_round():
    numbers = [random.randint(1, 10) for _ in range(3)]
    correct_answer = math.lcm(*numbers)
    question = " ".join(map(str, numbers))
    return question, correct_answer

DESCRIPTION = "Find the smallest common multiple of given numbers."
