# TASK 1: Hangman Game
import random

def hangman():
    words = ["python", "coding", "hangman", "computer", "program", "developer", "software", "algorithm"]
    word = random.choice(words).lower()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6
    
    # Create display word with underscores
    display_word = ["_" for _ in word]
    
    print("Welcome to Hangman!")
    print("Guess the word letter by letter")
    print(f"The word has {len(word)} letters")
    
    while wrong_guesses < max_wrong and "_" in display_word:
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Get user input
        guess = input("Enter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"Good! '{guess}' is in the word!")
            # Update display word
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
    
    # Game over
    print(f"\nFinal word: {' '.join(display_word)}")
    
    if "_" not in display_word:
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()