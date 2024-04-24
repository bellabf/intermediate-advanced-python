from math import sqrt


class Point:
    def __init__(self, abs: int, ord: int) -> None:
        self.__x = abs
        self.__y = ord

    def getX(self):
        return self.__x

    def setX(self):
        # self.__x=val
        print("non modiafiable")

    x = property(getX, setX)

    @property
    def y(self):
        print("Donnée privée")
        return None

    @y.setter
    def y(self, val):
        self.__y = val

    def deplacer(self, dx: int, dy: int) -> None:
        self.__x += dx
        self.__y += dy

    def afficher(self) -> str:
        return f"x= {self.x}, y= {self.y}"

    def distance(self, tgt) -> float:
        dist = sqrt((self.x - tgt.x) ** 2 + (self.y - tgt.y) ** 2)
        return dist

    def __repr__(self) -> str:
        return f"(({self.x}, {self.y}))"

    def __str__(self):
        return self.afficher()

    # p1 - p2 -> retourne la distance
    def __sub__(self, other):
        return self.distance(other)

    # p1 > p2 -> x1 > x2 et y1 > y2
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


if __name__ == "__main__":
    p1 = Point(2, 3)
    print(p1)
    print(p1.afficher())

    p1.deplacer(-2, 1)
    print(p1.afficher())

    p2 = Point(3, 4)
    print(p2.afficher())
