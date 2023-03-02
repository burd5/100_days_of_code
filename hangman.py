# Hangman

import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)

print(logo)

display = ["_"] * len(chosen_word)

end_game = False
lives = 7

while not end_game:
    guess = input('Guess a letter: ').lower()
    def check_letter(guess):
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = guess
    if guess not in chosen_word:
        lives -= 1
        print('You guessed wrong.')
        print(stages[lives])
        if lives == 0:
            end_game = True
            print('You lost.')

    check_letter(guess)
    print(display)

    if "_" not in display:
        end_game = True
        print('You won.')


