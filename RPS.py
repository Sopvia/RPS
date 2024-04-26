from random import randint
from tkinter import *

window = Tk()
window.title('Rock Paper Scissors ')
window.geometry("500x500")

title = Label(window, text="Rock Paper Scissors (cute version)")
title.grid(row=0, column=0)

player = Label(window, text="Player").grid(row=1, column=1)
vs = Label(window, text="vs").grid(row=1, column=2)
computer = Label(window, text="Computer").grid(row=1, column=3)

result = Label(window, text="").grid(row=2, column=1)

rock = Button(window, text="Rock", width=6, cursor="heart").grid(row=3, column=1)
paper = Button(window, text="Paper", width=6, cursor="heart").grid(row=3, column=2)
scissors = Button(window, text="Scissors", width=6, cursor="heart").grid(row=3, column=3)

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

player = False
computer = t[randint(0,2)]