def pain(recheio):
    def sandwich():
        print("</------\>")
        recheio()
        print("<\_____/>")

    return sandwich


@pain
def filler():
    print("--~~~~~~~--")


print(" \n sandwich")
filler()
print("\n")
