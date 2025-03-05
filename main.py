import random
import tkinter as tk
from tkinter import messagebox
import art


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x400")
        self.num = random.randint(1, 100)
        self.turns = 0
        self.guesses_left = 0
        self.create_widgets()

    def create_widgets(self):
        logo_label = tk.Label(self.root, text=art.logo, font=("Courier", 10), padx=10, pady=10)
        logo_label.pack()
        welcome_label = tk.Label(self.root, text="Welcome to the Number Guessing Game!", font=("Arial", 12))
        welcome_label.pack(pady=5)
        instructions_label = tk.Label(self.root, text="I'm thinking of a number between 1 and 100", font=("Arial", 10))
        instructions_label.pack(pady=5)
        easy_button = tk.Button(self.root, text="Easy (10 turns)", command=self.easy_mode, width=20)
        easy_button.pack(pady=5)
        hard_button = tk.Button(self.root, text="Hard (5 turns)", command=self.hard_mode, width=20)
        hard_button.pack(pady=5)
        self.guess_label = tk.Label(self.root, text="Enter your guess:", font=("Arial", 10))
        self.guess_label.pack(pady=5)
        self.guess_entry = tk.Entry(self.root, width=20)
        self.guess_entry.pack(pady=5)
        self.submit_button = tk.Button(self.root, text="Submit Guess", state=tk.DISABLED, command=self.submit_guess)
        self.submit_button.pack(pady=5)
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.feedback_label.pack(pady=5)

    def easy_mode(self):
        self.turns = 10
        self.guesses_left = self.turns
        self.feedback_label.config(text=f"You have {self.turns} turns to guess the number.")
        self.submit_button.config(state=tk.NORMAL)

    def hard_mode(self):
        self.turns = 5
        self.guesses_left = self.turns
        self.feedback_label.config(text=f"You have {self.turns} turns to guess the number.")
        self.submit_button.config(state=tk.NORMAL)

    def submit_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number between 1 and 100.")
            return

        if guess < 1 or guess > 100:
            messagebox.showwarning("Out of Range", "Please guess a number between 1 and 100.")
            return

        self.guesses_left -= 1

        if guess > self.num:
            self.feedback_label.config(text=f"Too high! You have {self.guesses_left} turns left.")
        elif guess < self.num:
            self.feedback_label.config(text=f"Too low! You have {self.guesses_left} turns left.")
        else:
            messagebox.showinfo("Congratulations!", f"Congrats! You've found the number {self.num}.")
            self.reset_game()

        if self.guesses_left == 0 and guess != self.num:
            messagebox.showinfo("Game Over", f"Sorry, you have no turns left. The correct number was {self.num}.")
            self.reset_game()

    def reset_game(self):
        self.num = random.randint(1, 100)
        self.guesses_left = 0
        self.turns = 0
        self.guess_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.submit_button.config(state=tk.DISABLED)
        self.guess_label.config(text="Enter your guess:")


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

