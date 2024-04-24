from math import sqrt


class Point:
    def __init__(self, abs: int, ord: int) -> None:
        self.x = abs
        self.y = ord

    def deplacer(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

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

    print(f"distance {p1.distance(p2)}")
    print(p1 - p2)
    print(p1 > p2)
