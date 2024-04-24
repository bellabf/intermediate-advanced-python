def mafct():
    x = "virginie"

    def innerfc():
        x = "hello"

    innerfc()
    return x


def mafct_2():
    x = "virginie"

    def innerfc():
        nonlocal x
        x = "hello"

    innerfc()
    return x


print(mafct())

print(mafct_2())
