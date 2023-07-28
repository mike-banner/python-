import string
from tkinter import *
from random import randint, choice


def generate_passw():
    password_min = 8
    password_max = 12
    all_charts = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_charts) for x in range(randint(password_min, password_max)))
    passw_entry.delete(0, END)
    passw_entry.insert(0, password)


# creation de la fenetre
window = Tk()
window.title("Generateur de mot de passe")
window.geometry("720x480")
window.config(bg="#ccd3f9")

# frame principal
frame = Frame(window, bg="#ccd3f9")

# image
height = 300
width = 300
image = PhotoImage(file="password-img.png")
canva = Canvas(frame, height=height, width=width, bg="#ccd3f9", bd=0, highlightthickness=0)
canva.create_image(width/2, height/2, image=image)

# grid pour aligner element 1
canva.grid(row=0, column=0, sticky="w") # sticky ou la situé par rapport a une boussole

# Frame de droite
R_frame = Frame(frame, bg="#ccd3f9")

# composant de la frame de droite
label_title = Label(R_frame, text="Mot de passe", font=("arial", 20),bg="#ccd3f9", fg="black")
label_title.pack()
passw_entry = Entry(R_frame, font=("arial", 20),bg="white", fg="grey")
passw_entry.pack()
generator_passw = Button(R_frame, text="generer", font=("arial, 20"),bg="#ccd3f9", command=generate_passw)
generator_passw.pack(fill="x")  # fill prend toute la place dans la frame

# grid pour aligner element 2
R_frame.grid(row=0, column=1, sticky="w")

# afficher frame principal
frame.pack(expand=YES)

# fenetre
window.mainloop()