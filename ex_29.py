# decorateur

# @nomdedecorateur
# def fonction():
#    pass
# decorateur - une fonction qui prend en arg une fonction et qui retourne une fonction


def decorateur(fct):
    def verification():
        print("j'execute ce que je veux avant")
        fct()
        print("j'ai fini de decorer")

    return verification


def a_decorer():
    print("decorez moi !")


print("****")
decorateur(a_decorer)()


@decorateur
def a_decorer():
    print("decorez moi !")


@decorateur
def intouchable():
    print("je suis a decoree a vie")


print("****")
a_decorer()
print("****")
intouchable()
