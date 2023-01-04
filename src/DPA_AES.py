from matplotlib import pyplot as plt
import json
import random
import numpy as np
import pickle

# Importer la sbox : utiliser le sbox.txt ou le sbox.pickle (plus simple)
sbox = None

# Creer une fonction AES simplifiée (XOR + substitution par s-box)
# En entrée : 1 octet de la clé et 1 octet de texte à chiffrer
def aes(key_byte, clear_text_byte):
    return None


assert aes(0xAB, 0xEF) == 0x1B
assert aes(0x22, 0x01) == 0x26
print("AES OK!")

# Creer un tableau de n octets aléatoires (1000 devraient suffir)
# Ces octets representeront le premier octet de n echantillons de texte clair
clear_texts = None

# Calculer le chiffrement de ces textes clairs par la vraie clé
# On simule ici l'execution du début de l'algorithme AES sur l'objet
key = 0xAB
ciphered = None

# Rappel : La consommation est corrélée au nombre de bit à 1 dans le résultat
# Créer une fonction hamming_weight qui renvoie le nb de bts à 1 dans un octet
def hamming_weight(ciphered_text):
    return None


assert hamming_weight(0b00000000) == 0
assert hamming_weight(0b11111111) == 8
assert hamming_weight(0b10101010) == 4
assert hamming_weight(0b01101011) == 5
print("Hamming Weight OK!")

# Appliquer la fonction Hamming Weight aux textes chiffrés
# On simule l'analyse de consommation
consos = None

# On connait seulement : le texte clair & la consommation mesurée
# Tout le reste est caché et interne au microcontrolleur on ne s'en sert plus dans la suite
# On va donc supposer une valeur de clé "guess" :
guess = None

# Trier les "traces" en fonction de l'un des bits du resultat du chiffrement par la clé supposée (guess)
zeros = None
ones = None

# Calculer la consommation moyenne pour chacune des deux categories
m0 = None
m1 = None

# Calculer la difference entre les consommations moyenne
diff = None
print(diff)

# En faisant varier guess qu'observe t-on ?

# On va maintenant itérer sur chaque guess possible
# Plotter diff en fonction du guess
diffs = None

plt.figure()
plt.plot(diffs)
plt.show()

# Qu'observe t-on ?

# Essayer en enlevant la substitution de la fonction AES tronquée
# Qu'observe t-on ? Comment expliquer ce resultat ?

####
# Nous avons chiffré 1000 textes aléatoires de 32 octets à l'aide d'une clé AES de 32 octets
# Nous avons pour chaque texte clair calculé le hammer weight (~consommation)
# Retrouvez la clé !
# traces : tableau de couples (texte_clair, consommation)
# texte_clair : 32 octets aléatoires
# consommation : 32 entiers (hammer weight) representant la consommation
####

l = 32
traces = None

key = None
print("".join([chr(c) for c in key]))

# Dans la réalité il est difficile de savoir à quel moment (indice du tableau de trace)
# a réellement eu lieu la sortie de la fonction de substitution.
# Trouver une solution pour retrouver la clé sans avoir l'information de la position dans la trace.

key = None
print("".join([chr(c) for c in key]))

# Ouvrir les vraies traces
# Appliquer le même pricipe qu'avant pour trouver la clé

traces = None

key = None
print("".join([chr(c) for c in key]))


# Combien de traces (environ) sont reellement necessaires pour trouver la clé
# Faire le code pour créer une figure pour le mettre en evidence

