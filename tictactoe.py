import tkinter as tk
from tkinter import messagebox

#game logic
def check_winner():
    #rows
    if btn1['text'] == btn2['text'] == btn3['text'] != " ": return True
    if btn4['text'] == btn5['text'] == btn6['text'] != " ": return True
    if btn7['text'] == btn8['text'] == btn9['text'] != " ": return True
    
    #columns
    if btn1['text'] == btn4['text'] == btn7['text'] != " ": return True
    if btn2['text'] == btn5['text'] == btn8['text'] != " ": return True
    if btn3['text'] == btn6['text'] == btn9['text'] != " ": return True
    
    #diagonals
    if btn1['text'] == btn5['text'] == btn9['text'] != " ": return True
    if btn3['text'] == btn5['text'] == btn7['text'] != " ": return True
    
    return False

def check_draw():
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
    for btn in buttons:
        if btn['text'] == " ":
            return False
    return True

def button_click(btn):
    # Only allow the move if the button is empty
    if btn['text'] == " ":
        btn.config(text="X") # Player is always X
        
        if check_winner():
            messagebox.showinfo("Game Over", "You win!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            label.config(text="AI is thinking...")
            root.after(500, ai_move)

def reset_game():
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
    for btn in buttons:
        btn.config(text=" ")
    label.config(text="TIC TAC TOE")

#smart ai logic
def get_board_list():
    return [btn1['text'], btn2['text'], btn3['text'], 
            btn4['text'], btn5['text'], btn6['text'], 
            btn7['text'], btn8['text'], btn9['text']]

def check_win_state(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # cols
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def minimax(board, depth, is_maximizing):
    if check_win_state(board, "O"): return 10 - depth  # AI wins
    if check_win_state(board, "X"): return depth - 10  # Player wins
    if " " not in board: return 0                      # Draw

    if is_maximizing: # AI's turn to simulate
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score

    else: 
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    board = get_board_list()
    best_score = -float('inf')
    best_move = -1

    # AI tests all available spots
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
    if best_move != -1:
        buttons[best_move].config(text="O")
        
        if check_winner():
            messagebox.showinfo("Game Over", "AI wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            label.config(text="Your Turn (X)")

#gui setup
root = tk.Tk()
root.geometry("400x450")
root.configure(bg="#242424")

root.configure(bg="#242424")
label = tk.Label(root, text="TIC TAC TOE",font=("Arial", 20), bg="#242424", fg="yellow")
label.grid(row=0,column=0, pady=20)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

label.grid(row=0, column=0, columnspan=3)
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=3)
for i in range(3):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

#buttons
btn1= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn1))
btn1.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

btn2= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn2))
btn2.grid(row = 0, column = 1, sticky="nsew", padx=1, pady=1)

btn3= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn3))
btn3.grid(row = 0, column = 2, sticky="nsew", padx=1, pady=1)

btn4= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn4))
btn4.grid(row = 1, column = 0, sticky="nsew", padx=1, pady=1)

btn5= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width  = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn5))
btn5.grid(row = 1, column = 1, sticky="nsew", padx=1, pady=1)

btn6= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn6))
btn6.grid(row = 1, column = 2, sticky="nsew", padx=1, pady=1)

btn7= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn7))
btn7.grid(row = 2, column = 0, sticky="nsew", padx=1, pady=1)

btn8= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn8))
btn8.grid(row = 2, column = 1, sticky="nsew", padx=1, pady=1)

btn9= tk.Button(frame, text=" ",font=("Arial", 11, "bold"), width = 10, height = 5,bg="#E6F372", fg="black", command=lambda: button_click(btn9))
btn9.grid(row = 2, column = 2, sticky="nsew", padx=1, pady=1)

root.mainloop()