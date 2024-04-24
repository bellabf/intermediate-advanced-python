class MaClasse:
    """ma class qui fait rien pour l'instant"""

    def __init__(
        self, val1, val2
    ):  # constructeur /!\ l'objet etait deja cree ici par __new__ mais sans valeur
        self.att1 = val1
        self.att2 = val2

    def afficher(self):
        print(f"Mon objet a pour att1: {self.att1} et pour att2 : {self.att2}")


if __name__ == "__main__":
    # 1er
    obj = MaClasse(1, "r")
    print("obj.att1", obj.att1)
    obj.att1 = 5
    print("obj.att1", obj.att1)

    # 2eme
    obj1 = MaClasse("2", "v")
    print("obj1.att1", obj1.att1)
    print("obj1.att2", obj1.att2)
    obj1.afficher()
