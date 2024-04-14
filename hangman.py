import random

word = input('enter your name:')
print('Welcome '+ word )


def choose_word():
    """Choose a random word from the list of words."""
    words = ['python','Sunday','Java', 'Commerce', 'science', 'Funday','Coding']
    return random.choice(words)

def display_hangman(guesses):
    """Display the hangman based on the number of guesses."""
    if guesses == 6:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("     /|\ ")
        print("     / \ ")
        print("  -----")
    elif guesses == 5:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("     /|\ ")
        print("     /  ")
        print("  -----")
    elif guesses == 4:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("     /|\ ")
        print("   ")
        print("  -----")
    elif guesses == 3:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("     / ")
        print("   ")
        print("  -----")
    elif guesses == 2:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("   ")
        print("   ")
        print("  -----")
    elif guesses == 1:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("   ")
        print("   ")
        print("  -----")
    else:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("   ")
        print("   ")
        print("   ")

def play_hangman():
    """Play a game of hangman."""
    word = choose_word()
    guessed_letters = []
    guesses = 6
    blanks = ['_'] * len(word)

    print("Let's play Hangman!")
    print("_ " * len(word))
    print("\n")

    while guesses > 0 and '_' in blanks:
        display_hangman(guesses)
        guess = input("Please guess a letter or type 'quit' to exit: ").lower()

        if guess == 'quit':
            break

        if len(guess) != 1:
            print("Please input only one letter at a time.")
            print("\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            print("\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    blanks[i] = guess
        else:
            guesses -= 1
            print("Sorry, that letter is not in the word.")
            print("\n")

        print(" ".join(blanks))
        print("\n")

    if '_' not in blanks:
        print("Congratulations, you won! The word was: " + word)
    elif guesses == 0:
        display_hangman(guesses)
        print("Sorry, you lost. The word was: " + word)

if __name__ == '__main__':
    play_hangman()