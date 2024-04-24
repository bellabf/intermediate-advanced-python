print("module debut")
print("module", __name__)  # part 2

a = 5

print("module milieu")


def addition(a, b):
    return a + b


def sqrt(a):
    return a  # purposely wrong


print("module fin")
