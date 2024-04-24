from point import Point
from math import pi


class Forme:
    def __init__(self, p=Point(0, 0)) -> None:
        self.origine = p

    def deplacer(self, dx, dy):
        self.origine.deplacer(dx, dy)

    def perimetre(self):
        print("attention pas de perimetre")

    def surface(self):
        print("attention pas de surface")


class Rectangle(Forme):
    def __init__(self, l: int, L: int, p: Point = Point(0, 0)) -> None:
        self.long = L
        self.larg = l
        Forme.__init__(self, p)
        # super() another form

    def afficher(self):
        return f"origin at {self.origine.afficher()} with longueur = {self.long} and largeur = {self.larg}"

    def surface(self):
        return self.larg * self.long

    def perimetre(self):
        return 2 * (self.long + self.larg)
    
    def __str__(self):
        return self.afficher()


class Cercle:
    def __init__(self, rayon: int, p: Point = Point(0, 0)) -> None:
        self.rayon = rayon
        Forme.__init__(self, p)

    def afficher(self):
        return f"origin at {self.origine.afficher()} with rayon = {self.rayon}"

    def surface(self):
        return (self.rayon**2) * pi

    def perimetre(self):
        return 2 * self.rayon * pi


if __name__ == "__main__":
    p1 = Point(4, 7)
    r1 = Rectangle(2, 6, p1)
    r2 = Rectangle(7, 9, Point(2, 4))
    r3 = Rectangle(3, 4)

    r3.deplacer(2, 3)

    print(r3.origine.afficher())
    print(r3.afficher())
    print(f"perimetre = {r3.perimetre()}")
    print(f"surface = {r3.surface()}")

    c = Cercle(3)

    print(c.origine.afficher())
    print(c.afficher())
    print(f"perimetre = {c.perimetre()}")
    print(f"surface = {c.surface()}")
