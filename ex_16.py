def addition(val1, val2):
    somme = val1 + val2
    return somme


def afficherpers(nom, prenom):
    print(f"{nom}, {prenom}")


l = [6, 7]

print(addition(l[0], l[1]))
print(addition(*l))

d = {"nom": "Bicalho", "prenom": "Isabella"}
afficherpers(**d)
