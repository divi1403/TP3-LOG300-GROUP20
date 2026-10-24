# Module Backend - Calculatrice Flash

## 1. Raison d'être du module
Le module **Backend** est le cœur logique de l'application web. Il est responsable de la gestion du serveur web, du routage HTTP, de la réception des requêtes de l'interface utilisateur, de l'analyse syntaxique (parsing) des expressions mathématiques saisies, et de l'exécution sécurisée des calculs arithmétiques via le framework Flask.

---

## 2. Principaux fichiers et responsabilités

* **`app.py`**
  * **Rôle :** Point d'entrée principal de l'application Flask.
  * **Responsabilités :** Initialise l'application, configure le dossier des templates HTML, définit les routes HTTP (méthodes GET et POST), intercepte les soumissions du formulaire de la calculatrice, et transmet les expressions au module de calcul pour afficher les résultats ou les erreurs.

* **`operators.py`**
  * **Rôle :** Module de logique mathématique.
  * **Responsabilités :** Contient les fonctions fondamentales de calcul (`add`, `subtract`, `multiply`, `divide`). Il applique les opérations arithmétiques de base et gère les cas d'erreurs métiers (comme la division par zéro).

---

## 3. Dépendances et hypothèses

* **Dépendances techniques :**
  * **Python 3.x**
  * **Flask** (bibliothèque principale pour le serveur et le routage web).
* **Hypothèses et prérequis :**
  * Le module suppose que le répertoire parent a correctement installé les dépendances listées dans le `requirements.txt` global.
  * Il est supposé que le dossier contenant les fichiers statiques et les templates HTML (`Frontend`) est accessible via le chemin relatif configuré dans `app.py` (`../Frontend/templates`).
