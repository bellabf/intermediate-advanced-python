eleve = [("math", 15), ("histoire", 6), ("francais", 12), ("anglais", 10), ("sport", 3)]
print("eleve:", eleve)


inverse = [(note, matiere) for matiere, note in eleve]
print("inverse:", inverse)

inverse.sort()
eleve = [(matiere, note) for note, matiere in eleve]
print("inverse_sort:", eleve)
