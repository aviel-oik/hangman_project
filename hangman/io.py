# from game import is_won, is_lost
# import game

def prompt_guess() -> str:
    ch = input("Enter your guess: ")
    return ch

def print_status(state: dict) -> None:
    print("the state is: " + "".join(state["display"]))
    print("letters already guessed : " + str(state["guesses"]))
    print("number of tries remaining : " + str(state["max_tries"] - state["wrong_guesses"]))

def render_summary(state: dict) -> str:
    return "the secret is: " + state["secret"] + "\nThe letters that have been guessed are : " + "".join(state["display"])

def print_result(state: dict) -> None:
    if is_won(state):
        print("You won!")
    if is_lost(state):
        print("You lost!")
        print(render_summary(state))


# func of game
def is_won(state: dict) -> bool:
    return state["secret"] == str(state["display"])

def is_lost(state: dict) -> bool:
    return state["wrong_guesses"] >= state["max_tries"]