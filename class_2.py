class MaClasse:
    """ma class qui fait rien pour l'instant"""

    def __init__(self, val1, val2):  # constructeur
        self.att1 = val1
        self.att2 = val2


if __name__ == "__main__":
    # 1er
    obj = MaClasse(1, "r")
    print("obj.att1", obj.att1)
    obj.att1 = 5
    print("obj.att1", obj.att1)

    # 2eme
    obj1 = MaClasse("2", "v")
    print("obj1.att1", obj1.att1)
