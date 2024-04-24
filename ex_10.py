import copy

t = (1, 2, 3, ["a", "b"])
t[3][1] = 4

t1 = copy.copy(t)
t2 = copy.deepcopy(t)
