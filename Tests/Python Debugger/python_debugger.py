"""
    Point d'arrêt pour déboguer

        ->  Utilisation du point-virgule :
            Le point-virgule est nécessaire ici car nous plaçons deux instructions sur la même ligne,
            ce qui est courant lors de l'utilisation de pdb pour insérer un point d'arrêt.

        ->  Placement du point d'arrêt :
            On place l'arrêt en une seule ligne au-dessus de l'instruction ou de la variable
            dont on veut connaître la valeur.
"""

aaa = 5
bbb = 10

# Arrête le code ici, permet d'inspecter les variables avant d'exécuter les lignes suivantes.
# ATTENTION : Après le débogage, n'oubliez pas de supprimer cette ligne pour éviter un arrêt involontaire.
import pdb; pdb.set_trace()

ccc = aaa + bbb
print(ccc)


# ------AUTRE EXEMPLE -----


def add(a, b):
    somme = a + b
    return somme


x = 10
y = '20'  # Erreur : addition d'un int et d'un str

import pdb; pdb.set_trace()  # Point d'arrêt pour examiner `x` et `y`

result = add(x, y)  # Cela va provoquer une erreur
print(result)

"""
    Comment fonctionne pdb.set_trace() ?

        ->  pdb.set_trace() démarre le débogueur Python 
            et arrête l'exécution du code à l'endroit où il est inséré. 

        ->  Cela te permet de voir les valeurs des variables 
            et d'exécuter le code ligne par ligne à partir de cet endroit.


    Commandes de base dans pdb :

        ->  n (next) : Exécute la ligne actuelle et passe à la suivante.
        ->  c (continue) : Continue l'exécution jusqu'à la fin ou jusqu'au prochain point d'arrêt.
        ->  s (step) : Entre dans une fonction si la ligne actuelle en appelle une.
        ->  Tu peux également taper directement le nom d'une variable (par exemple ccc) pour obtenir sa valeur.
        ->  p <nom_de_variable> (print) : Affiche la valeur d'une variable spécifique.
        ->  q (quit) : Quitte le débogueur.

    ATTENTION : 

        Après avoir fini le débogage, il est important de supprimer ou de commenter la ligne 
        contenant pdb.set_trace() pour éviter que le programme ne s'arrête lors de son exécution normale.
"""

