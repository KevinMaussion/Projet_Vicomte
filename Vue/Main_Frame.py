from tkinter import *


class Interface(Frame):
    def __init__(self, fenetre=None, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=580, **kwargs)

        # Creation de la barre de menu
        self.barremenu = Menu(fenetre)

        # Creation du menu "Règles"
        self.regles = Menu(self.barremenu, tearoff=0)
        self.barremenu.add_cascade(label="Règles", underline=0, menu=self.regles)
        self.regles.add_command(label="Lister les règles", underline=0, command=self.lister)
        self.regles.add_command(label="Créer une règle", underline=0, command=self.creer)
        self.regles.add_command(label="Quitter", underline=0, command=self.quitter)

        # Creation du menu "?"
        self.aide = Menu(self.barremenu, tearoff=0)
        self.barremenu.add_cascade(label="?", underline=0, menu=self.aide)

        # Afficher le menu
        fenetre.config(menu=self.barremenu)

        # Définition des frames
        frametop = Frame(fenetre, width=768, height=290)
        frametop.pack(side=TOP)

        framebot = Frame(fenetre, width=768, height=290)
        framebot.pack(side=BOTTOM)

        ###############Frame du haut###################################
        Label(frametop, text="Nom du répertoire").grid(row=3, column=2)
        Label(frametop, text="Renommer en lots").grid(row=2, column=3)
        nomdurep = Entry(frametop).grid(row=3, column=3)
        Label(frametop, text="").grid(row=3, column=5)
        Label(frametop, text="").grid(row=6, column=5)

        # Photo
        photo = PhotoImage(file="vicomte.gif")
        label1 = Label(frametop, image=photo)
        label1.image = photo
        label1.grid(row=5, column=5, columnspan=2, sticky=NW)

        ###############Frame du bas###################################

        # Amorce
        Label(framebot, text="Amorce").grid(row=1, column=1)
        var_choix = StringVar()

        choix_aucune = Radiobutton(framebot, text="Aucune", variable=var_choix, value="Aucune")
        choix_lettre = Radiobutton(framebot, text=" Lettre   ", variable=var_choix, value="Lettre")
        choix_chiffre = Radiobutton(framebot, text="Chiffre  ", variable=var_choix, value="Chiffre")
        choix_aucune.grid(row=2, column=1)
        choix_lettre.grid(row=3, column=1)
        choix_chiffre.grid(row=4, column=1)

        Label(framebot, text="A partir de").grid(row=5, column=1)
        Apartir = Entry(framebot, width=5).grid(row=6, column=1)
        Label(framebot, text="").grid(row=7, column=1)
        Label(framebot, text="").grid(row=7, column=6)

        # Prefixe
        Label(framebot, text="Préfixe").grid(row=1, column=2)
        prepost = StringVar()
        choix_pre = Radiobutton(framebot, variable=prepost, value="pre")
        choix_pre.grid(row=2, column=2)

        # Nom du fichier
        Label(framebot, text="Nom du fichier", borderwidth=8).grid(row=1, column=4)
        choix_nom_fi = StringVar()
        choix_nomorig = Radiobutton(framebot, variable=choix_nom_fi, value="original")
        Label(framebot, text="Nom original").grid(row=2, column=4)
        choix_nomsaisi = Radiobutton(framebot, variable=choix_nom_fi, value="saisi")
        nom_saisi = Entry(framebot, width=11).grid(row=3, column=4)
        choix_nomorig.grid(row=2, column=3)
        choix_nomsaisi.grid(row=3, column=3)
        """fin nom du fichier"""

        # Postixe
        Label(framebot, text="Postfixe", borderwidth=8).grid(row=1, column=5)
        choix_post = Radiobutton(framebot, variable=prepost, value="post")
        choix_post.grid(row=2, column=5)

        Label(framebot, text="Extension concernée").grid(row=1, column=6)

        Button(framebot, text='Renommer', width=10).grid(row=6, column=6)

        Button(framebot, text='Retour', width=10, command=fenetre.destroy).grid(row=8, column=6)

    def creer(self):
        root = Tk()
        root.title("Créer une règle")

        # Définition des frames
        frametop = Frame(root, width=768, height=290)
        frametop.pack(side=TOP)

        framebot = Frame(root, width=768, height=290)
        framebot.pack(side=BOTTOM)

        ###############Frame du haut###################################
        Label(frametop, text="Nom du répertoire").grid(row=3, column=2)
        Label(frametop, text="Renommer en lots").grid(row=2, column=3)
        nomdurep = Entry(frametop).grid(row=3, column=3)
        Label(frametop, text="").grid(row=3, column=5)
        Label(frametop, text="").grid(row=6, column=5)

        # Photo
        # photo = PhotoImage(file="vicomte.gif")
        # label1 = Label(frametop, image=photo)
        # label1.image = photo
        # label1.grid(row=5, column=5, columnspan=2, sticky=NW)

        ###############Frame du bas###################################

        # Amorce
        Label(framebot, text="Amorce").grid(row=1, column=1)
        var_choix = StringVar()

        choix_aucune = Radiobutton(framebot, text="Aucune", variable=var_choix, value="Aucune")
        choix_lettre = Radiobutton(framebot, text=" Lettre   ", variable=var_choix, value="Lettre")
        choix_chiffre = Radiobutton(framebot, text="Chiffre  ", variable=var_choix, value="Chiffre")
        choix_aucune.grid(row=2, column=1)
        choix_lettre.grid(row=3, column=1)
        choix_chiffre.grid(row=4, column=1)

        Label(framebot, text="A partir de").grid(row=5, column=1)
        Apartir = Entry(framebot, width=5).grid(row=6, column=1)
        Label(framebot, text="").grid(row=7, column=1)
        Label(framebot, text="").grid(row=7, column=6)

        # Prefixe
        Label(framebot, text="Préfixe").grid(row=1, column=2)
        prepost = StringVar()
        choix_pre = Radiobutton(framebot, variable=prepost, value="pre")
        choix_pre.grid(row=2, column=2)

        # Nom du fichier
        Label(framebot, text="Nom du fichier", borderwidth=8).grid(row=1, column=4)
        choix_nom_fi = StringVar()
        choix_nomorig = Radiobutton(framebot, variable=choix_nom_fi, value="original")
        Label(framebot, text="Nom original").grid(row=2, column=4)
        choix_nomsaisi = Radiobutton(framebot, variable=choix_nom_fi, value="saisi")
        nom_saisi = Entry(framebot, width=11).grid(row=3, column=4)
        choix_nomorig.grid(row=2, column=3)
        choix_nomsaisi.grid(row=3, column=3)
        """fin nom du fichier"""

        # Postixe
        Label(framebot, text="Postfixe", borderwidth=8).grid(row=1, column=5)
        choix_post = Radiobutton(framebot, variable=prepost, value="post")
        choix_post.grid(row=2, column=5)

        Label(framebot, text="Extension concernée").grid(row=1, column=6)

        Button(framebot, text='Renommer', width=10).grid(row=6, column=6)

        Button(framebot, text='Retour', width=10, command=root.destroy).grid(row=8, column=6)
        root.mainloop()

    def lister(self):
        # fenetreLister.geometry("%dx%d%+d%+d" % (100, 400, 250, 200))
        pass

    def quitter(self):
        self.master.destroy()
