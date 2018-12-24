"""
generate bin function
"""
import dill
import sys


def serialize(fn, filename):
    """
    Serialise la fonction <fn> passee en parametre
    :param filename: nom du fichier a produire
    :param fn: fonction a serialiser
    :return: neant
    """

    with open(filename, "wb") as file:
        dill.dump(fn, file)


def estpair(n):
    """
    Fonction binaire qui retourne Vrai pour les parametres entiers pairs
    :param n: entier
    :return: True si n est pair, False sinon
    """
    return n % 2 == 0


def main():
    filename = './function.bin'
    if len(sys.argv) == 2:
        filename =sys.argv[1]
    serialize(estpair, filename)


if __name__ == "__main__":
    main()
