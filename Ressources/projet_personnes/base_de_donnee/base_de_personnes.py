import pickle

from objets.personnes.femme import Femme
from objets.personnes.homme import Homme


class BaseDeDonneeInexistanteErreur(Exception):
    pass


class PersonneIntrouvableErreur(Exception):
    pass


class BaseDePersonnes():
    def __init__(self, nom):
        self.nom = nom
        self._personnes = {}

    def sauver(self):
        fichier = open(self.nom + ".bin", mode="wb+")
        pickle.dump(self, fichier)
        fichier.close()

    @staticmethod
    def charger(nom):
        try:
            fichier = open(nom + ".bin", mode="rb")
            return pickle.load(fichier)
        except:
            msg = "La base de donnees du nom '" + nom + "' n'existe pas"
            raise BaseDeDonneeInexistanteErreur(msg)

    def ajouter(self, prenom, nom, age, homme=True, nationalite="Belge", metier=None):
        if homme:
            personne = Homme(prenom, nom, age, nationalite, metier)
        else:
            personne = Femme(prenom, nom, age, nationalite, metier)
        self._personnes[personne.id] = personne
        return personne.id

    def recuperer(self, id):
        if id in self._personnes.keys():
            return self._personnes[id]
        else:
            msg = "La personne portant l'id : " + str(id) + " est introuvable"
            raise PersonneIntrouvableErreur(msg)

    def recuperer_tous(self):
        lst = []
        for id in self._personnes.keys():
            lst.append(self._personnes[id])
        return lst  # Liste contenant toutes les personnes de la bdd

    def supprimer(self, id):
        if id in self._personnes.keys():
            del self._personnes[id]
        else:
            msg = "La personne portant l'id : " + str(id) + " est introuvable"
            raise PersonneIntrouvableErreur(msg)

    def nettoyer(self):
        cles = list(self._personnes.keys())
        for cle in cles:
            del self._personnes[cle]
            # Ou simplement : self._personnes = {}
