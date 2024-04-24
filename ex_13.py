def afficherpers(nom, prenom, civ):
    print(f"{civ} {nom}, {prenom}")


def afficherpers_2(**tutu):  # kwargs
    print(tutu)
    for cle in tutu:
        print(tutu[cle])


afficherpers("Lopez", "Virginie", "Mme")
afficherpers(nom="Lopez", prenom="Virginie", civ="Mme")
afficherpers(civ="Mme", prenom="Virginie", nom="Lopez")

afficherpers_2(civ="Mme", prenom="Virginie", nom="Lopez")
