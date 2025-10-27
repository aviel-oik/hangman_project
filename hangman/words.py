import random

def choose_secret_word(words: list[str]) -> str:
    random_word = random.choice(words)
    return random_word
