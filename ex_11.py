a = 1


def nomfct():
    print("globals", globals())
    print("locals 1", locals())
    global a
    a = 2
    print("locals 2", locals())
    print("mafonction", a)
