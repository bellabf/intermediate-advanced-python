"""
Interface entre le rectangle et la base de données

--> pas de requete, classe et obj
--> ORM


"""

import sqlite3 as sql
from forme import Rectangle, Point


class RectangleDB:
    # __init__
    def __init__(self):
        self.con = sql.connect("rectangle.db")
        self.cur = self.con.cursor()

    def creertable(self):
        try:
            self.cur.execute("CREATE TABLE rectangle(Long, Larg, x, y)")
        except:
            print("ATTENTION la table existe déja")

    # conection
    # def connection(self):

    # recuperer les rectangles

    def listeRectangle(self):
        rectangles = self.cur.execute("SELECT * FROM rectangle")
        listR = []

        for rect in rectangles.fetchall():
            #r = (L, l, x, y) -> Rectangle (l, L, Point(x, y))
            rectObj = Rectangle(rect[1], rect[0], Point(rect[2], rect[3]))
            listR.append(rectObj)

        return listR
    

    # enregistrer un rectangle

    def getRectangle(self, l):
        r = self.cur.execute(f"SELECT * FROM rectangle WHERE Long={l}")
        rect = r.fetchone()
        return Rectangle(rect[1], rect[0], Point(rect[2], rect[3]))


    def enregistrer(self, r):
        self.cur.execute(
            f"INSERT INTO rectangle VALUES({r.long}, {r.larg}, {r.origine.x}, {r.origine.y})"
        )
    
        self.con.commit()

    def __enter__(self):
        self.cur = self.con.cursor()
        return self
    
    def __exit__(self, type, value, traceback):
        self.cur.close()

    
if __name__ == "__main__":
    '''db = RectangleDB()
        db.creertable()
        db.enregistrer(Rectangle(10, 23, Point(9, 1)))

        for i in db.listeRectangle():
            print(i)

        print("***************")
        print(db.getRectangle(9))
    '''

    with RectangleDB() as db:

        print(db.getRectangle(2))

    print("la connection est fermée")