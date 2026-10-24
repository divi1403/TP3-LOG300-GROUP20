"""Module de tests unitaires pour la Calculatrice Flash.

Ce module contient les tests pour valider  la fonction d'analyse syntaxique (calculate) de l'application Flask, permettant
de détecter les bogues cachés.
"""

import unittest
import sys
import os

# Ajout du dossier Backend au chemin de recherche pour importer les modules
from app import calculate

 """Classe de tests unitaires pour l'analyse syntaxique et l'évaluation de l'application (app.py)."""

class TestCalculatorParser(unittest.TestCase):

    def test_calculate_valid_expressions(self):
        """Vérifie l'évaluation correcte d'expressions valides sous forme de chaînes."""
        self.assertEqual(calculate("10 + 5"), 15)
        self.assertEqual(calculate("8 - 3"), 5)
        self.assertEqual(calculate("4 * 3"), 12)
        self.assertEqual(calculate("20 / 4"), 5.0)

    def test_calculate_invalid_expressions(self):
        """Vérifie que les expressions mal formées lèvent bien une exception ValueError."""
        with self.assertRaises(ValueError):
            calculate("")  # Expression vide
        with self.assertRaises(ValueError):
            calculate("5 + + 3")  # Multiples opérateurs
        with self.assertRaises(ValueError):
            calculate("abc + 3")  # Opérandes non numériques


if __name__ == '__main__':
    unittest.main()

