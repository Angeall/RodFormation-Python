import unittest

from objets.personne import ChaineDeCaractereAttendueErreur
from base_de_donnee.base_de_personnes import BaseDePersonnes


class TestBaseDepersonnes(unittest.TestCase):
    def setUp(self):
        self.bdd = BaseDePersonnes("")

    def test_ajouter(self):
        self.bdd.ajouter("Marie", "Test", 33, False)
        personnes = self.bdd.recuperer_tous()
        self.assertEqual(len(personnes), 1)
        self.assertTrue(personnes[0].nom == "Test")
        self.assertTrue(personnes[0].prenom == "Marie")

    def test_ajouter2(self):
        self.assertRaises(ChaineDeCaractereAttendueErreur, self.bdd.ajouter, 2, "Test", 33, False)