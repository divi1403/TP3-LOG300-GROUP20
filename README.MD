
# Calculatrice Flash (Équipe 20)

## 1. Description du projet (But et Portée)

### Objectif
**Calculatrice Flash** est une application web interactive de calculatrice simple développée dans le cadre d'un projet collaboratif universitaire/professionnel. Elle vise à fournir une interface web légère permettant d'effectuer des opérations arithmétiques de base tout en instaurant de bonnes pratiques de génie logiciel : gestion de versions, documentation modulaire, tests automatisés et correction de bogues.

### Portée et Architecture
Le projet repose sur une architecture simple séparant le **Backend** et le **Frontend** :
* **Backend (`/Backend`) :** Développé avec le framework Python **Flask**. Il gère le routage HTTP, l'analyse syntaxique (parsing) sécurisée des expressions mathématiques et l'exécution des opérations arithmétiques.
* **Frontend (`/Frontend`) :** Composé de fichiers HTML et CSS pour offrir une interface utilisateur ergonomique et intuitive sous forme de grille de calculatrice.

---

## 2. Prérequis techniques

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre poste de travail :
* **Git** (pour le clonage et la gestion des branches)
* **Python** (version 3.8 ou supérieure recommandée) et son gestionnaire de paquets **pip**
* Un navigateur web moderne (Chrome, Firefox, Edge, Safari)

---

## 3. Guide d'installation (Étape par étape)

Suivez ces instructions pour configurer l'environnement de développement en local :

### Étape 1 : Cloner le dépôt
Ouvrez votre terminal et clonez le dépôt distant sur votre machine :
```bash
git clone <URL_DE_VOTRE_DEPOT_GITHUB>
cd nom-du-repo
```

### Étape 2 : Créer et activer un environnement virtuel
Il est fortement recommandé d'isoler les dépendances du projet dans un environnement virtuel :
* **Sous macOS / Linux :**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Sous Windows (Invite de commandes / PowerShell) :**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### Étape 3 : Installer les dépendances
Installez la bibliothèque Flask requise pour le serveur web :
```bash
pip install -r requirements.txt
```
*(Si le fichier `requirements.txt` est manquant, installez Flask directement : `pip install Flask`)*

---

## 4. Instructions d'utilisation

### Lancer l'application
1. Rendez-vous dans le répertoire contenant le script principal du serveur :
   ```bash
   cd Backend
   ```
2. Exécutez l'application Flask :
   ```bash
   python app.py
   ```
3. Ouvrez votre navigateur web et accédez à l'adresse locale indiquée dans votre terminal (par défaut : **`http://127.0.0.1:5000`**).

### Utiliser les fonctionnalités
* Saisissez ou cliquez sur une expression mathématique simple (ex: `5 + 3`, `10 - 4`, `6 * 7`, `8 / 2`).
* Soumettez le calcul pour afficher instantanément le résultat ou le message d'erreur approprié en cas de format invalide ou de division par zéro.

---

## 5. Section Tests

Pour garantir la fiabilité de la base de code et valider les correctifs de bogues :
 Exécutez la suite de tests unitaires depuis le dossier racine du projet :
   ```bash
   python -m unittest tests/test_operator.py tests/test_app.py
   ```
---

## 6. Flux de contribution (Workflow Git)

Pour collaborer efficacement au sein de l'équipe (Équipe 20), veuillez respecter scrupuleusement le flux de travail suivant :

1. **Gestion des Issues :**
   * Chaque tâche, correction de bogue ou ajout de fonctionnalité doit correspondre à une **Issue** GitHub ouverte et assignée.
2. **Création d'une branche :**
   * Ne travaillez jamais directement sur la branche principale `main` ou `master`. Créez une branche dédiée à partir de `main` avec un nom explicite :
     ```bash
     git checkout -b feature/nom-de-la-fonctionnalite
     # ou pour un bogue :
     git checkout -b bugfix/description-du-bogue
     ```
3. **Validation des modifications (Commits) :**
   * Rédigez des messages de commit clairs, concis et descriptifs (ex: `fix: correction de la division par zéro dans operators.py`).
4. **Soumission (Pull Request - PR) :**
   * Poussez votre branche sur le dépôt distant :
     ```bash
     git push origin feature/nom-de-la-fonctionnalite
     ```
   * Ouvrez une **Pull Request (PR)** vers la branche `main` sur GitHub.
   * Demandez une relecture (code review) à un membre de l'équipe avant fusion.
