from Vue.Main_Frame import *

# extension_list = [".docx", ".txt"]
# test = []
# path_to_save_file = r"C:\Users\Wizkalista\Desktop\NOMLOGICIEL.ini"
# path_to_folder = r"C:\Users\Wizkalista\Desktop\test"
#
# regle = Regle()
#
# regle.regle("aze", "a partir de", "prefixe_", True, "_postfixe", extension_list)
#
#
# rename = Renommage(path_to_folder,  regle)
#
# liste_a_sauvegarder = ListeRegle()
# liste_a_charger = ListeRegle()
#
# liste_a_sauvegarder.creation_liste(regle)
#
# print(regle)
#
# for e in liste_a_sauvegarder:
#     print("Voici les objets dans la liste à sauvegarder dans le fichier: {}".format(e))
#
# liste_a_sauvegarder.sauvegarder_liste_regle(path_to_save_file)
#
# liste_a_charger.charger_liste_regle(path_to_save_file)
#
# for e in liste_a_charger:
#     print("Voici les objets dans la liste chargé à partir du fichier: {}".format(e))
#
# rename.renommer()
#
# print(ord('z'))
# print(chr(97))

fenetre = Tk()
interface = Main_Frame(fenetre)
interface.mainloop()
