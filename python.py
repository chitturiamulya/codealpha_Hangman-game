import random

# Predefined list of words
word_list = ["apple", "bread", "chair", "plant", "mouse"]

# Choose a random word from the list
secret_word = random.choice(word_list)

# Set for guessed letters and wrong attempts
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Function to display current state of the word
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

print("🎮 Welcome to Hangman!")
print("Guess the word. You have 6 incorrect tries.\n")

# Main game loop
while wrong_guesses < max_wrong:
    print(f"Word: {display_word()}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        if all(letter in guessed_letters for letter in secret_word):
            print(f"🎉 Congratulations! You guessed the word: {secret_word}")
            break
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_wrong - wrong_guesses} tries left.\n")

if wrong_guesses == max_wrong:
    print(f"😢 Game Over! The word was: {secret_word}")
