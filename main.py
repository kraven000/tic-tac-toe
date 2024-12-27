import customtkinter as ct
from tkinter.messagebox import showinfo
import random


WINNING_COMBINATION = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
icon = "icon.ico"

class TicTacToe(ct.CTk):
    def __init__(self):
        self.user = set()
        self.computer = set()
        self.winner = False
        
        super().__init__()
        
        self.geometry("363x467")
        self.configure(bg="white")
        self.iconbitmap(icon)
        
        # create table
        self.canvas = ct.CTkCanvas(self,border=0,borderwidth=0)
        self.canvas.pack(fill="both",expand=True,padx=0,pady=0)
        self.canvas.create_line(120,0,120,380,fill="black",width=3)
        self.canvas.create_line(240,0,240,380,fill="black",width=3)
        self.canvas.create_line(0,120,365,120,fill="black",width=3)
        self.canvas.create_line(0,240,365,240,fill="black",width=3)
        
        # to show turns
        self.restart = ct.CTkButton(self.canvas,text="RESTART",width=10,height=30,font=("Roboto",16),
                                    command=self.restart_game)
        self.restart.grid(column=1,row=10,padx=10,pady=50)
        
        # to track the buttons used by Computer and user
        self.buttons = {}
        
        self.buttons_used = [i+1 for i in range(9)]
        
        for i in range(9):
            btn = ct.CTkButton(self.canvas, text="", width=100, height=100,font=("Roboto",50),
                               bg_color="white",fg_color="white",border_width=0,border_spacing=0,
                               hover_color="white",border_color="white",text_color="black",
                               command=lambda x=i+1: self.logic(x))
            btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            self.buttons[i+1] = btn  
    
    def logic(self, button_number):
        # Handle player's move
        if button_number in self.user or button_number in self.computer or self.winner:
            return
        
        self.buttons[button_number].configure(text="X")
        self.user.add(button_number)
        self.buttons_used.remove(button_number)
        
        if self.check_winner(self.user):
            self.end_game("YOU WIN")
            return
        
        # Check for tie before computer's move
        if not self.buttons_used:
            self.end_game("IT'S A TIE")
            return
        
        # Computer's move
        comp = random.choice(self.buttons_used)
        self.buttons[comp].configure(text="O")
        self.computer.add(comp)
        self.buttons_used.remove(comp)

        if self.check_winner(self.computer):
            self.end_game("COMPUTER WINS")
            return

    def check_winner(self, player_moves):
        for combination in WINNING_COMBINATION:
            if combination.issubset(player_moves):
                return True
        return False

    def end_game(self, result):
        showinfo(title="Result", message=result)
        self.winner = True
        for button in self.buttons.values():
            button.configure(state="disabled")
        else:
            self.restart_game()

    def restart_game(self):
        # Reset the game state
        self.user.clear()
        self.computer.clear()
        self.winner = False

        # Reset the board buttons
        for i in self.buttons:
            self.buttons[i].configure(text="", state="normal")

        # Reset the available moves
        self.buttons_used = [i + 1 for i in range(9)]



if __name__ == "__main__":
    a = TicTacToe()
    a.mainloop()