"""
Simple test

__author__ = Marc Durocher

"""
import dill

#
# Importation de la fonction a partir du fichier "binaire"
#
with open("../estpair.bin", "rb") as file:
    estpair = dill.load(file)

#
# Invocation de la fonction récupérer
#

for i in range(10):
    print("%d est pair ? %s" % (i, estpair(i)))
