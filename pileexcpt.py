# 3 exceptions
# PileException -> herite de Exception
# code : par default 22
# message : par default : erreur pile

# PilePleineException -> herite de PileException
# code 23
# message : 'pile pleine

# PileVideException -> herite de PileException
# code : 24
# message : pile vide


class PileException(Exception):
    def __init__(self, code=22, message="erreur pile"):
        self.message = message
        self.error_code = code

        Exception.__init__(self)

    def __str__(self):
        return f"ERROR {self.error_code}: {self.message}"


class PilePleineException(PileException):
    def __init__(self):
        PileException.__init__(self, code=23, message="Pile Pleine")


class PileVideException(PileException):
    def __init__(self):
        PileException.__init__(self, code=24, message="Pile Vide")
