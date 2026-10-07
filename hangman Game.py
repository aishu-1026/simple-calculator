import random

# Words for the game
words = [
    "python",
    "computer",
    "programming",
    "keyboard",
    "internet",
    "developer",
    "software",
    "hangman"
]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong attempts
wrong_attempts = 0
max_attempts = 6

print("================================")
print("        HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 wrong attempts.\n")

while wrong_attempts < max_attempts:

    # Display the hidden word
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    # Check whether the player won
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.\n")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is correct
    if guess in secret_word:
        print("✅ Correct guess!\n")
    else:
        wrong_attempts += 1
        print("❌ Wrong guess!")
        print("Attempts left:", max_attempts - wrong_attempts)
        print()

# Game over
if wrong_attempts == max_attempts:
    print("💀 GAME OVER!")
    print("The correct word was:", secret_word)
