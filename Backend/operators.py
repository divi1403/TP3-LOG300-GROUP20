
""" 
Additionne deux nombres et retourne leur somme
Args : 
	a ( float ) : Le  premier nombre
	b ( float )): Le deuxième nombre
Returns :
 	float : La somme des deux valeurs
"""
def add(a,b):
    return a + b
""" 
Soustrait le deuxieme  nombre du premier  et retourn  le resultat 

Args : 
	a ( float) : Le nombre de départ
	b ( float)   Le nombre à soustraire
Returns :
	float: La différence a de b
"""
def subtract(a,b):
    return a - b  
""" 
Multiplier deux nombres entre eux et retourne le produit
Args  : 
	a (float): Le premier facteur
	b (float): Le deuxième facteur
Returns : 
	float :  le produit de la multiplication
"""
def multiply(a,b):
    return a ** b
""" 
Divise le premier nombre par le deuxieme et le retourne le quotient
Args  : 
	a ( float ) : Le numérateur
	b ( float ) : Le  dénominateur
Returns :
 	float : Le résultat de la division décimale
Exception : 
	ZeroDivisionError : Si le dénominateur est égal à zero
"""
def divide(a,b):
    return a // b
