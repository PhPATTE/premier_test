# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:54:44 2022

@author: toufl
"""

import random

liste_de_porte = [
    "porte_1",
    "porte_2",
    "porte_3",
    # "porte_4",
    # "porte_5",
    # "porte_6",
    ]

# tirage porte gagnante
porte_gagnante = random.choice(liste_de_porte)
print("Gagnante =", porte_gagnante)

# print("liste_de_porte", liste_de_porte)
choix_1 = input("Saisir un numéro de porte (" + str(liste_de_porte) + ") : ")
choix_1 = "porte_" + choix_1 
print("Choix 1 =", choix_1)

liste_de_supprimable = list(liste_de_porte)
liste_de_supprimable.remove(porte_gagnante)

if choix_1 in liste_de_supprimable:
    liste_de_supprimable.remove(choix_1)

print("liste_de_supprimable", liste_de_supprimable)

porte_a_supprimer = random.choice(liste_de_supprimable)
print("porte_a_supprimer", porte_a_supprimer)

liste_de_porte.remove(porte_a_supprimer)
print("liste_de_porte", liste_de_porte)
print("")

print("vous aviez choisi la porte :", choix_1)
choix_2 = input("Saisir un numéro de porte (" + str(liste_de_porte) + ") : ")
choix_2 = "porte_" + choix_2 
print("Choix 2 =", choix_2)

if choix_2 == porte_gagnante:
    print("vous avez Gagné !!!!!")
else:
    print("vous avez perdu, la porte gagnante était la", porte_gagnante)

