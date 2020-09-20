import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
canvas = tk.Canvas(root, height=100, width=300, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


def pedir_pass():
    frame.destroy()
    frame2 = tk.Frame(root, bg="white")
    frame2.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    legenda_pass = Label(frame2, text="Introduza a password")
    legenda_pass.pack()
    nome_pass = Entry(frame2, width=20)
    nome_pass.pack()
    nomeBotao = tk.Button(frame2, text="Ir", padx=10, pady=5, fg="white", bg="#263D42")
    nomeBotao.pack()




def pedir_user():

    legenda_user = Label(frame, text="Introduza o nome de utilizador")
    legenda_user.pack()

    nome_user = Entry(frame, width=20)
    nome_user.pack()

    nomeBotao = tk.Button(frame, text="Ir", padx=10, pady=5, fg="white", bg="#263D42", command=pedir_pass)
    nomeBotao.pack()


pedir_user()
root.mainloop()