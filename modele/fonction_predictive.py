import dill


def serialize(fn):
    """
    Serialise la fonction <fn> passee en parametre
    :param fn: fonction a serialiser
    :return: neant
    """

    fn_name = fn.__name__
    filename = "../%s.bin" % (fn_name,)
    with open(filename, "wb") as file:
        dill.dump(fn, file)


def estpair(n):
    """
    Fonction binaire qui retourne Vrai pour les parametres entiers pairs
    :param n: entier
    :return: True si n est pair, False sinon
    """
    return n % 2 == 0


for i in range(10):
    print("%d est pair ? %s" % (i, estpair(i)))

serialize(estpair)
