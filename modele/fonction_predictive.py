import dill


def serialize():
    """
    Serialise la fonction est Pair
    :return: neant
    """

    file = open("../mafonctionSerialisee.bin", "wb")
    dill.dump(estpair, file)
    file.close()


def estpair(n):
    """
    Fonction binaire qui retourne Vrai pour les parametres entiers pairs
    :param n: entier
    :return: True si n est pair, False sinon
    """
    return n % 2 == 0


for i in range(10):
    print("%d est pair ? %s" % (i, estpair(i)))

serialize()
