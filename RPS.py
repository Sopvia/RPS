from random import randint
import tkinter as tk
import customtkinter


class window(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, fg_color='#FFF3F5')

        self.font = customtkinter.CTkFont(family='Georgia', size=12)

        self.player = customtkinter.CTkLabel(self, text="Player", text_color='#FF92A5', font=(self.font, 14), height=8, width=8)
        self.player.grid(row=0, column=0, padx=20, sticky="ew")

        self.vs = customtkinter.CTkLabel(self, text="vs", text_color='#FF92A5', font=(self.font, 14), height=8, width=8)
        self.vs.grid(row=0, column=1, padx=20, sticky="ew")

        self.computer = customtkinter.CTkLabel(self, text="Computer", text_color='#FF92A5', font=(self.font, 14), height=8, width=8)
        self.computer.grid(row=0, column=2, padx=20, sticky="ew")

        self.rock = customtkinter.CTkButton(self, text="Rock", text_color="white", font=(self.font, 14), height=8, width=8, fg_color="#FFC0CB", hover_color="#FF92A5", command=lambda: action("Rock"))
        self.rock.grid(row=3, column=0, padx=20, sticky="ew")

        self.paper = customtkinter.CTkButton(self, text="Paper", text_color="white", font=(self.font, 14), height=8, width=8, fg_color="#FFC0CB", hover_color="#FF92A5", command=lambda: action("Paper"))
        self.paper.grid(row=3, column=1, padx=20, sticky="ew")

        self.scissors = customtkinter.CTkButton(self, text="Scissors", text_color="white", font=(self.font, 14), height=8, width=8, fg_color="#FFC0CB", hover_color="#FF92A5", command=lambda: action("Scissors"))
        self.scissors.grid(row=3, column=2, padx=20, sticky="ew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=3)
        self.grid_rowconfigure(3, weight=3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


        def action(x):
            self.rock.grid_forget()
            self.paper.grid_forget()
            self.scissors.grid_forget()

            self.result_player = customtkinter.CTkLabel(self, text_color='#FF92A5', font=(self.font, 14))
            self.result_player.grid(row=1, column=0, padx=20, sticky='ew')

            self.result_computer = customtkinter.CTkLabel(self, text_color='#FF92A5', font=(self.font, 14))
            self.result_computer.grid(row=1, column=2, padx=20, sticky='ew')

            self.outcome = customtkinter.CTkLabel(self, text_color='#FF92A5', font=(self.font, 14))
            self.outcome.grid(row=2, column=1, padx=20, sticky='ew')
            
            choice = ["Rock", "Paper", "Scissors"]
            computer = choice[randint(0,2)]
            match x:
                case "Rock":
                    player = "Rock"
                case "Paper":
                    player = "Paper"
                case "Scissors":
                    player = "Scissors"

            if player == computer:
                outcome_text = 'Tie!'
            elif player == "Rock":
                if computer == "Paper":
                    outcome_text = 'You lose! Computer covers player'
                else:
                    outcome_text = 'You win! Player smashes computer'
            elif player == "Paper":
                if computer == "Scissors":
                    outcome_text = 'You lose! Computer cuts player'
                else:
                    outcome_text = 'You win! Player covers computer'
            elif player == "Scissors":
                if computer == "Rock":
                    outcome_text = 'You lose! Computer smashes player'
                else:
                    outcome_text = 'You win! Player cuts computer'

            self.result_player.configure(text=player)
            self.result_computer.configure(text=computer)
            self.outcome.configure(text=outcome_text)

            self.restart = customtkinter.CTkButton(self, text="Try again", text_color="white", font=(self.font, 14), fg_color="#FFC0CB", hover_color="#FF92A5", command=tryagain, height=8, width=8)
            self.restart.grid(row=3, column=1, padx=20, sticky="ew")

        def tryagain():
            self.result_player.configure(text='')
            self.result_computer.configure(text='')
            self.outcome.configure(text='')

            self.restart.grid_forget()
            self.rock.grid(row=3, column=0, padx=20, sticky="ew")
            self.paper.grid(row=3, column=1, padx=20, sticky="ew")
            self.scissors.grid(row=3, column=2, padx=20, sticky="ew")


class root(customtkinter.CTk):
    def __init__(self):
        super().__init__(fg_color="white")
        self.geometry("500x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title('Rock Paper Scissors (cute version)')
        self.iconbitmap('icon.ico')

        self.window_frame = window(master=self)
        self.window_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = root()
app.mainloop()