import game

def prompt_guess() -> str:
    ch = input("Enter your guess: ")
    return ch

def print_status(state: dict) -> None:
    print("the state is: " + "".join(state["display"]) + "\n")
    print("letters already guessed : " + state["guessed"] + "\n")
    print("number of tries remaining : " + state["max_tries"] - state["wrong_guesses"] + "\n")

def print_result(state: dict) -> None:
    if game.is_won(dict):
        print("You won!")
    if game.is_lost(dict):
        print("You lost!")