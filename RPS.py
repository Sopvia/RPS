from random import randint
import tkinter as tk
import customtkinter
from customtkinter import *
from PIL import Image


language = "english"


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
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)


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

            if computer == "Rock":
                if language == "german":
                    computerText = "Stein"
                elif language == "english":
                    computerText = "Rock"
            elif computer == "Paper":
                if language == "german":
                    computerText = "Papier"
                elif language == "english":
                    computerText = "Paper"
            elif computer == "Scissors":
                if language == "german":
                    computerText = "Schere"
                elif language == "english":
                    computerText = "Scissors"

            match x:
                case "Rock":
                    player = "Rock"
                    if language == "german":
                        playerText = "Stein"
                    elif language == "english":
                        playerText = "Rock"
                case "Paper":
                    player = "Paper"
                    if language == "german":
                        playerText = "Papier"
                    elif language == "english":
                        playerText = "Paper"
                case "Scissors":
                    player = "Scissors"
                    if language == "german":
                        playerText = "Schere"
                    elif language == "english":
                        playerText = "Scissors"

            if player == computer:
                if language == "german":
                    outcome_text = "Unentschieden!"
                elif language == "english":
                    outcome_text = "Tie!"
            elif player == "Rock":
                if computer == "Paper":
                    if language == "german":
                        outcome_text = "Sie verlieren! Computer deckt Spieler"
                    elif language == "english":
                        outcome_text = 'You lose! Computer covers player'
                else:
                    if language == "german":
                        outcome_text = "Sie haben gewonnen! Spieler zertrümmert Computer"
                    elif language == "english":
                        outcome_text = 'You win! Player smashes computer'
            elif player == "Paper":
                if computer == "Scissors":
                    if language == "german":
                        outcome_text = "Sie verlieren! Computer schneidet Spieler"
                    elif language == "english":
                        outcome_text = 'You lose! Computer cuts player'
                else:
                    if language == "german":
                        outcome_text = "Sie haben gewonnen! Spieler deckt Computer"
                    elif language == "english":
                        outcome_text = 'You win! Player covers computer'
            elif player == "Scissors":
                if computer == "Rock":
                    if language == "german":
                        outcome_text = "Sie haben verloren! Computer zerschlägt Spieler"
                    elif language == "english":
                        outcome_text = 'You lose! Computer smashes player'
                else:
                    if language == "german":
                        outcome_text = "Sie haben gewonnen! Spieler schneidet Computer"
                    elif language == "english":
                        outcome_text = 'You win! Player cuts computer'

            self.result_player.configure(text=playerText)
            self.result_computer.configure(text=computerText)
            self.outcome.configure(text=outcome_text)

            retry = customtkinter.CTkImage(light_image=Image.open("retry.png"), dark_image=Image.open("retry.png"), size=(20, 20))

            self.restart = customtkinter.CTkButton(self, image=retry, text="", fg_color="#FFC0CB", hover_color="#FF92A5", command=tryagain, height=8, width=8)
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
        self.geometry("600x500")
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title('Rock Paper Scissors (cute version)')
        self.iconbitmap('icon.ico')

        self.font = customtkinter.CTkFont(family='Georgia', size=12)

        self.window_frame = window(master=self)
        self.window_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")


        def switchLanguage():
            global language
            if language == "english":
                language = "german"
            else:
                language = "english"

            if language == "german":
                playerText = "Spieler"
                rockText = "Stein"
                paperText = "Papier"
                scissorsText = "Schere"
            elif language == "english":
                playerText = "Player"
                rockText = "Rock"
                paperText = "Paper"
                scissorsText = "Scissors"


            self.window_frame.player.configure(text=playerText)
            self.window_frame.rock.configure(text=rockText)
            self.window_frame.paper.configure(text=paperText)
            self.window_frame.scissors.configure(text=scissorsText)


        self.language = customtkinter.CTkButton(self, text="De/En", text_color="white", font=(self.font, 14), fg_color="#FFC0CB", hover_color="#FF92A5", command=switchLanguage, height=8, width=8)
        self.language.grid(row=0, column=0, padx=20, sticky="ns")


app = root()
app.mainloop()