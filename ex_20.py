# closure


def salutation():
    def bonjour():
        return "Bonjour"

    return bonjour()


salutation()
