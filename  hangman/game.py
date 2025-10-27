

def init_state(secret: str, max_tries: int) -> dict:
    display_list = ["_"] * len(secret)
    dic = {"secret" : secret, "display" : display_list, "guesses" : [], "wrong_guesses" : 0, "max_tries" : max_tries}
    return dic

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    valid = True
    if len(ch) != 1:
        return False,"invalid input"
    if ch in guessed:
        return False,"already guessed,try again"
    else:
        return True,"check..."

def apply_guess(state: dict, ch: str) -> bool:
    state["guesses"].append(ch)
    if ch in state["secret"]:
        for i in range(0, len(state["secret"])-1):
            if state["secret"][i] == ch:
                state["display"][i] = ch
        return True
    else:
        state["wrong_guesses"] += 1
        return False

def is_won(state: dict) -> bool:
    return state["guesses"] == state["display"]







