import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("TIC-TAC-TOE")
        self.master.configure(bg='black')  # Set background color to black

        self.buttons = []
        self.current_player = 'X'
        self.board = [' ']*9

        # Labels to display player symbols and leader board
        self.player_labels = [
            tk.Label(master, text='Player X', font=('Helvetica', 14), fg='blue', bg='black'),
            tk.Label(master, text='Player O', font=('Helvetica', 14), fg='yellow', bg='black'),
            tk.Label(master, text='Leaderboard', font=('Helvetica', 14), fg='white', bg='black')
        ]
        self.player_labels[0].grid(row=0, column=0, columnspan=3)
        self.player_labels[1].grid(row=0, column=3, columnspan=3)
        self.player_labels[2].grid(row=0, column=6, columnspan=3)

        for i in range(9):
            button = tk.Button(master, text='', width=6, height=3,
                               command=lambda digit=i: self.make_move(digit), bg='black', fg='white')
            button.grid(row=i // 3 + 1, column=i % 3)
            self.buttons.append(button)

        # Initialize leader board
        self.leaderboard = {'X': 0, 'O': 0}
        self.update_leaderboard()

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner() or self.check_tie():
                self.end_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.update_player_label()

    def update_player_label(self):
        self.player_labels[0].config(text=f"Player {self.current_player}", fg='blue' if self.current_player == 'X' else 'yellow')

    def check_winner(self):
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                        (0, 4, 8), (2, 4, 6)]            # diagonals
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != ' ':
                winner = self.board[pattern[0]]
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.update_leaderboard(winner)
                return True
        return False

    def check_tie(self):
        if ' ' not in self.board:
            messagebox.showinfo("Game Over", "Match Tied")
            return True
        return False

    def end_game(self):
        self.master.destroy()

    def update_leaderboard(self, winner=None):
        if winner:
            self.leaderboard[winner] += 1
        self.player_labels[2].config(text=f'Leaderboard\nX: {self.leaderboard["X"]}  O: {self.leaderboard["O"]}')

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
