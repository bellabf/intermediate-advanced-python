# une fonction peut avoir pour aug une fonction
# fct(fct1)


def salut():
    return "bonjour"


def fairelabise(arg):  # arg = fct
    print("Je te dis")
    print(arg())
    print("et je te fais la bise")


fairelabise(salut)
