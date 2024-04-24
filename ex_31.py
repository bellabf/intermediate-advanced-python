def pain(recheio):
    def sandwich(arg):
        print("</------\>")
        recheio(arg)
        print("<\_____/>")

    return sandwich


def salade(recheio):
    def sandwich(arg):
        print(" #######  ")
        recheio(arg)
        print("  ~~~~~~  ")

    return sandwich


@pain
@salade
def filler(arg):
    print(f"--{arg}--")


# pain(salade(filler))('j')

print(" \n sandwich")
filler("poulet")
print("\n")


print(" \n sandwich")
filler("brie")
print("\n")


print(" \n sandwich")
filler("veggie")
print("\n")
