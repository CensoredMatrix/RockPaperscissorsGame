import random
from collections import Counter
import tkinter as tk
from tkinter import messagebox
#colors
default_bg_color="#262626"
hover_bg="444444"
reset_default_bg_color="red"
reset_hover_bg="#ff4d4d"
bg_color = ["#1e1e1e", "#2a2a2a", "#333333", "#444444", "#555555"]

# Score tracking
user_score = 0
computer_score = 0
ties = 0
user_choices = []  # Stores user choices for AI learning

# Hover effect functions for game buttons
def change_bg_color(index=0):
    """Smooth background color transition"""
    root.configure(bg=bg_color[index])  # Change the window background color
    index = (index + 1) % len(bg_color)  # Move to the next color in the list
    root.after(1500, change_bg_color, index)  # Schedule the function to run again in 1.5 seconds

def on_enter_game(event):
    event.widget.config(bg=hover_bg)

def on_leave_game(event):
    event.widget.config(bg=default_bg)

# Hover effect functions for the reset button
def on_enter_reset(event):
    event.widget.config(bg=reset_hover_bg)

def on_leave_reset(event):
    event.widget.config(bg=reset_default_bg)


def get_computer_choice():
    """AI adapts by countering the user's most frequent choice."""
    if user_choices:
        most_common = Counter(user_choices).most_common(1)[0][0]
        counter_choice = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        return counter_choice[most_common]
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    global user_score, computer_score, ties
    if user == computer:
        ties += 1
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"
def countdown(count, user_choice):
    """Handles the 3-second countdown before revealing choices."""
    if count > 0:
        result_label.config(text=f"{count}")
        root.after(1000, countdown, count -1, user_choice)
    else:
        reveal_choices(user_choice)
def reveal_choices(user_choice):
    """Reveals the AI's choice and determines the winner."""
    user_choices.append(user_choice)
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer - {ties} Ties")
def flash_bg(color, step=0) :
    """flashes the background color when a player wins or loses"""  
    if step <4:
        root.configure(bg=color if step % 2==0 else default_bg) 
        root.after(300, flash_bg, color , step + 1)
    else :
        root.configure (bg=default_bg)                       
# Smooth result animation (scale up effect)
    for size in range(14, 22, 2):  # Increase font size
        result_label.after(size * 10, lambda s=size: result_label.config(font=("Arial", s)))
    result_label.after(300, lambda: result_label.config(font=("Arial", 14)))  # Reset font size
    flash_bg(color) #flash the background color for a win or a loss
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer - {ties} Ties")
def button_click_animation(btn, user_choice):
    """Shrinks button slightly when clicked, then starts countdown."""
    btn.config(font=("Arial", 10))  # Shrink
    root.after(100, lambda: btn.config(font=("Arial", 12)))  # Restore size
    result_label.config(text="Starting countdown...")
    root.after(1000, countdown, 5, user_choice)
def play(user_choice):
    """User selects a choice, and the countdown starts."""
    result_label.config(text="Starting countdown...")
    root.after(1000, countdown, 3, user_choice)  # Start 3-second countdown
 

def reset_game():
    """Resets the game scores and updates the display."""
    global user_score, computer_score, ties, user_choices
    user_score = 0
    computer_score = 0
    ties = 0
    user_choices = []
    result_label.config(text="Let's Play!")
    score_label.config(text="Score: You 0 - 0 Computer - 0 Ties")
    root.configure(bg=default_bg)
    #Hover effect funtions
    def on_enter(event):
        event.widget.config(bg=hover_bg)

# GUI window Elements
root = tk.Tk()
root.title("Rock Paper Scissors AI")
root.geometry("400x400")
root.configure(bg="#1e1e1e")

# Heading
heading = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
heading.pack(pady=10)

# Display Result
result_label = tk.Label(root, text="Let's Play!", font=("Arial", 14), fg="white", bg="#1e1e1e")
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(root, text="Score: You 0 - 0 Computer - 0 Ties", font=("Arial", 12), fg="white", bg="#1e1e1e")
score_label.pack(pady=10)

# Buttons for choices
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack()
#rock button
rock_btn = tk.Button(btn_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10, pady=10)
rock_btn.bind("<Enter>", on_enter_game)
rock_btn.bind("<Leave>",on_leave_game)
#paper button
paper_btn = tk.Button(btn_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10, pady=10)
paper_btn.bind("<Enter>",on_enter_game)
paper_btn.bind("<Leave>",on_leave_game)
#scissors button
scissors_btn = tk.Button(btn_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10, pady=10)
scissors_btn.bind("<Enter>", on_enter_game)
scissors_btn.bind("<Leave>",on_leave_game)
# Reset button
reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12), bg="red", fg="white", command=reset_game)
reset_btn.pack(pady=20)
reset_btn.bind("<Enter>", lambda event: reset_btn.config(bg="#ff4d4d"))
reset_btn.bind("leave>", lambda event: reset_btn.config(bg="red"))

#backbround animation
change_bg_color()

root.mainloop()
