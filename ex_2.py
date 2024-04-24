j_semaines = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
print(j_semaines[2])
print(j_semaines[-2])

# j_semaines.pop(4)
j_semaines = j_semaines[0:3] + j_semaines[4:]
print(j_semaines)

j_semaines[3] = "jeudi"
print(j_semaines)

# j_semaines.insert(5, "vendredi")
j_semaines = j_semaines[0:4] + ["vendredi"] + j_semaines[4:]
for i in j_semaines:
    print(i)
    if i == "vendredi":
        print("C'est le we")
