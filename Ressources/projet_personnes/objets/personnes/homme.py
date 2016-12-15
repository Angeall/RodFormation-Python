from objets.personne import Personne


class Homme(Personne):
    @property
    def sexe(self):
        return "Homme"
