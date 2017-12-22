from Modele.Regle import *
from Modele.ListeRegle import *

od = OrderedDict()
path_to_save_file = r"C:\Users\kmaussion\Desktop\test\NOMLOGICIEL.ini"

regle = Regle()
regle2 = Regle()

regle.regle("amorce", "a partir de", "prefixe", True, "postfixe", od)
regle2.regle("test", "test", "test", False, "test", od)

liste_a_sauvegarder = ListeRegle()
liste_a_charger = ListeRegle()

liste_a_sauvegarder.creation_liste(regle)
liste_a_sauvegarder.creation_liste(regle2)

print(regle)
print("Nombre d'objet dans la liste: {}".format(liste_a_sauvegarder.count()))


for e in liste_a_sauvegarder:
    print("Voici les objets dans la liste à sauvegarder dans le fichier: {}".format(e))

liste_a_sauvegarder.sauvegarder_liste_regle(path_to_save_file)

liste_a_charger.charger_liste_regle(path_to_save_file)

for e in liste_a_charger:
    print("Voici les objets dans la liste chargé à partir du fichier: {}".format(e))