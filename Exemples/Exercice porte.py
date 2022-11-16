# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:54:44 2022

@author: toufl
00002 master
branche 1 master
"""

import random
from tkinter import Tk, Button, Label

def cree_portes(liste_de_porte, final= False):
    Label(ma_fen, text= "Choisissez une porte").grid(column= 0, row= 0, padx= 5, pady= 5, columnspan= len(liste_de_porte))
    compt = 0
    for porte in liste_de_porte:
        # global porte_gagnante
        bouton = Button(ma_fen, text= porte)
        if not(final):
            bouton.bind("<Button-1>", choix_porte)
            
        else:
            bouton.bind("<Button-1>", choix_porte_final)
        if porte == porte_gagnante:
            bouton.configure(bg= 'pink')
        bouton.grid(column= compt, row= 1, padx= 5, pady= 5)
        compt = compt + 1

def suppr_portes():
    for widget in ma_fen. winfo_children():
        # print(widget)
        widget.destroy()
        # print(widget)

def choix_porte(event):
    porte_choisie = event.widget.cget('text')
    supprime_porte_de_liste(porte_gagnante, porte_choisie)
    suppr_portes()
    cree_portes(liste_de_porte, True)

def choix_porte_final(event):
    porte_choisie = event.widget.cget('text')
    suppr_portes()
    ma_fen.update_idletasks()
    
    if porte_choisie == porte_gagnante:
        Label(ma_fen, text= "Gagné !!!!").grid(column= 0, row= 0, padx= 5, pady= 5)
    else:
        Label(ma_fen, text= "Perdu ...").grid(column= 0, row= 0, padx= 5, pady= 5)
    
def supprime_porte_de_liste(porte_gagnante, porte_choisie):
    global liste_de_porte
    liste_supprimable = list(liste_de_porte)
    liste_supprimable.remove(porte_choisie)
    if porte_gagnante in liste_supprimable:
        liste_supprimable.remove(porte_gagnante)
    porte_a_supprimer = random.choice(liste_supprimable)
    liste_de_porte.remove(porte_a_supprimer)

def charge_liste():
    global liste_de_porte
    liste_de_porte = [
        "porte_1",
        "porte_2",
        "porte_3",
        # "porte_4",
        # "porte_5",
        # "porte_6",
        ]

liste_de_porte = []
charge_liste()
# tirage porte gagnante
porte_gagnante = random.choice(liste_de_porte)

ma_fen = Tk()
ma_fen.title("Jeu de la porte")
ma_fen.geometry("300x200+500+400")
ma_fen.configure(background= 'grey')

charge_liste()
cree_portes(liste_de_porte)

ma_fen.mainloop()

# test git