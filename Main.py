from Modele.ListeRegle import *
from Modele.Regle import *
from Modele.Renommage import *

extension_list = [".docx", ".txt"]
test = []
path_to_save_file = r"C:\Users\Wizkalista\Desktop\NOMLOGICIEL.ini"
path_to_folder = os.path.abspath(r"C:\Users\Wizkalista\Desktop\test")

regle = Regle()

regle.regle("amorce", "a partir de", "prefixe_", True, "_postfixe", test)


rename = Renommage(path_to_folder,  regle)

liste_a_sauvegarder = ListeRegle()
liste_a_charger = ListeRegle()

liste_a_sauvegarder.creation_liste(regle)

print(regle)

for e in liste_a_sauvegarder:
    print("Voici les objets dans la liste à sauvegarder dans le fichier: {}".format(e))

liste_a_sauvegarder.sauvegarder_liste_regle(path_to_save_file)

liste_a_charger.charger_liste_regle(path_to_save_file)

for e in liste_a_charger:
    print("Voici les objets dans la liste chargé à partir du fichier: {}".format(e))

rename.renommer()