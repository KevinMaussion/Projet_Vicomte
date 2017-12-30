from tkinter import *


class Creer_Regle_Frame(Frame):
    def __init__(self, fenetre=None, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)

        self.master.title("Projet Vicomte")
        self.master.geometry('550x350')

        # Définition des frames
        frametop = Frame(fenetre)
        frametop.pack(side=TOP)

        framebot = Frame(fenetre)
        framebot.pack(side=BOTTOM)

        ###############Frame du haut###################################
        Label(frametop, text="Nom du répertoire").grid(row=3, column=2)
        Label(frametop, text="Renommer en lots").grid(row=2, column=3)
        self.var = StringVar()
        self.nomdurep = Entry(frametop, textvariable=self.var)
        self.var.set(r'C:\Users\Wizkalista\Desktop\test')
        self.nomdurep.grid(row=3, column=3)
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
        self.var_choix = StringVar(master=fenetre)

        choix_aucune = Radiobutton(framebot, text="Aucune", variable=self.var_choix, value="Aucune")
        choix_lettre = Radiobutton(framebot, text=" Lettre   ", variable=self.var_choix, value="Lettre")
        choix_chiffre = Radiobutton(framebot, text="Chiffre  ", variable=self.var_choix, value="Chiffre")
        choix_aucune.grid(row=2, column=1)
        choix_lettre.grid(row=3, column=1)
        choix_chiffre.grid(row=4, column=1)
        choix_aucune.select()

        Label(framebot, text="A partir de").grid(row=5, column=1)
        self.a_partir = Entry(framebot, width=5)
        self.a_partir.grid(row=6, column=1)

        # Prefixe
        Label(framebot, text="Préfixe").grid(row=1, column=2)
        # prepost = StringVar()
        self.choix_pre = Entry(framebot, width=5)
        self.choix_pre.grid(row=2, column=2)

        # Nom du fichier
        Label(framebot, text="Nom du fichier", borderwidth=8).grid(row=1, column=4)
        self.choix_nom_fi = StringVar()

        self.choix_nomorig = Radiobutton(framebot, variable=self.choix_nom_fi, value="original")
        Label(framebot, text="Conserver le nom originel").grid(row=2, column=4)

        self.choix_aucun_nom = Radiobutton(framebot, variable=self.choix_nom_fi, value="vide")
        Label(framebot, text="Ne pas conserver le nom originel").grid(row=3, column=4)

        l = LabelFrame(framebot, text="Changer le nom originel", padx=5, pady=5)
        l.grid(row=4, column=4)
        self.choix_nomsaisi = Radiobutton(framebot, variable=self.choix_nom_fi, value="saisi")
        self.w = Entry(l, text="test", width=11)
        self.w.pack()

        self.choix_nomorig.grid(row=2, column=3)
        self.choix_aucun_nom.grid(row=3, column=3)
        self.choix_nomsaisi.grid(row=4, column=3)
        self.choix_nomorig.select()
        """fin nom du fichier"""

        # Postixe
        Label(framebot, text="Postfixe", borderwidth=8).grid(row=1, column=5)
        self.choix_post = Entry(framebot, width=5)
        self.choix_post.grid(row=2, column=5)

        # Extension
        Label(framebot, text="Extension concernée").grid(row=1, column=6)
        self.choix_ext = Entry(framebot, width=5)
        self.choix_ext.grid(row=2, column=6)

        rename_button = Button(framebot, text='Renommer', width=10, command=self.renommage)
        rename_button.grid(row=6, column=6)

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

    def set_amorce(self):
        choix_amorce = self.var_choix.get()
        amorce = ""

        if choix_amorce == "Aucune":
            pass
        elif choix_amorce == "Lettre":
            if self.a_partir.get():
                amorce = self.a_partir.get()
            else:
                amorce = "a"
        elif choix_amorce == "Chiffre":
            if self.a_partir.get():
                amorce = self.a_partir.get()
            else:
                amorce = 0o01
        return amorce

    def set_nom_fichier(self):
        choix_nom = self.choix_nom_fi.get()
        nom_fichier = ""
        if choix_nom == "original":
            nom_fichier = True
        elif choix_nom == "vide":
            nom_fichier = False
        elif choix_nom == "saisi":
            nom_fichier = self.w.get()

        return nom_fichier

    def set_extension(self):
        extension = self.choix_ext.get()
        extension_list = extension.split(',')
        return extension_list

    # def renommage(self):
    #     directory_path = os.path.abspath(self.nomdurep.get())
    #
    #     regle = Regle()
    #     regle.prefixe = self.choix_pre.get()
    #     regle.postfixe = self.choix_post.get()
    #     regle.amorce = self.set_amorce()
    #     regle.nomfichier = self.set_nom_fichier()
    #     regle.extension = self.set_extension()
    #
    #     print("test: " + directory_path)
    #
    #     rename = Renommage(directory_path, regle)
    #     rename.renommer()
