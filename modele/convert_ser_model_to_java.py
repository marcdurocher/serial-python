import dill
import getopt
import sys
import os

import m2cgen as m2c

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
        global model
        model = dill.load(file)

    #
    # Create a Java File Source
    # Class Name : Modelo
    # Package Name: bzh.marcdurocher.prediction
    #
    java_file = m2c.export_to_java(model,"bzh.marcdurocher.prediction","Modelo")

    #
    # Create directory structure for Java source
    # respective to the package name
    #
    if not os.path.exists("./bzh/marcdurocher/prediction/"):
        os.makedirs("./bzh/marcdurocher/prediction/")

    with open("./bzh/marcdurocher/prediction/Modelo.java", "w") as file:
        file.write(java_file)


if __name__ == "__main__":
    main()

