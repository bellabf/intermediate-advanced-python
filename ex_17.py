def serveur(ip, host, **kwargs):
    if ip is None and "ip" in kwargs:
        ip = kwargs["ip"]

    if host is None and "host" in kwargs:
        ip = kwargs["host"]

    if isinstance(ip, str) and isinstance(host, str):
        return True

    else:
        print("Argument missing")
        return False


print(serveur("11", "22"))
print(serveur(11, "22"))
print(serveur("11", 22))

k_dict = {"ip": "11111", "host": "111111"}

print(serveur(**k_dict))


k_dict = {"ip": "11111"}

print(serveur(host=22, **k_dict))
print(serveur(host="22", **k_dict))

k_dict = {"host": "11111"}
print(serveur(ip="1111", **k_dict))
print(serveur(ip=1111, **k_dict))

print(serveur(ip=1111, host="111", banana=1, kiwi=2))
print(serveur(ip="1111", host="111", banana=1, kiwi=2))
