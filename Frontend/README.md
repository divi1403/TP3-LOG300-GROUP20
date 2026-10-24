# Module Frontend - Calculatrice Flash

## 1. Raison d'être du module
Le module **Frontend** regroupe tous les éléments visuels et statiques de l'application web. Il fournit l'interface utilisateur (UI) de la calculatrice, permettant aux utilisateurs d'interagir avec les boutons, de visualiser les entrées sur l'écran d'affichage, et de soumettre les calculs au serveur Flask.

---

## 2. Principaux fichiers et responsabilités

* **`index.html`** *(situé dans le sous-dossier `templates/`)*
  * **Rôle :** Structure de la page web de la calculatrice.
  * **Responsabilités :** Fournit le balisage HTML de l'interface, incluant l'écran d'affichage des résultats, les boutons numériques et d'opérations (+, -, *, /), ainsi que le formulaire interactif relié au backend Flask.

* **`style.css`** *(situé dans le sous-dossier `static/`)*
  * **Rôle :** Mise en forme et design de l'interface utilisateur.
  * **Responsabilités :** Gère l'apparence visuelle de la calculatrice (mise en page en grille, couleurs, polices, effets au survol des boutons) pour garantir une expérience utilisateur ergonomique et moderne.

---

## 3. Dépendances et hypothèses

* **Dépendances techniques :**
  * Aucun gestionnaire de paquets requis (le rendu repose nativement sur les moteurs de templates intégrés à Flask).
* **Hypothèses et prérequis :**
  * Le fichier `index.html` s'attend à recevoir une variable `result` transmise par le backend Flask pour afficher le résultat du calcul ou les messages d'erreur.
