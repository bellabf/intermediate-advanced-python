def addition(*toto):
    somme = 0
    for nb in toto:
        somme += nb

    return somme


def moyenne(*toto):  # args
    somme = 0
    for nb in toto:
        somme += nb

    return somme / len(toto)


print(addition(1, 2, 3, 4, 5, 6, 7))
