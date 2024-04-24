print("*** Ex 1 ***")

list_1 = []

for i in range(1, 16, 2):
    list_1.append(i)

print(list_1)


list_2 = list(range(1, 16, 2))
print(list_2)

print("*** Ex 2 ***")
for i in range(0, -20, -2):
    print(i)

print("*** Ex 3 ***")
for i in range(0, 100):
    if i % 4 == 0:
        print(i)

print(list((range(0, 100, 4))))
