import os

from Modele.Action import *


class Renommage(Action):

    def __init__(self, path_to_folder, regle):
        Action.__init__(self, path_to_folder, regle)

    def renommer(self):
        list_of_file = os.listdir(self._get_path_to_folder())
        os.chdir(self._get_path_to_folder())
        amorce = self._get_regle()._get_amorce()
        # Bloc concernant la variable _extension dans la règle.
        for file in list_of_file:
            file_no_extension, file_extension = os.path.splitext(file)

            # Si les fichiers doivent être renommés en fonctione de leur extension le prog entre dans le if.
            if self._get_regle()._get_extension():

                # Pour tous les fichiers du dossier, si l'un d'entre eux comporte une extension de la liste, on le modifie. On touche pas aux autres.
                for extension in self._get_regle()._get_extension():
                    if file_extension == extension:

                        # Bloc de code concernant la variable _nomfichier dans la règle.
                        j = 0
                        new_filename = file
                        if self._get_regle()._get_nomfichier() == True:
                            pass
                        elif self._get_regle()._get_nomfichier() == False:
                            new_filename = "" + file_extension
                        else:
                            try:
                                new_filename = self._get_regle()._get_nomfichier()
                            except OSError:
                                new_filename = self._get_regle()._get_nomfichier() + str(j)
                                j = j + 1

                        # Bloc concernant la variable _prefixe dans la règle.
                        if self._get_regle()._get_prefixe() != "":
                            new_filename = self._get_regle()._get_prefixe() + new_filename

                        # Bloc concernant la variable _postfixe dans la règle.
                        if self._get_regle()._get_postfixe() != "":
                            new_filename = new_filename.replace(".", self._get_regle()._get_postfixe() + ".")

                        print(self._get_regle()._get_amorce())
                        print(isinstance(self._get_regle()._get_amorce(), int))

                        # Bloc concernant la variable _amorce dans la règle.
                        if amorce == "":
                            print("amorce = " + str(amorce))
                            pass
                        elif isinstance(amorce, str):
                            list_ascii = [ord(c) for c in amorce]
                            print(list_ascii)
                            if list_ascii[-1] < 122:
                                new_filename = amorce + new_filename
                                list_ascii[-1] = list_ascii[-1] + 1
                                list_char = [chr(c) for c in list_ascii]
                                amorce = ''.join(list_char)
                            else:
                                new_filename = amorce + new_filename
                                list_ascii[-1] = 97
                                list_ascii.append(list_ascii[-1])
                                list_char = [chr(c) for c in list_ascii]
                                amorce = ''.join(list_char)
                        elif isinstance(amorce, int):
                            new_filename = str(amorce) + new_filename
                            amorce += 1

                        # Renommage des fichiers
                        os.rename(file, new_filename)
            # Si la liste des extensions est vide, on modifie tous les fichiers du dossier.
            else:
                # Bloc de code concernant la variable _nomfichier dans la règle.
                j = 0
                new_filename = file
                if self._get_regle()._get_nomfichier() == True:
                    pass
                elif self._get_regle()._get_nomfichier() == False:
                    new_filename = "" + file_extension
                else:
                    try:
                        new_filename = self._get_regle()._get_nomfichier() + file_extension
                    except OSError:
                        new_filename = self._get_regle()._get_nomfichier() + str(j) + file_extension
                        j = j + 1

                # Bloc concernant la variable _prefixe dans la règle.
                if self._get_regle()._get_prefixe() != "":
                    new_filename = self._get_regle()._get_prefixe() + new_filename

                # Bloc concernant la variable _postfixe dans la règle.
                if self._get_regle()._get_postfixe() != "":
                    new_filename = new_filename.replace(".", self._get_regle()._get_postfixe() + ".")

                # Bloc concernant la variable _amorce dans la règle.
                if amorce == "":
                    print("amorce = " + str(amorce))
                    pass
                elif isinstance(amorce, str):
                    list_ascii = [ord(c) for c in amorce]
                    print(list_ascii)
                    if list_ascii[-1] < 122:
                        new_filename = amorce + new_filename
                        list_ascii[-1] = list_ascii[-1] + 1
                        list_char = [chr(c) for c in list_ascii]
                        amorce = ''.join(list_char)
                    else:
                        new_filename = amorce + new_filename
                        list_ascii[-1] = 97
                        list_ascii.append(list_ascii[-1])
                        list_char = [chr(c) for c in list_ascii]
                        amorce = ''.join(list_char)
                elif isinstance(amorce, int):
                    new_filename = str(amorce) + new_filename
                    amorce += 1

                # Renommage des fichiers
                os.rename(file, new_filename)
