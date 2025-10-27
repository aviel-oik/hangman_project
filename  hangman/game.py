

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
# guessed.add(ch)
        return True,"check..."





