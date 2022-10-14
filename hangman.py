import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
display = []
guessed_letters = []

for i in chosen_word:
    display.append("_")


while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You've already guessed this letter, try again.")
    else:
        guessed_letters.append(guess)
        for i in range(word_length):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter
        if guess not in chosen_word:
            print(f"{guess} is not in word.")
            lives -= 1
            if lives == 0:
                print("You Lose")
                print(stages[lives])
                break      
        print(f"{' '.join(display)}")
        print(stages[lives])

if "_" not in display:
    print("You Win")