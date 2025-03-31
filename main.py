from engine import run_game
from games import game_lcm, game_progression


def main():
    print("Choose a game:\n1 - Least Common Multiple \n2 - Geometric Progression")
    choice = input("Enter your choice: ")

    if choice == "1":
        run_game(game_lcm.generate_round, game_lcm.DESCRIPTION)
    elif choice == "2":
        run_game(game_progression.generate_round, game_progression.DESCRIPTION)
    else:
        print("Invalid choice. Exiting...")


if __name__ == "__main__":
    main()
