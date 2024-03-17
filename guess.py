import tkinter as tk
import random

def check_guess():
    try:
        guess = int(entry_guess.get())
        if guess == secret_number:
            result_label.config(text=f"Congratulations! You guessed it right in {attempts} attempts.")
        elif guess < secret_number:
            result_label.config(text="Too low! Try again.")
        else:
            result_label.config(text="Too high! Try again.")
        entry_guess.delete(0, tk.END)
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Guess a number between 1 and 100.")
    entry_guess.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Number Guessing Game")

# Generate a secret number
secret_number = random.randint(1, 100)
attempts = 0

# Guess entry
guess_label = tk.Label(window, text="Enter Your Guess:")
guess_label.pack(pady=5)
entry_guess = tk.Entry(window)
entry_guess.pack(pady=5)

# Check button
check_button = tk.Button(window, text="Check Guess", command=check_guess)
check_button.pack(pady=5)

# Result label
result_label = tk.Label(window, text="Guess a number between 1 and 100.")
result_label.pack(pady=5)

# New game button
new_game_button = tk.Button(window, text="New Game", command=new_game)
new_game_button.pack(pady=5)

window.mainloop()
