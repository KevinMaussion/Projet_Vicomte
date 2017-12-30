from Vue.Main_Frame import *

# extension_list = [".docx", ".txt"]
# test = []
# path_to_save_file = "NOMLOGICIEL.ini"
# # path_to_folder = r"C:\Users\Wizkalista\Desktop\test"
#
# regle = Regle()
# regle2 = Regle()
# regle3 = Regle()
#
# regle.regle("aze", "a partir de", "prefixe_", True, "_postfixe", extension_list)
# regle2.regle("test", "a partir de", "prefixe_", True, "_postfixe", extension_list)
# regle3.regle("test", "test", "test", True, "test", test)
#
# # rename = Renommage(path_to_folder,  regle)
#
# liste_a_sauvegarder = []
# liste_a_charger = ListeRegle()
#
# # liste_a_sauvegarder.creation_liste(regle)
# liste_a_sauvegarder.append(regle2)
# liste_a_sauvegarder.append(regle3)
#
# print(regle)
# # print(liste_a_sauvegarder.count())
# for e in liste_a_sauvegarder:
#     print("Voici les objets dans la liste à sauvegarder dans le fichier: {}".format(e))
#
# # liste_a_sauvegarder.sauvegarder_liste_regle(path_to_save_file)
# #
# # liste_a_charger.charger_liste_regle(path_to_save_file)
# #
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
