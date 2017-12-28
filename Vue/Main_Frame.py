from tkinter import *


class Interface(Frame):
    def __init__(self, fenetre=None, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)

        self.master.title("Projet Vicomte")
        self.master.geometry('550x350')

        # Creation de la barre de menu
        self.barremenu = Menu(fenetre)

        # Creation du menu "Règles"
        self.regles = Menu(self.barremenu, tearoff=0)
        self.barremenu.add_cascade(label="Règles", underline=0, menu=self.regles)
        self.regles.add_command(label="Lister les règles", underline=0, command=self.lister)
        self.regles.add_command(label="Créer une règle", underline=0, command=self.creer)
        self.regles.add_separator()
        self.regles.add_command(label="Quitter", underline=0, command=self.quitter)

        # Creation du menu "?"
        self.barremenu.add_command(label="?", underline=0, command=self.software_information)

        # Afficher le menu
        fenetre.config(menu=self.barremenu)

        # Définition des frames
        frametop = Frame(fenetre)
        frametop.pack(side=TOP)

        framebot = Frame(fenetre)
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
        label1.grid(row=3, column=10, sticky=W)

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


        # Prefixe
        Label(framebot, text="Préfixe").grid(row=1, column=2)
        prepost = StringVar()
        choix_pre = Entry(framebot, width=5)
        choix_pre.grid(row=2, column=2)

        # Nom du fichier
        Label(framebot, text="Nom du fichier", borderwidth=8).grid(row=1, column=4)
        choix_nom_fi = StringVar()

        choix_nomorig = Radiobutton(framebot, variable=choix_nom_fi, value="original")
        Label(framebot, text="Conserver le nom originel").grid(row=2, column=4)

        choix_aucun_nom = Radiobutton(framebot, variable=choix_nom_fi, value="vide")
        Label(framebot, text="Ne pas conserver le nom originel").grid(row=3, column=4)

        l = LabelFrame(framebot, text="Changer le nom originel", padx=5, pady=5)
        l.grid(row=4, column=4)
        choix_nomsaisi = Radiobutton(framebot, variable=choix_nom_fi, value="saisi")
        w = Entry(l, text="test", width=11)
        w.pack()

        choix_nomorig.grid(row=2, column=3)
        choix_aucun_nom.grid(row=3, column=3)
        choix_nomsaisi.grid(row=4, column=3)
        """fin nom du fichier"""

        # Postixe
        Label(framebot, text="Postfixe", borderwidth=8).grid(row=1, column=5)
        choix_post = Entry(framebot, width=5)
        choix_post.grid(row=2, column=5)

        # Extension
        Label(framebot, text="Extension concernée").grid(row=1, column=6)
        choix_ext = Entry(framebot, width=5)
        choix_ext.grid(row=2, column=6)

        Button(framebot, text='Renommer', width=10).grid(row=6, column=6)


    def creer(self):
        root = Toplevel()
        root.title("Créer une règle")

        # Définition des frames
        frametop = Frame(root)
        frametop.pack(side=TOP)

        framebot = Frame(root)
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
        label1.grid(row=3, column=10, sticky=W)

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

        # Prefixe
        Label(framebot, text="Préfixe").grid(row=1, column=2)
        prepost = StringVar()
        choix_pre = Entry(framebot, width=5)
        choix_pre.grid(row=2, column=2)

        # Nom du fichier
        Label(framebot, text="Nom du fichier", borderwidth=8).grid(row=1, column=4)
        choix_nom_fi = StringVar()

        choix_nomorig = Radiobutton(framebot, variable=choix_nom_fi, value="original")
        Label(framebot, text="Conserver le nom originel").grid(row=2, column=4)

        choix_aucun_nom = Radiobutton(framebot, variable=choix_nom_fi, value="vide")
        Label(framebot, text="Ne pas conserver le nom originel").grid(row=3, column=4)

        l = LabelFrame(framebot, text="Changer le nom originel", padx=5, pady=5)
        l.grid(row=4, column=4)
        choix_nomsaisi = Radiobutton(framebot, variable=choix_nom_fi, value="saisi")
        w = Entry(l, text="test", width=11)
        w.pack()

        choix_nomorig.grid(row=2, column=3)
        choix_aucun_nom.grid(row=3, column=3)
        choix_nomsaisi.grid(row=4, column=3)
        """fin nom du fichier"""

        # Postixe
        Label(framebot, text="Postfixe", borderwidth=8).grid(row=1, column=5)
        choix_post = Entry(framebot, width=5)
        choix_post.grid(row=2, column=5)

        # Extension
        Label(framebot, text="Extension concernée").grid(row=1, column=6)
        choix_ext = Entry(framebot, width=5)
        choix_ext.grid(row=2, column=6)

        Button(framebot, text='Créer règle', width=10).grid(row=6, column=6)
        root.mainloop()

    def lister(self):
        # fenetreLister.geometry("%dx%d%+d%+d" % (100, 400, 250, 200))
        pass

    def software_information(self):
        root = Toplevel(width="500", height="500")
        root.title("Information Logiciel")

        labell = Label(root, text="Auteur du logiciel :")
        label2 = Label(root, text="Vicomte Sebban")
        label3 = Label(root, text="Version du logiciel :")
        label4 = Label(root, text="1.0")
        labell.grid(row=1, column=1)
        label2.grid(row=1, column=2)
        label3.grid(row=2, column=1)
        label4.grid(row=2, column=2)

        root.mainloop()

    def quitter(self):
        self.master.destroy()
