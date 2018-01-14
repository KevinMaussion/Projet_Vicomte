class Regle(object):

    def __init__(self):
        self._amorce = ""
        self._apartirde = ""
        self._prefixe = ""
        self._nomfichier = False
        self._postfixe = ""
        self._extension = []

    def regle(self, amorce, apartirde, prefixe, nomfichier, postfixe, extension):
        self._amorce = amorce
        self._apartirde = apartirde
        self._prefixe = prefixe
        self._nomfichier = nomfichier
        self._postfixe = postfixe
        self._extension = extension

    def _get_amorce(self):
        return self._amorce

    def _get_apartirde(self):
        return self._apartirde

    def _get_prefixe(self):
        return self._prefixe

    def _get_nomfichier(self):
        return self._nomfichier

    def _get_postfixe(self):
        return self._postfixe

    def _get_extension(self):
        return self._extension

    def _set_amorce(self, amorce):
        self._amorce = amorce

    def _set_apartide(self, apartirde):
        self._apartirde = apartirde

    def _set_prefixe(self, prefixe):
        self._prefixe = prefixe

    def _set_nomfichier(self, nomfichier):
        self._nomfichier = nomfichier

    def _set_postfixe(self, postfixe):
        self._postfixe = postfixe

    def _set_extension(self, extension):
        self._extension = extension

    amorce = property(_get_amorce, _set_amorce)
    apartirde = property(_get_apartirde, _set_apartide)
    prefixe = property(_get_prefixe, _set_prefixe)
    nomfichier = property(_get_nomfichier, _set_nomfichier)
    postfixe = property(_get_postfixe, _set_postfixe)
    extension = property(_get_extension, _set_extension)

    def __repr__(self):
        return "Règle: amorce = {}, à partir de = {}, prefixe = {}, nom de fichier = {}, postfixe = {}, extension = {}"\
            .format(self._get_amorce(), self._get_apartirde(), self._get_prefixe(),
                    self._get_nomfichier(), self._get_postfixe(), self._get_extension())
