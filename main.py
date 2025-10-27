import hangman.words
import hangman.game
import hangman.io
import data.words

def play(words: list[str], max_tries: int = 26) -> None:
    word = hangman.words.choose_secret_word(words)
    state = hangman.game.init_state(word, max_tries)
    while True:
        flag = True
        while flag:
            ch = hangman.io.prompt_guess()
            (flag, message) = hangman.game.validate_guess(ch, state["guesses"])
            print(message)
        is_in = hangman.game.apply_guess(state, ch)
        if is_in:
            print("Well done! The letter is indeed part of the word.")
        else:
            print("Sorry, the letter wasn't part of the word.")
        hangman.io.print_status(state)
        if hangman.game.is_won(state):
            hangman.io.print_result(state)
            break
        if hangman.game.is_lost(state):
            hangman.io.print_result(state)
            break



def main():
    play(data.words.words)

main()