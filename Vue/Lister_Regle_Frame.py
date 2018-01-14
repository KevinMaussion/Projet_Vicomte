from tkinter import *


class Lister_Regle_Frame(Frame):
    def __init__(self, fenetre=None, **kwargs):
        Frame.__init__(self, fenetre, **kwargs, command=self.liste_regle())

        self.master.title("Projet Vicomte")
        self.master.geometry('750x350')

        # Définition des frames
        self.frame = Frame(fenetre, command=self.liste_regle())
        self.frame.pack()

    def liste_regle(self):
        liste = Listbox(self.frame)
        liste.pack()
