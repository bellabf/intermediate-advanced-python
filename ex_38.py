def division(n, m):
    if n < 0:
        # lever exception
        raise TypeError
    return n / m


try:
    division(6, 0)

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
