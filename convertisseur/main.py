"""
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
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
    val_float = float(val_entry)
    val_convert = round(val_float * facteur, 2)
    print(f"la conversion de {val_float} {unit1} est : {val_convert} {unit2}")
    return False


#  demarrage du programme du programme
choice = input("entrer 1 (cm to pouce) entre 2 (pouce to cm): ")

while True:
    if choice == "1":
        if choice_conv("cm", "pouce", 0.394):
            break
    if choice == "2":
        if choice_conv("pouce", "centimetre", 2.54):
            break


