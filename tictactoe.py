import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.game_over = False
        
        # Create the buttons
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text="", font=('Arial', 60), width=4, height=2,
                                   command=lambda row=i, col=j: self.clicked(row, col))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)
            
        # Create the status label
        self.status_label = tk.Label(master, text="Player {}'s turn".format(self.current_player), font=('Arial', 20))
        self.status_label.grid(row=3, column=0, columnspan=3)
        
        # Create the reset button
        self.reset_button = tk.Button(master, text="Reset", font=('Arial', 20), command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=3, sticky="nsew")
        
    def clicked(self, row, col):
        if self.buttons[row][col]['text'] == "" and not self.game_over:
            self.buttons[row][col]['text'] = self.current_player
            if self.check_win():
                self.status_label['text'] = "Player {} wins!".format(self.current_player)
                self.game_over = True
            elif self.check_tie():
                self.status_label['text'] = "It's a tie!"
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label['text'] = "Player {}'s turn".format(self.current_player)
    
    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False
    
    def check_tie(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True
    
    def reset(self):
        self.current_player = 'X'
        self.game_over = False
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
        self.status_label['text'] = "Player {}'s turn".format(self.current_player)
        
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
