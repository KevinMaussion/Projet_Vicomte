import tkinter.filedialog
from tkinter import *

from Modele.Regle import *
from Modele.Renommage import *
from Vue.Creer_Regle_Frame import Creer_Regle_Frame


class Main_Frame(Frame):
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
        self.frametop = Frame(fenetre)
        self.frametop.pack(side=TOP)

        self.framebot = Frame(fenetre)
        self.framebot.pack(side=BOTTOM)

        ###############Frame du haut###################################
        Label(self.frametop, text="Nom du répertoire").grid(row=3, column=2)
        Label(self.frametop, text="Renommer en lots").grid(row=2, column=3)
        self.var = StringVar()
        button_dir_path = Button(self.frametop, text='Cliquez pour choisir un dossier', command=self.get_folder_path)
        button_dir_path.grid(row=3, column=2)

        Label(self.frametop, text="").grid(row=3, column=5)
        Label(self.frametop, text="").grid(row=6, column=5)

        # Photo
        photo = PhotoImage(file="vicomte.gif")
        label1 = Label(self.frametop, image=photo)
        label1.image = photo
        label1.grid(row=3, column=10, sticky=W)

        ###############Frame du bas###################################

        # Amorce
        Label(self.framebot, text="Amorce").grid(row=1, column=1)
        self.var_choix = StringVar(master=fenetre)

        choix_aucune = Radiobutton(self.framebot, text="Aucune", variable=self.var_choix, value="Aucune")
        choix_lettre = Radiobutton(self.framebot, text=" Lettre   ", variable=self.var_choix, value="Lettre")
        choix_chiffre = Radiobutton(self.framebot, text="Chiffre  ", variable=self.var_choix, value="Chiffre")
        choix_aucune.grid(row=2, column=1)
        choix_lettre.grid(row=3, column=1)
        choix_chiffre.grid(row=4, column=1)
        choix_aucune.select()

        Label(self.framebot, text="A partir de").grid(row=5, column=1)
        self.a_partir = Entry(self.framebot, width=5)
        self.a_partir.grid(row=6, column=1)


        # Prefixe
        Label(self.framebot, text="Préfixe").grid(row=1, column=2)
        # prepost = StringVar()
        self.choix_pre = Entry(self.framebot, width=5)
        self.choix_pre.grid(row=2, column=2)

        # Nom du fichier
        Label(self.framebot, text="Nom du fichier", borderwidth=8).grid(row=1, column=4)
        self.choix_nom_fi = StringVar()

        self.choix_nomorig = Radiobutton(self.framebot, variable=self.choix_nom_fi, value="original")
        Label(self.framebot, text="Conserver le nom originel").grid(row=2, column=4)

        self.choix_aucun_nom = Radiobutton(self.framebot, variable=self.choix_nom_fi, value="vide")
        Label(self.framebot, text="Ne pas conserver le nom originel").grid(row=3, column=4)

        l = LabelFrame(self.framebot, text="Changer le nom originel", padx=5, pady=5)
        l.grid(row=4, column=4)
        self.choix_nomsaisi = Radiobutton(self.framebot, variable=self.choix_nom_fi, value="saisi")
        self.w = Entry(l, text="test", width=11)
        self.w.pack()

        self.choix_nomorig.grid(row=2, column=3)
        self.choix_aucun_nom.grid(row=3, column=3)
        self.choix_nomsaisi.grid(row=4, column=3)
        self.choix_nomorig.select()
        """fin nom du fichier"""

        # Postixe
        Label(self.framebot, text="Postfixe", borderwidth=8).grid(row=1, column=5)
        self.choix_post = Entry(self.framebot, width=5)
        self.choix_post.grid(row=2, column=5)

        # Extension
        Label(self.framebot, text="Extension concernée").grid(row=1, column=6)
        self.choix_ext = Entry(self.framebot, width=5)
        self.choix_ext.grid(row=2, column=6)

        rename_button = Button(self.framebot, text='Renommer', width=10, command=self.renommage)
        rename_button.grid(row=6, column=6)


    def creer(self):
        root = Toplevel()
        root.title("Créer une règle")
        interface = Creer_Regle_Frame(root)
        interface.mainloop()


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

    def get_folder_path(self):
        self.var.set(tkinter.filedialog.askdirectory())
        print(self.var.get())
        self.nomdurep = Label(self.frametop, text=self.var.get())
        self.nomdurep.grid(row=3, column=3)

    def set_apartirde(self, txt):
        try:
            if txt:
                value = int(txt)
                return value
            else:
                return txt

        except ValueError:  # not an integer
            return txt

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
        if extension_list == ['']:
            extension_list = []
        print(extension_list)
        return extension_list

    def renommage(self):
        directory_path = os.path.abspath(self.var.get())

        regle = Regle()
        regle.prefixe = self.choix_pre.get()
        regle.postfixe = self.choix_post.get()
        regle.amorce = self.set_amorce()
        regle.nomfichier = self.set_nom_fichier()
        regle.extension = self.set_extension()
        regle.apartirde = self.set_apartirde(self.a_partir.get())
        rename = Renommage(directory_path, regle)
        rename.renommer()
