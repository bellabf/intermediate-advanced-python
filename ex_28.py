def test():
    return True


def fct(arg):
    def verification():
        if arg():
            print("ok")
        else:
            print("pas ok")

    return verification


print(fct(test))
fct(test)()
