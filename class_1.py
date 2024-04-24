class MaClasse:
    """ma class qui fait rien pour l'instant"""

    def __init__(self):  # constructeur
        self.att1 = 1
        self.att2 = "r"


if __name__ == "__main__":
    # 1er
    obj = MaClasse()
    print("obj.att1", obj.att1)
    obj.att1 = 5
    print("obj.att1", obj.att1)

    # 2eme
    obj1 = MaClasse()
    print("obj1.att1", obj1.att1)
