eleve = [("math", 15), ("histoire", 6), ("francais", 12), ("anglais", 10), ("sport", 3)]

list_order = []
min_note = 100
min_mat = ""
taille_list = len(eleve)

while len(list_order) < taille_list:
    for mat, note in eleve:
        if min_note >= note:
            min_note = note
            min_mat = mat

    list_order.append((min_mat, min_note))
    eleve.remove((min_mat, min_note))

print(list_order)
