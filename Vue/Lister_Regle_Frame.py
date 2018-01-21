from tkinter import *

from Modele.ListeRegle import ListeRegle


class Lister_Regle_Frame(Frame):
    def __init__(self, fenetre=None, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)

        self.master.title("Projet Vicomte")
        self.master.geometry('750x350')

        # Définition des frames
        self.frame = Frame(fenetre)
        self.frame.pack(side=TOP, fill=BOTH)

        liste_regle = ListeRegle()
        liste_regle.charger_liste_regle('NOMLOGICIEL.ini')

        liste = Listbox(self.frame)
        i = 0
        for regle in liste_regle:
            liste.insert(i, regle)
            i += 1
        liste.pack(fill=BOTH)
