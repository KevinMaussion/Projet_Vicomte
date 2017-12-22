#Importation de module
from tkinter import *
import tkinter as tk

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        #Creation de la barre de menu
        self.barremenu = tk.Menu(self.master)

        #Creation du menu "Règles"
        self.regles = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "Règles", underline = 0, menu = self.regles)
        self.regles.add_command(label = "Lister les règles", underline = 0, command = self.lister)
        self.regles.add_command(label = "Créer une règle", underline = 0, command = self.creer)
        self.regles.add_command(label = "Quitter", underline = 0, command = self.quitter)

        #Creation du menu "?"
        self.aide = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "?", underline = 0, menu = self.aide)

        #Afficher le menu
        self.master.config(menu = self.barremenu)


        
    #Premier onglet du menu
    def lister(self):
        

        root = Tk()
        #root.geometry("%dx%d%+d%+d" %(1000,400,250,200))
        root.title("Lister les règles")
        
        """ defini les frames"""
        frametop=Frame(root,width=1000,height=400)
        frametop.pack(side=TOP)

        framebot=Frame(root,width=1000,height=400)
        framebot.pack(side=BOTTOM)

        """Partie du haut"""
        #Button(frametop,text='Lister',width=10).grid(row=1,column=0)


        Label(frametop,text = "Nom du répertoire").grid(row=3,column=2)
        Label(frametop,text = "Renommer en lots").grid(row=2,column=3)
        nomdurep = Entry(frametop).grid(row=3,column=3)
        Label(frametop,text = "").grid(row=3,column=5)
        Label(frametop,text = "").grid(row=6,column=5)
        
        """Photo qui marche pas"""
        photo = PhotoImage(file="arthur.png")
        canvas = Canvas(frametop,width=200,height=100)
        #canvas.create_image(0, 0,anchor=NW,image=photo)
        #canvas.pack()
        #Label(frametop,image=photo).grid(row=5,column=5)

        Label(frametop,text = "").grid(row=6,column=1)
        

        
        """ fin de partie du haut """

        """ Amorce """
        Label(framebot,text = "Amorce").grid(row=1,column=1)
        var_choix = StringVar()

        choix_aucune = Radiobutton(framebot, text="Aucune", variable=var_choix, value="Aucune")
        choix_lettre = Radiobutton(framebot, text=" Lettre   ", variable=var_choix, value="Lettre")
        choix_chiffre = Radiobutton(framebot, text="Chiffre  ", variable=var_choix, value="Chiffre")
        choix_aucune.grid(row=2,column=1)
        choix_lettre.grid(row=3,column=1)
        choix_chiffre.grid(row=4,column=1)

        Label(framebot,text = "A partir de").grid(row=5,column=1)
        Apartir = Entry(framebot,width=5).grid(row=6,column=1)
        Label(framebot,text = "").grid(row=7,column=1)
        Label(framebot,text = "").grid(row=7,column=6)
        #Label(framebot,text = "").grid(row=7,column=8)
        """Fin amorce """

        """Préfixe"""
        Label(framebot,text = "Préfixe").grid(row=1,column=2)
        prepost = StringVar()
        choix_pre = Radiobutton(framebot, variable=prepost, value="pre")
        choix_pre.grid(row=2,column=2)
        """Préfixe"""

        """Nom du fichier"""
        Label(framebot,text = "Nom du fichier", borderwidth=8).grid(row=1,column=4)
        choix_nom_fi = StringVar()
        choix_nomorig = Radiobutton(framebot, variable=choix_nom_fi, value="original")
        Label(framebot,text = "Nom original").grid(row=2,column=4)
        choix_nomsaisi = Radiobutton(framebot, variable=choix_nom_fi, value="saisi")
        nom_saisi = Entry(framebot,width=11).grid(row=3,column=4)
        choix_nomorig.grid(row=2,column=3)
        choix_nomsaisi.grid(row=3,column=3)
        """fin nom du fichier"""

        """Postfixe"""
        Label(framebot,text = "Postfixe", borderwidth=8).grid(row=1,column=5)
        choix_post = Radiobutton(framebot, variable=prepost, value="post")
        choix_post.grid(row=2,column=5)
        """fin postfixe"""



        Label(framebot,text = "Extension concernée").grid(row=1,column=6)



        Button(framebot,text='Renomer',width=10).grid(row=6,column=6)

        Button(framebot,text='Retour',width=10, command=root.destroy).grid(row=8,column=6)



        root.mainloop(  )

        


    def creer(self):
        fenetreLister = tk.Tk()
        fenetreLister.title("Creation d'un règle")
        fenetreLister.geometry("%dx%d%+d%+d" %(100,400,250,200))
        
    def quitter(self): self.master.destroy()


    #Deuxième onglet du menu
    def apropos(self):
        fenetreLister = tk.Tk()
        fenetreLister.title("A propos")
        fenetreLister.geometry("%dx%d%+d%+d" %(1000,400,250,200))
        
#Creation de la fenêtre
fenetre = tk.Tk()

#Titre de la fenêtre
fenetre.title("Renommage de fichier")
app = Application(fenetre)


#Taille de la fenêtre et sa position quand on lance l'appli
fenetre.geometry("%dx%d%+d%+d" %(1000,400,250,200))

Button(fenetre,text='Quitter',width=10,command =fenetre.destroy).grid(row=1,column=1)

#Démarage de la boucle Tkinter qui s'interompt quand on ferme
fenetre.mainloop()


