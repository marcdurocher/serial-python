"""
HTTP endpoint
"""
import dill
import getopt
import sys

from bottle import route, run


@route('/api/<number:int>')
def estpair(number):
    """

    :param number: parametre de type entier attendu. Controle et transforme par le framework bottle
    :return: retourne un dictionnaire qui est transforme en reponse HTTP de type application/json
    """
    rv = {"number": number, "estPair": _estpair(number)}
    return rv

#
# Importation de la fonction a partir du fichier "binaire"
#
# remarque: si le fichier estpair.bin n'est pas present il faut
# le generer en executant le programme Python fonction_predictive
#


def main():
    """
    Fonction principale
    :return: code retour
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], None, ['file='])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(-1)

    nomfichier = None

    for o, a in opts:
        if o == "--file":
            nomfichier = a

    if not nomfichier:
            print("Nom de fichier attendu avec l'option --file <nom fichier>")
            sys.exit(-2)

    with open(nomfichier, 'rb') as file:
        global _estpair
        _estpair = dill.load(file)

    run(host='localhost', port=8080, debug=True)


if __name__ == "__main__":
    main()
