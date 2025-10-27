

def init_state(secret: str, max_tries: int) -> dict:
    display_list = ["_"] * len(secret)
    dic = {"secret" : secret, "display" : display_list, "guesses" : [], "wrong_guesses" : 0, "max_tries" : max_tries}
    return dic
