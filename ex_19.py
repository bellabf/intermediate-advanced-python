# fonction qui retourne une fonction


def salutation():
    def hello():
        return "hello"

    return hello


h = salutation()
print(h())
print(salutation()())


# check address
