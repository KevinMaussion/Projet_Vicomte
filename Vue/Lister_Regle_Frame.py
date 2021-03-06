from tkinter import *

from Modele.ListeRegle import ListeRegle


class Lister_Regle_Frame(Frame):
    def __init__(self, fenetre=None, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)

        self.master.title("Projet Vicomte")
        self.master.geometry('750x350')

        # Définition des frames
        self.frame_top = Frame(fenetre)
        self.frame_top.pack(side=TOP, fill=BOTH, expand=1)

        self.frame_bot = Frame(fenetre)
        self.frame_bot.pack(side=BOTTOM, fill=BOTH, expand=1)

        liste_regle = ListeRegle()
        liste_regle.charger_liste_regle('NOMLOGICIEL.ini')

        # ##############Frame du haut###################################
        self.liste = Listbox(self.frame_top, selectmode=SINGLE)
        i = 0
        for regle in liste_regle:
            self.liste.insert(i, regle)
            i += 1
        self.liste.pack(fill=BOTH)
        self.liste.bind('<<ListboxSelect>>', self.callback)

        # ##############Frame du bas###################################
        label = Label(self.frame_bot, text="Règle choisie :")
        label.pack(side=TOP)

        self.label_regle = Label(self.frame_bot, text="Aucune règle choisie.")
        self.label_regle.pack(side=TOP)

        self.button_validation = Button(self.frame_bot, text="Utiliser Règle")
        self.button_validation.pack(side=BOTTOM)

    def callback(self, event):
        self.label_regle.config(text=self.liste.get(self.liste.curselection()))
