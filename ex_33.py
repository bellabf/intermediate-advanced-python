# exercice 1
# decorateur qui verifie que les arg que je passe sont du type str

# exercice 2
# il prend en argument une liste de type acceptés

def dec_str(fct):
    
    def verifie_parms(*args):
        v=True
        for i in [isinstance(element, str) for element in args]:
            if not i:
                print(-1)
                v=False
                break

        if v:
            fct(*args) 

    return verifie_parms

def dec_all(type, *args):

    def wrapper(fct):
    def verifie_parms(*args):
        v=True
        for i in [isinstance(element, type) for element in args]:
            if not i:
                print(-1)
                v=False
                break

        if v:
            fct(*args) 

    return verifie_parms


@dec_str
def names(*args):
    print(f'first argument {args[0]}')

@dec_all(int)
def sames(*args):
    print(f'first argument {args[0]}')

print('\n str type')
names("name", "another_name")
names("name", "another_name", 3)
names(3)

print('\n int type')
sames("name", "another_name")
sames("name", "another_name", 3)
sames(3)
