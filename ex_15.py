def afficherpers_2(**tutu):  # kwargs
    print(tutu)
    for cle in tutu:
        print(tutu[cle])


def addition(*toto):
    somme = 0
    for nb in toto:
        somme += nb

    return somme


def lesdeux(*args, **kwargs):
    print(args)
    print(kwargs)


print(addition(1, 2, 3, 4, 5, 6, 7))
afficherpers_2(civ="Mme", prenom="Virginie", nom="Lopez")
lesdeux(4, "r", 8, val=1, toto="tutu")
