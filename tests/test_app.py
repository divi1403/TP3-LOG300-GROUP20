"""Module de tests unitaires pour la Calculatrice Flash.

Ce module contient les tests pour valider  la fonction d'analyse syntaxique (calculate) de l'application Flask, permettant
de détecter les bogues cachés.
"""

import unittest
import sys
import os

# Ajout du dossier Backend au chemin de recherche pour importer les modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Backend')))

from app import calculate


class TestCalculatorParser(unittest.TestCase):
    """Classe de tests unitaires pour l'analyse syntaxique et l'évaluation de l'application (app.py)."""

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

    def test_division_par_zero(self):
        """Vérifie que calculate('5/0') propage ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            calculate("5/0")
 
    def test_nombres_decimaux(self):
        """Vérifie que les opérandes décimaux sont acceptés."""
        self.assertEqual(calculate("2.5*2"), 5.0)
 
    def test_resultat_negatif(self):
        """Vérifie qu'une soustraction peut donner un résultat négatif."""
        self.assertEqual(calculate("10-20"), -10)
 
    def test_operande_gauche_negatif(self):
        """Un premier nombre négatif ne doit pas être pris pour un opérateur (bogue)."""
        self.assertEqual(calculate("-5+3"), -2)
 
    def test_operande_droit_negatif(self):
        """Un signe moins après un opérateur indique un nombre négatif (bogue)."""
        self.assertEqual(calculate("5*-3"), -15)
 
    def test_deux_operandes_negatifs(self):
        """Vérifie '-4--2' : soustraction de deux nombres négatifs (bogue)."""
        self.assertEqual(calculate("-4--2"), -2)


if __name__ == '__main__':
    unittest.main()