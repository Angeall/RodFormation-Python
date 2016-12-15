from objets.personne import Personne


class Femme(Personne):
    @property
    def sexe(self):
        return "Femme"
