import os

from Modele.Action import *


class Renommage(Action):

    def __init__(self, path_to_folder, regle):
        Action.__init__(self, path_to_folder, regle)

    def renommer(self):
        list_of_file = os.listdir(self._get_path_to_folder())
        os.chdir(self._get_path_to_folder())

        # Bloc concernant la variable _extension dans la règle.
        for file in list_of_file:

            # Si les fichiers doivent être renommés en fonctione de leur extension le prog entre dans le if.
            if self._get_regle()._get_extension():
                file_no_extension, file_extension = os.path.splitext(file)

                # Pour tous les fichiers du dossier, si l'un d'entre eux comporte une extension de la liste, on le modifie. On touche pas aux autres.
                for extension in self._get_regle()._get_extension():
                    if file_extension == extension:

                        # Bloc de code concernant la variable _nomfichier dans la règle.
                        j = 0
                        new_filename1 = file
                        if self._get_regle()._get_nomfichier() == True:
                            pass
                        elif self._get_regle()._get_nomfichier() == False:
                            new_filename1 = ""
                            os.rename(file, new_filename1)
                        else:
                            try:
                                new_filename1 = self._get_regle()._get_nomfichier()
                                os.rename(file, new_filename1)
                            except OSError:
                                new_filename1 = self._get_regle()._get_nomfichier() + str(j)
                                os.rename(file, new_filename1)
                                j = j + 1

                        # Bloc concernant la variable _prefixe dans la règle.
                        if self._get_regle()._get_prefixe() != "":
                            new_filename2 = self._get_regle()._get_prefixe() + new_filename1
                            os.rename(new_filename1, new_filename2)

                        # Bloc concernant la variable _postfixe dans la règle.
                        if self._get_regle()._get_postfixe() != "":
                            new_filename3 = new_filename2.replace(".", self._get_regle()._get_postfixe() + ".")
                            os.rename(new_filename2, new_filename3)

            # Si la liste des extensions est vide, on modifie tous les fichiers du dossier.
            else:
                # Bloc de code concernant la variable _nomfichier dans la règle.
                j = 0
                for file in list_of_file:
                    new_filename1 = file
                    if self._get_regle()._get_nomfichier() == True:
                        pass
                    elif self._get_regle()._get_nomfichier() == False:
                        new_filename1 = ""
                        os.rename(file, new_filename1)
                    else:
                        try:
                            new_filename1 = self._get_regle()._get_nomfichier()
                            os.rename(file, new_filename1)
                        except OSError:
                            new_filename1 = self._get_regle()._get_nomfichier() + str(j)
                            os.rename(file, new_filename1)
                            j = j + 1

                    # Bloc concernant la variable _prefixe dans la règle.
                    if self._get_regle()._get_prefixe() != "":
                        new_filename2 = self._get_regle()._get_prefixe() + new_filename1
                        os.rename(new_filename1, new_filename2)

                    # Bloc concernant la variable _postfixe dans la règle.
                    if self._get_regle()._get_postfixe() != "":
                        new_filename3 = new_filename2.replace(".", self._get_regle()._get_postfixe() + ".")
                        os.rename(new_filename2, new_filename3)
