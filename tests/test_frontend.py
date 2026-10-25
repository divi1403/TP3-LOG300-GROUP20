"""Tests de l'interface HTML de la Calculatrice.

Ce module lit directement le template index.html (sans lancer Flask) pour
vérifier que les boutons affichent le bon symbole.
"""

import os
import re
import unittest

# Chemin du template, lu directement pour vérifier le HTML sans passer par Flask
INDEX_HTML = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../Frontend/templates/index.html'))


class TestFrontendBoutons(unittest.TestCase):
    """Vérifie que chaque bouton affiche le même symbole que celui qu'il ajoute à l'écran."""

    def test_etiquettes_des_boutons(self):
        """Chaque bouton appendToDisplay('X') doit afficher exactement X (bogues : « 02 », « 88 », * et / vides)."""
        with open(INDEX_HTML, encoding='utf-8') as f:
            html = f.read()
        boutons = re.findall(
            r"""onclick="appendToDisplay\('([^']*)'\)">([^<]*)</button>""", html)
        # 10 chiffres + 4 opérateurs : on s'assure qu'aucun bouton n'a été oublié
        self.assertEqual(len(boutons), 14)
        for valeur, etiquette in boutons:
            # subTest liste chaque bouton fautif séparément dans le rapport
            with self.subTest(bouton=valeur):
                self.assertEqual(etiquette.strip(), valeur)


if __name__ == '__main__':
    unittest.main()
