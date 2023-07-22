"""
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
4 - gestion des cas d'erreurs

- fin du programme.

1 pouce = 2.54 cm
1 cm = 0.394 pouces

"""
print("******************* Programe pour convertir les cm en pouces et inversement ******************\n")

"""
conversion de l'unité choisie 1 a l'unité choisié 2:
"""


def choice_conv(unit1, unit2, facteur):
    val_entry = input(f"conversion de {unit1} vers {unit2} donnez une valeur (ou x pour exit): ")
    if val_entry == "x":
        print("fin du programme")
        return True
    try:
        val_float = float(val_entry)
    except ValueError:
        print("vous devez entrer une valeur numerique et utiliser un point si nombre decimal!")
        return choice_conv(unit1, unit2, facteur)
    val_convert = round(val_float * facteur, 2)
    print(f"la conversion de {val_float} {unit1} est : {val_convert} {unit2}")
    return False


""""  
demarrage du programme du programme
    while 1 gestion erreur entrer input
    while 2 execution du programme
"""
while True:
    choice = input("entrer 1 (cm to pouce) entre 2 (pouce to cm): ")
    if choice == "1" or choice == "2":
        break

    print("vous devez entrer un nombre parmis les choix disponible (1 et 2 dans ce cas)\n")

while True:
    if choice == "1":
        if choice_conv("cm", "pouce", 0.394):
            break
    if choice == "2":
        if choice_conv("pouce", "centimetre", 2.54):
            break


