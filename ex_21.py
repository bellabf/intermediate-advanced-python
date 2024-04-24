def salutations(arg):
    def hi():
        return "hi"

    def by():
        return "by"

    if arg == "hi":
        return hi
    elif arg == "by":
        return by
    else:
        return None


b = salutations("by")
print(b)
