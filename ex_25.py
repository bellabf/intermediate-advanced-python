# etat de la fonction


def generateur_puissance(exp):
    def puissance(nb):
        return nb**exp

    return puissance


p = generateur_puissance(2)
p1 = generateur_puissance(3)

print(id(p))
print(id(p1))
print(p(3))
print(p1(3))
