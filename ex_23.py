def salutations(arg):
    def hi(nom):
        return f"hi {nom}"

    def by(nom):
        return f"by {nom}"

    if arg == "hi":
        return hi
    elif arg == "by":
        return by
    else:
        return default


b = salutations("by")("isabella")
print(b)
