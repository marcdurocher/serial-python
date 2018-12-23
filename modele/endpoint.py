import dill
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
with open('../estpair.bin', 'rb') as file:
    _estpair = dill.load(file)


run(host='localhost', port=8080, debug=True)
