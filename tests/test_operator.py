"""Module de tests unitaires pour la Calculatrice Flash.

Ce module contient les tests pour valider le comportement des opérateurs arithmétiques  permettant
de détecter les bogues cachés.
"""

import unittest
import sys
import os

# Ajout du dossier Backend au chemin de recherche pour importer les modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Backend')))

from operators import add, subtract, multiply, divide

"""Classe de tests unitaires pour les fonctions arithmétiques du module operators.py."""
class TestCalculatorOperators(unittest.TestCase):
    def test_add(self):
        """Vérifie le bon fonctionnement de l'addition."""
        # 2 + 3 doit retourner 5
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        """Vérifie le bon fonctionnement de la soustraction."""
        # 5 - 3 doit retourner 2 (met en évidence le bogue potentiel d'inversion b - a)
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        """Vérifie le bon fonctionnement de la multiplication."""
        # 4 * 3 doit retourner 12 (met en évidence le bogue potentiel de la puissance **)
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        """Vérifie le bon fonctionnement de la division et la gestion des erreurs."""
        # 10 / 2 doit retourner 5.0 (met en évidence le bogue potentiel de la division entière //)
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        
        # Vérification de la levée d'une exception en cas de division par zéro
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
