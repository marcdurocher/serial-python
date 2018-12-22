import dill

#
# Importation de la fonction a partir du fichier "binaire"
#
file = open("../mafonctionSerialisee.bin", "rb")
estPair = dill.load(file)
file.close()

#
# Invocation de la fonction récupérer
#

for i in range(10):
    print("%d est pair ? %s" % (i, estPair(i)))
