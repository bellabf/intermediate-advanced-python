# syntax compréhension

l1 = list(range(0, 11))
print(l1)

l2 = []
for elm in l1:
    l2.append(elm * 4)

print("l2:", l2)

l3 = [elm * 4 for elm in l1]
print("l3:", l3)

# filtre avec compréhension

l4 = []

for elm in l3:
    if elm > 3:
        l4.append(elm)

print("l4:", l4)

l5 = [elem for elem in l3 if elem > 3]
print("l5:", l5)

l6 = [elm if elm > 3 else "a" for elm in l3]
print("l6:", l6)

print("**** Ex 5 ****")


n_l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("n_l1:", n_l1)

n_carre = [elm**2 for elm in n_l1]
print("carre:", n_carre)

n_impar = [elm for elm in n_l1 if elm % 2 != 0]
print("impair:", n_impar)

n_pair_cube = [elm**3 for elm in n_l1 if elm % 2 == 0]
print("cube pair:", n_pair_cube)
