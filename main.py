import pygame
from tkinter import *
import random
import time
from threading import Thread
import tkinter as tk
import tkinter as ttk
from PIL import Image, ImageTk
from tkinter.font import Font
from threading import Thread

# name input
namebox = ""
#player's life from start of each level
life = 3
#images for background
mainmenu = ("./Images/BackgroundMenu.png")
#images for characters
#

#Score, global score
score = 0


#to close menu
def on_close():
    global run
    run = False
    menu_a.destroy()
#to enable fullscreen
def toggle_fullscreen(event):
    global fullscreen
    fullscreen = not fullscreen
    menu_a.attributes('-fullscreen', fullscreen)

def menu():
    global menu_a
    global run
    global fullscreen

    # Create the main menu window
    menu_a = tk.Tk()

    # Define a custom font and its size
    Title = Font(menu_a, family="Fifties Movies", size=50)
    Subtitle = Font(menu_a, family="Fifties Movies", size=30)
    Butons = Font(menu_a, family="Franchise", size=25)
    # To run
    run = True
    fullscreen = False
    # here I define some aspects of the menu window
    bgmenu = tk.PhotoImage(file = "./Images/BackgroundMenu.png")
    menu_a.title("Vintage Space Game")
    menu_a.geometry("1280x720")
    lmenu = Label(menu_a, image=bgmenu)
    lmenu.pack()

    # Add some details to the menu window

    # Bind F11 to toggle fullscreen mode
    menu_a.bind("<F11>", toggle_fullscreen)

    # Set a custom close function
    menu_a.protocol("WM_DELETE_WINDOW", on_close)

    # Add text to the menu using the custom font
    GameTitle = Label(lmenu, text="Vintage Space Game", font=Title, fg="white", bg="black")
    GameTitle.place(relx=0.5, y=100, anchor=ttk.S)

    #level title and buttons of level #
    Levels = Label(lmenu, text="Levels", font=Subtitle, fg="white", bg="black")
    Levels.place(relx=0.275, rely=0.30, anchor=ttk.S)
    Level1 = ttk.Button(lmenu, text="Level 1", font=Butons,fg="White", bg="black", relief="flat")
    Level1.place(relx=0.275, rely=0.45, anchor=ttk.S)
    Level2 = ttk.Button(lmenu, text="Level 2", font=Butons, fg="White", bg="black", relief="flat")
    Level2.place(relx=0.275, rely=0.6, anchor=ttk.S)
    Level3 = ttk.Button(lmenu, text="Level 3", font=Butons, fg="White", bg="black", relief="flat")
    Level3.place(relx=0.275, rely=0.75, anchor=ttk.S)

    # everything else about the game
    About = Label(lmenu, text="About", font=Subtitle, fg="white", bg="black")
    About.place(relx=0.725, rely=0.30, anchor=ttk.S)
    Info = ttk.Button(lmenu, text="Information", font=Butons, fg="White", bg="black", relief="flat")
    Info.place(relx=0.725, rely=0.45, anchor=ttk.S)
    Instructions = ttk.Button(lmenu, text="Instructions", font=Butons, fg="White", bg="black", relief="flat")
    Instructions.place(relx=0.725, rely=0.6, anchor=ttk.S)
    Leaderboard = ttk.Button(lmenu, text="Leaderboard", font=Butons, fg="White", bg="black", relief="flat")
    Leaderboard.place(relx=0.725, rely=0.75, anchor=ttk.S)

    # Start the main loop
    menu_a.mainloop()

# Call the menu function
menu()