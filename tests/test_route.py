"""Tests d'intégration des routes Flask de la Calculatrice.

Ce module vérifie le comportement de l'application de bout en bout via le
client de test Flask : affichage de la page, soumission du formulaire,
gestion des erreurs et service des fichiers statiques (CSS).
"""

import os
import re
import sys
import unittest

# Ajout du dossier Backend au chemin de recherche pour importer les modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Backend')))

from app import app


class TestFlaskRoute(unittest.TestCase):
    """Tests d'intégration de la route principale '/' et des fichiers statiques."""

    def setUp(self):
        """Crée un client de test Flask neuf pour chaque test."""
        self.client = app.test_client()

    def _display_value(self, response):
        """Extrait la valeur affichée dans le champ #display de la page rendue.

        Args:
            response: La réponse Flask renvoyée par le client de test.

        Returns:
            str: Le contenu de l'attribut value du champ d'affichage.
        """
        html = response.data.decode('utf-8')
        match = re.search(r'id="display"\s+value="([^"]*)"', html)
        self.assertIsNotNone(match, "champ #display introuvable dans la page")
        return match.group(1)

    def test_get_index(self):
        """Vérifie que la page d'accueil se charge (GET /) avec le champ d'affichage vide."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self._display_value(response), "")

    def test_post_calcul_valide(self):
        """Vérifie qu'un POST avec une expression valide affiche le résultat."""
        response = self.client.post('/', data={'display': '6*7'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self._display_value(response), "42.0")

    def test_post_division_par_zero(self):
        """Vérifie que la division par zéro affiche un message d'erreur au lieu de planter le serveur."""
        response = self.client.post('/', data={'display': '5/0'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self._display_value(response).startswith("Error"))

    def test_css_est_servi(self):
        """Vérifie que la feuille de style du Frontend est accessible (bogue : static_folder manquant)."""
        response = self.client.get('/static/style.css')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
