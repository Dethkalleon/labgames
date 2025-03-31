def run_game(game_logic, description):
    """Функция запускает игру с переданной логикой."""
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")
    print(description + "\n")

    rounds = 3  # Максимальное количество раундов

    for _ in range(rounds):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == 'exit':
            print(f"Goodbye, {name}!")
            return

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n")
            print("Let's try again!\n")

    print(f"Congratulations, {name}!\n")
