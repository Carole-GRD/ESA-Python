"""
Les packages

https://sametmax.com/category/digital/

Clique droit sur le nom du projet sur lequel vous voulez rajouter le package
    → New
    → Python Package

    Module
    ------
    Un module est un fichier regroupant différentes fonctions ou variables
    qui pourront être utilisées dans vos programmes.

    Les noms des modules doivent être court et uniquement en minuscule.
    Vous pouvez utiliser des soulignés dans les noms des modules si cela améliore la lisibilité.

    Package
    -------
    Un package est un regroupement de module. C’est un dossier mais qui contient
    au minimum un fichier “__init__.py” qui peut être vide.

    Les packages Python doivent également être court et uniquement minuscule.
    L’utilisation de souligné est déconseillé dans le nom des paquets.


PEP 8 :
    → une importation par ligne
    → trier les importations par ordre alphabétique
"""

from utils.fonctions_utils import affiche_moi
from utils.fonctions_utils import ajoute_moi
from utils.fonctions_utils import ma_variable as mv

affiche_moi(mv)
print(ajoute_moi(mv, " ou pas"))
