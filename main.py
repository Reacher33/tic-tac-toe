import tkinter as tk
from tkinter import messagebox
import random

# Initialize the game
root = tk.Tk()
root.title("Tic Tac Toe")

# Set initial variables
current_player = "X"
game_board = [" " for _ in range(9)]
game_over = False
vs_computer = False

# Create buttons for the game board
buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: handle_click(i))
    button.grid(row=row, column=col)
    buttons.append(button)


# Function to handle button clicks
def handle_click(i):
    global current_player, game_board, game_over, vs_computer
    if game_board[i] == " " and not game_over:
        game_board[i] = current_player
        buttons[i].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            game_over = True
        elif " " not in game_board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            game_over = True
        else:
            if vs_computer and current_player == "X":
                computer_move()
            else:
                current_player = "O" if current_player == "X" else "X"


# Function to check for a winner
def check_winner():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if game_board[condition[0]] == game_board[condition[1]] == game_board[condition[2]] != " ":
            for index in condition:
                buttons[index].config(bg='yellow')
            return True
    return False


# Function for computer move (random)
def computer_move():
    empty_cells = [i for i, val in enumerate(game_board) if val == " "]
    if empty_cells:
        computer_choice = random.choice(empty_cells)
        game_board[computer_choice] = "O"
        buttons[computer_choice].config(text="O")
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", "Computer wins!")
            game_over = True
        elif " " not in game_board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            game_over = True
        else:
            current_player = "X"


# Function to restart the game
def restart_game():
    global current_player, game_board, game_over
    current_player = "X"
    game_board = [" " for _ in range(9)]
    game_over = False
    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace")
    if vs_computer and current_player == "O":
        computer_move()


# Function to toggle playing against the computer
def toggle_player():
    global vs_computer
    vs_computer = not vs_computer
    restart_game()


# Button for restarting the game
restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3)

# Button for playing against the computer
player_button = tk.Button(root, text="Play vs Computer", command=toggle_player)
player_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
