"""
Creation d'interface graphique
fenetre - boutons - ouvrir - fermer
"""

from tkinter import *

# creation window
window = Tk()


# frame (boite)
frame_1 = Frame(window, bg="#ccd3f9")

# personalisation de la fenetre
window.title("application test")
window.geometry("1000x500")
window.iconbitmap("logo93.ico")
window.config(background='#ccd3f9')

# ajout d'un titre
label_title = Label(frame_1, text="bienvenue dans mon application", font=("arial", 30), bg="#ccd3f9")
label_title.pack()

# ajout d'un bouton
button_a = Button(frame_1, text="Ouvrir", font=("arial", 20))
button_a.pack()

frame_1.pack(expand=YES)

# affiche la fenetre
window.mainloop()