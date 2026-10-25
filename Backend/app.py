"""Application principale Flask pour la Calculatrice Flash.

Ce module gère les routes web, la réception des requêtes de l'interface utilisateur,
l'analyse syntaxique des expressions mathématiques et le rendu des résultats.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Initialisation de l'application Flask et configuration du template
app = Flask(
    __name__,
    template_folder='../Frontend/templates', 
    static_folder='../Frontend/static')

# Dictionnaire associant chaque symbole d'opération à sa fonction correspondante
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

"""Analyse une expression mathématique sous forme de chaîne de caractères et retourne le résultat.

    Args:
        expr (str): L'expression à évaluer (ex: "5 + 3").

    Returns:
        float, int: Le résultat du calcul.

    Raises:
        ValueError: Si l'expression est vide, mal formatée, contient plusieurs opérateurs,
                    ou si les opérandes ne sont pas des nombres valides.
"""


def calculate(expr: str):

    # Vérification de la validité de l'entrée (non vide et de type chaîne)
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

   # Suppression des espaces superflus pour faciliter l'analyse
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parcours de la chaîne pour identifier l'opérateur unique
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch
   
    # Validation de la position de l'opérateur (ne doit pas être au début, à la fin ou absent)
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")
    # Extraction des opérandes gauche et droite par rapport à l'opérateur
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")
    # Exécution de l'opération correspondante via le dictionnaire OPS
    return OPS[op_char](a, b)

"""
Gère la route principale de l'application web (affichage et soumission du formulaire).

Returns:
        str: Le rendu HTML de la page de la calculatrice avec le résultat ou l'erreur éventuelle.
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            # Évaluation sécurisée de l'expression saisie par l'utilisateur
            result = calculate(expression)
        except Exception as e:
            # Capture des erreurs de calcul ou de format pour affichage dans l'interface
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lancement du serveur de développement Flask en mode debug
    app.run(debug=True)
