from pileexcpt import PileException, PilePleineException, PileVideException


class Pile:
    def __init__(self, taille, elements) -> None:
        self.elements = taille
        self.taille = elements

    def empiler(self, elmt):
        if len(self) < self.taille:
            self.elements.append(elmt)
        else:
            raise PilePleineException

    def depiler(self):
        if len(self) > 0:
            return self.elements.pop()

        raise PileVideException


if __name__ == "__main__":
    p = Pile(2)
    p.empile(1)
    print("e1")
    p.empiler(2)
    print("e2")

    try:
        p.empiler(3)
    except PileException as e:
        print(e)
