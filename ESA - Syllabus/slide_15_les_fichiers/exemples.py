"""
Les fichiers
"""

import os

# from os import chdir
# chdir("/home/anuyens/monNouveauFichier")


# mon_fichier = open("toto.txt", "r")
# print("hello")  # FileNotFoundError: [Errno 2] No such file or directory: 'toto.txt'
# → ERREUR si toto.txt n'existe pas
# mon_fichier.close()

# mon_fichier = open("toto.txt", "w")  # crée le fichier s'il n'existe pas
# print("hello")
# mon_fichier.close()


"""
Voici une liste des fonctions les plus utilisées, ainsi que leur signification :
    ● os.system() : permet une commande de console bash ou DOS. (ie.os.system("dir"), os.system("ls") …)
    ● os.name : Nom du système d’exploitation
    ● os.path : possède lui-même pas mal de sous fonction …
    ● os.curdir : répertoire courant.
    ● os.pardir : répertoire parent.
    ● os.walk produit un générateur capable de délivrer de façon récursive une série de tuples de trois éléments :
        - le nom du répertoire ;
        - la liste de ses sous-répertoires ;
        - la liste de ses fichiers.
"""
# for rep, sous, fich in os.walk("../../ESA - Syllabus"):
#     print("\nRép:", rep)
#     print(" S-R:", sous)
#     print(" Fic:", fich)


"""
Les droits (sous système UNIX) :
    ● os.chown(fichier, usr, grp) : fixe le propriétaire et le groupe, exprimés sous forme de nombres
    ● os.chmod(fichier, mode) : fixe les attributs du fichier en trois chiffres octaux. 
      Le premier concerne le propriétaire du fichier, le second un groupe, et le troisième tout le monde.
    ● os.access(fichier, mode) retourne TRUE selon les possibilités d’accès à un fichier. Mode =
    ● os.F_OK pour l'existence ;
    ● os.R_OK pour la lecture ;
    ● os.W_OK pour la modification ;
    ● os.X_OK pour l’exécution du fichier (ou l’ouverture du répertoire).
"""

"""
Édition de fichiers :
    ● descr = open(chaine, flags, mode) : ouvre un fichier.
    ● flags admet les variables suivantes :
        ● O_RDONLY (=0) ;
        ● O_WRONLY (=1) ;
        ● O_RDWR (=2) ;
        ● O_CREAT (=64) ;
        ● O_APPEND (=1024) ;
        ● O_BINARY (MS seulement)… on les compose en les additionnant ou avec le “ou” logique "|".

    ● os.read(descr, n) : retourne une chaîne de n octets du contenu d’un fichier ouvert en 0 ou 1
    ● os.write(descr, chaine) : écrit une chaîne dans un fichier (en écrasant ou en ajout selon le mode d’ouverture)
    ● os.close(descr) ferme un fichier

    ● os.lseek(descr, n, mode) positionne le curseur d’un fichier selon un offset n, selon le mode :
        - os.SEEK_SET (ou 0, à partir du début) ;
        - os.SEEK_CUR (ou 1, à partir de la position courante) ;
        - os.SEEK_END (ou 2: à partir de la fin)
    ● os.remove(fichier) détruit un fichier si vous avez les droits d’écritures
    ● os.rename(ancien, nouveau) : renomme un fichier ou un répertoire, permet également de déplacer un fichier
"""

# mon_fichier = open("toto.txt", "r")
# mon_fichier.write("hello")   # io.UnsupportedOperation: not writable
# mon_fichier.close()
# # → ERREUR car on a ouvert le fichier en mode lecture

# mon_fichier = open("toto.txt", "w")
# mon_fichier.write("hello")
# mon_fichier.close()
# si on effectue plusieurs fois le programme, il écrase le mot "hello" car on est en mode écriture

# mon_fichier = open("toto.txt", "a")
# mon_fichier.write("hello")
# mon_fichier.close()
# # → si on effectue plusieurs fois le programme, il écrit plusieurs fois le mot "hello" collés "hellohellohello"

# mon_fichier = open("toto.txt", "r", encoding='UTF-8')
# # mon_fichier = open("toto.txt", "r")
# lines = mon_fichier.readlines()
# mon_fichier.close()
# for line in lines:
#     print(line)


"""
Gestion des répertoires
    ● os.getcwd() : renvoie le répertoire courant connu du système. 
      Si un script est appelé par l’interface graphique (et que le module sys est importé), 
      il est préférable d’utiliser la fonction suivante.
    ● os.path.dirname(sys.argv[0]),
    ● os.chdir(repertoire) : rentre dans un répertoire existant.
    ● chdir(os.pardir) : remonte d’un niveau de répertoire.

    ● os.listdir(os.getcwd()) : renvoie une liste de tous les objets du répertoire courant
    ● os.mkdir(repertoire, mode) : crée un répertoire dans le répertoire courant, mode 0777 par défaut
    ● os.makedirs(chemin, mode) : crée tout un chemin dans le répertoire courant, mode 0777 par défaut
    ● os.rmdir(repertoire) : détruit un répertoire (en principe vide) si droit d’écriture 

    ● os.path.getsize(fichier) : retourne la taille (entier long)
    ● os.path.getmtime(fichier) : retourne la date de la dernière modification d’un fichier (idem)
    ● os.path.getatime(fichier) : retourne la date du dernier accès à un fichier (en nombre de secondes)
    ● os.path.dirname(cheminfichier) : retourne la partie de l’adresse 
      à gauche du dernier séparateur de répertoire (/, \…)

    ● os.path.basename(cheminfichier) : retourne la partie de l’adresse à droite du dernier séparateur de répertoire
    ● os.path.split(cheminfichier) : retourne un tuple avec les résultats de dirname et basename
    ● os.path.abspath(fichier) : renvoie l’adresse absolue du nom de fichier précisé
    ● os.path.exists(fichier) : renvoie True si le fichier existe

    ● os.path.isfile(fichier) : renvoie True si l’objet est un fichier
    ● os.path.isdir(fichier) : renvoie True si l’objet est un répertoire
    ● os.path.islink(fichier) : renvoie True si l’objet est un lien symbolique, un lien matériel renvoie False
    ● dir(os.path) : informe sur les méthodes du sous-module os.path
"""

# print(os.path.abspath('slide_9'))
# print(os.path.exists('../slide_9'))
# print(dir(os))
# print(dir(os.path))


# fichier = open('toto.txt', 'r')
# # t = fichier.read()
# t = fichier.read(9)  # lit les 9 premiers caractères
# print(t)
# fichier.close()


"""
Python possède quelques fonctions utiles pour manipuler de tel fichier :
    ● readline() : permet de lire une ligne entière du fichier. 
      Le pointeur de fichier se situe ensuite sur la ligne suivante.
    ● readlines() : permet de lire toutes les lignes restantes du fichier. 
      À éviter si le fichier contient de nombreuses lignes.

"""
