"""
CodeAlpha Internship — Task 1: Hangman Game
Author  : [Your Name]
GitHub  : CodeAlpha_HangmanGame
"""

import random

# ── Hangman ASCII art stages (0 = full, 6 = empty gallows) ──────────────────
HANGMAN_STAGES = [
    # 0 wrong guesses
    """
   -----
   |   |
       |
       |
       |
       |
=========""",
    # 1 wrong guess
    """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
    # 2 wrong guesses
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
    # 3 wrong guesses
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
    # 4 wrong guesses
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    # 5 wrong guesses
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    # 6 wrong guesses — DEAD
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========""",
]

# ── Word bank ────────────────────────────────────────────────────────────────
WORDS = ["python", "hangman", "coding", "laptop", "keyboard"]


def display_board(wrong_count: int, guessed: set, word: str) -> None:
    """Print current game state."""
    print(HANGMAN_STAGES[wrong_count])
    print("\nWrong guesses left:", 6 - wrong_count)
    print("Letters guessed   :", " ".join(sorted(guessed)) if guessed else "—")

    # Show word progress
    display_word = " ".join(ch if ch in guessed else "_" for ch in word)
    print(f"\nWord: {display_word}\n")


def get_valid_input(guessed: set) -> str:
    """Prompt until the player enters a new, single alphabetical letter."""
    while True:
        letter = input("Guess a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("⚠  Please enter a single alphabetical letter.")
        elif letter in guessed:
            print(f"⚠  You already guessed '{letter}'. Try another.")
        else:
            return letter


def play_hangman() -> None:
    """Main game loop."""
    word        = random.choice(WORDS)
    guessed     = set()          # all letters guessed so far
    wrong_count = 0
    max_wrong   = 6

    print("\n" + "=" * 40)
    print("     Welcome to HANGMAN!  Good luck 🎯")
    print("=" * 40)

    while wrong_count < max_wrong:
        display_board(wrong_count, guessed, word)

        # Check win condition
        if all(ch in guessed for ch in word):
            print(f"🎉 Congratulations! You guessed the word: '{word.upper()}'")
            break

        letter = get_valid_input(guessed)
        guessed.add(letter)

        if letter in word:
            print(f"✅  Great! '{letter}' is in the word.")
        else:
            wrong_count += 1
            print(f"❌  '{letter}' is NOT in the word. ({max_wrong - wrong_count} chances left)")
    else:
        # Show final losing state
        display_board(wrong_count, guessed, word)
        print(f"💀 Game Over! The word was: '{word.upper()}'")

    # Ask to play again
    print()
    again = input("Play again? (y/n): ").strip().lower()
    if again == "y":
        play_hangman()
    else:
        print("Thanks for playing! 👋")


# ── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    play_hangman()
