"""
Creation d'interface pour programme generateur de password
"""

from tkinter import *
import generator


def pass_program():
    generator.generator_win()


# creation window
master = Tk()


# frame (emplacement)
frame_1 = Frame(master, bg="#ccd3f9")

# personalisation de la fenetre
master.title("application test")
master.geometry("1000x500")
master.iconbitmap("logo93.ico")
master.config(bg='#ccd3f9')

# ajout d'un titre
label_title = Label(frame_1, text="Application generateur de mot de pass", font=("arial", 30), bg="#ccd3f9")
label_title.pack()

# ajout d'un bouton
button_a = Button(frame_1, text="Ouvrir", font=("arial", 20), )
button_a.pack()

frame_1.pack(expand=YES)

# affiche la fenetre
master.mainloop()