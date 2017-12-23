from Modele.Action import *
import os

class Renommage(Action):

    def __init__(self, path_to_folder, regle):
        Action.__init__(self, path_to_folder, regle)


    def renommer(self):
        list_of_file = os.listdir(self._path_to_folder)
        print(self._path_to_folder)
        print(list_of_file)