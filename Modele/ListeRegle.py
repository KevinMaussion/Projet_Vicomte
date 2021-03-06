from pickle import Pickler, Unpickler


class ListeRegle(list):

    def __init__(self):
        super().__init__()
        self._liste_regle = []

    def creation_liste(self, regle):
        self._liste_regle.append(regle)

    def _get_liste_regle(self):
        return self._liste_regle

    def _set_liste_regle(self, regle):
        self._liste_regle = regle

    liste_regle = property(_get_liste_regle, _set_liste_regle)

    def append(self, regle):
        self._liste_regle.append(regle)

    def count(self, **kwargs):
        return len(self._get_liste_regle())

    def sauvegarder_liste_regle(self, path_to_save_file):
        with open(path_to_save_file, 'wb') as fichier:
            mon_pickler = Pickler(fichier)
            mon_pickler.dump(self)

    def charger_liste_regle(self, path_to_save_file):
        with open(path_to_save_file, 'rb') as fichier:
            mon_depickler = Unpickler(fichier)
            self._liste_regle = mon_depickler.load()

    def __iter__(self):
        for e in self._get_liste_regle():
            yield e

    def __repr__(self):
        return str(self._get_liste_regle())
