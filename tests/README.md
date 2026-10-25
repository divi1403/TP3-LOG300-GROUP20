# Module de Tests - Calculatrice Flash

## 1. Raison d'être du module
Ce module de tests a pour objectif de valider automatiquement le comportement de la base de code, de confirmer la présence des bogues cachés signalés par l'équipe, et de garantir la non-régression lors des futurs correctifs et ajouts de fonctionnalités.

---

## 2. Fichiers inclus
* **`test_operator.py`** : Contient les cas de test unitaires et d'intégration pour :
  * Les fonctions mathématiques de base (`add`, `subtract`, `multiply`, `divide`).
  * L'analyseur d'expressions (`calculate`) de l'application Flask.

---

## 3. Comment exécuter les tests ?

Assurez-vous d'avoir activé votre environnement virtuel et d'être à la racine du projet, puis exécutez la commande suivante via le framework de test `unittest` de Python :

```
python -m unittest nom_du_fichier.py
