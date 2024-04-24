def division(n, m):
    pass


try:
    "a" / 5
except ZeroDivisionError:
    print("pas divisible par 0")
except TypeError as e:
    print(e)
except:
    print("erreur non connu")
else:
    print("si y a pas d'erreur")
finally:
    print("dans tout les cas")

print("la suite du programme")
