# Module de tests - Calculatrice Flash

## 1. Raison d'être du module
Ce module vérifie automatiquement le comportement de l'application. Il a servi à confirmer les bogues cachés de la base de code (chaque test en échec a donné lieu à une issue GitHub) et protège maintenant contre leur retour lors des futures modifications.

---

## 2. Fichiers et couverture

Un fichier de test par partie de l'application :

| Fichier | Partie testée | Ce qui est vérifié |
|---|---|---|
| `test_operator.py` | `Backend/operators.py` | Addition, soustraction (ordre des opérandes), multiplication, division décimale (`7 / 2 = 3.5`) et levée de `ZeroDivisionError` |
| `test_app.py` | `calculate()` dans `Backend/app.py` | Expressions valides, expressions mal formées (`ValueError`), décimaux, nombres négatifs (`-5+3`, `5*-3`, `-4--2`), division par zéro |
| `test_routes.py` | Route `/` de Flask | Affichage de la page (GET), calcul via le formulaire (POST), message d'erreur en cas de division par zéro, service de `style.css` |
| `test_frontend.py` | `Frontend/templates/index.html` | Chaque bouton affiche le même caractère que celui qu'il ajoute à l'écran |

Chaque test porte un docstring qui décrit le comportement vérifié. Les tests importent le Backend en ajoutant `../Backend` au chemin de recherche Python ; ils fonctionnent donc quel que soit le dossier d'où on les lance.

---

## 3. Comment exécuter les tests

Environnement virtuel activé et dépendances installées (voir le README principal), depuis la **racine** du dépôt :

```bash
# Toute la suite
python -m unittest discover -s tests -v

# Un seul fichier
python -m unittest discover -s tests -p test_routes.py -v
```

Résultat attendu : `OK`, sans échec ni erreur.

> Le dossier s'appelle `tests/` et non `test/` : `test` est le nom d'un paquet de la bibliothèque standard de Python, ce qui faisait échouer `python -m unittest test/...` depuis la racine.

---

## 4. Dépendances et hypothèses
* `unittest` est inclus dans Python ; seul Flask (installé avec `Backend/requirements.txt`) est nécessaire pour `test_app.py` et `test_routes.py`.
* `test_frontend.py` lit directement le fichier HTML et suppose que chaque bouton de saisie appelle `appendToDisplay('<caractère>')`.
* Pour ajouter un test, créez un fichier `test_<partie>.py` dans ce dossier : `discover` le trouvera automatiquement.
