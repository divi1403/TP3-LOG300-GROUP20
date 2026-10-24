
""" 
Additionne deux nombres et retourne leur somme
Args : 
	a (int , float ) : Le  premier nombre
	b (int , float )): Le deuxième nombre
Returns :
 	int,float : La somme des deux valeurs
"""
def add(a,b):
    return a + b
""" 
Soustrait le deuxieme  nombre du premier  et retourn  le resultat 

Args : 
	a ( int, float) : Le nombre de départ
	b ( int, float)   Le nombre à soustraire
Returns :
	int,float: La différence a de b
"""
def subtract(a,b):
    return a - b  
""" 
Multiplier deux nombres entre eux et retourne le produit
Args  : 
	a (int , float): Le premier facteur
	b (int , float): Le deuxième facteur
Returns : 
	int , float :  le produit de la multiplication
"""
def multiply(a,b):
    return a ** b
""" 
Divise le premier nombre par le deuxieme et le retourne le quotient
Args  : 
	a ( int, float ) : Le numérateur
	b ( int, float ) : Le  dénominateur
Returns :
 	float : Le résultat de la division décimale
Exception : 
	ZeroDivisionError : Si le dénominateur est égal à zero
"""
def divide(a,b):
    return a // b
