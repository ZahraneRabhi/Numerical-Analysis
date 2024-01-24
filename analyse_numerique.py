from tabulate import tabulate


F = lambda x:  (x**3) + x - 1 # Définition du fonction f(x) = (x^3)+x−1.

signe = lambda x: -1 if x < 0 else 1 # Retourne le signe d'une valeur donnée

def bissect(a, b, epsilon, max_iter):
    """
    Applique la méthode de bissection pour trouver la racine d'une fonction dans un intervalle spécifié.
    
    Arguments:
    - a, b: intervale [a,b].
    - epsilon: valeur de précision.
    - max_iter: nombre maximal d'itérations pour éviter les boucles infinies.
    """
    entete = ["i", "a", "F(a)", "b", "F(b)", "x", "F(x)"]
    table = []
    compteur = 0

    while (compteur < max_iter):
        c = (a + b) / 2
        table.append([compteur, a, F(a), b, F(b), c, F(c)])
        if F(c) == 0 or (b - a) / 2 < epsilon:
            print(f"\nSolution trouvée: {c} \n")
            break
        compteur += 1
        if signe(F(c)) == signe(F(a)):
            a = c
        else:
            b = c
    print(tabulate(table, headers=entete, tablefmt="rounded_grid"))



