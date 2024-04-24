# decorateur de decorateur
# decorateur qui a pour arg: dessus et dessous


def dessus_dessous(dessus, dessous):  # createur de decorateur
    def choix(fct):
        def wrapper(arg):
            print(dessus)
            fct(arg)
            print(dessous)

        return wrapper

    return choix


@dessus_dessous("</''''''\>", "<\______/>")
def centre(arg):
    print(arg)


centre("---brie---")
