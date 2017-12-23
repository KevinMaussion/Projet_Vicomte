class Action(object):

    def __init__(self, path_to_folder, regle):
        self._path_to_folder = path_to_folder
        self._regle = regle

    def _get_path_to_folder(self):
        return self._path_to_folder

    def _get_regle(self):
        return self._regle

    def _set_path_to_folder(self, path_to_folder):
        self._path_to_folder = path_to_folder

    def _set_regle(self, regle):
        self._regle = regle

    def simule(self):
        pass

    def __str__(self):
        return "Voici une description de l'action : {}, {}".format(self._path_to_folder, self._regle)