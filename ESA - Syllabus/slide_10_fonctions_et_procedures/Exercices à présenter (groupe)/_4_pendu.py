NOMBRE_D_ERREUR = 7

# mot_choisi = "Eau".lower()
mot_choisi = "kayak".lower()


def jouer_au_pendu(mot="eau", nombre_d_erreur=7):
    """
    Fonction permettant de jouer au jeu du pendu avec un mot donné.

    : pre :
        - `mot` est une chaîne de caractères non vide (str) et en minuscules.
        - `nombre_d_erreur` est un entier positif représentant le nombre maximum d'erreurs autorisées.

    : post :
        * Si le joueur trouve toutes les lettres du mot avant d'atteindre le nombre maximum d'erreurs :
            → Le programme affiche "C'est gagné !" et le mot complet.
        - Si le joueur atteint le nombre maximum d'erreurs sans trouver le mot :
            - Le programme affiche "C'est perdu !".
        - À chaque tentative, l'état actuel du mot est affiché avec les lettres trouvées
            et les emplacements restants sous forme de tirets.
        - À chaque mauvaise tentative, le compteur d'échecs est incrémenté
            et la lettre incorrecte est enregistrée et affichée.
        - À la fin d'une partie, l'utilisateur peut choisir de rejouer ou de quitter.
    """
    while True:
        # Initialisation du jeu
        mot_trouver = len(mot) * "_ "
        nombre_d_echec = 0
        mauvaise_lettre = ""
        print(mot_trouver)

        # Jeu
        while (nombre_d_echec < nombre_d_erreur) and (mot != mot_trouver):
            lettre_trouve = False
            print("les mauvaises lettres deja utlise sont : ", mauvaise_lettre)
            lettre = input("veuillez introduire une lettre (en minuscule) : ")

            # Vérifier si la lettre se trouve dans le mot et remplacer les tirets correspondants par cette lettre.
            for i, caractere in enumerate(mot):
                if lettre == caractere:
                    lettre_trouve = True
                    # todo : completer la chaine
                    index = i * 2  # index du tiret à remplacer
                    mot_trouver = mot_trouver[:index] + lettre + mot_trouver[index + 1:]
                    # → le "+ 1" représente la longueur de la chaine qui a été remplacée (→ une lettre)

            # Si le mot est trouvé, on imprime le mot et on sort de la boucle
            if mot == ''.join(mot_trouver.split(' ')):
                print(mot_trouver)
                break

            # Si le mot n'est pas trouvé, on incrémente le nombre d'échecs
            # et ajoute la lettre à la liste des mauvaises lettres.
            if not lettre_trouve:
                nombre_d_echec += 1
                mauvaise_lettre += lettre

            # On affiche les tirets avec les lettres déjà trouvées placées aux endroits correspondants
            # afin que le joueur voie où il en est dans sa recherche.
            print(mot_trouver)

        # On est sorti de la boucle car, on a trouvé le mot ou on a fait 7 erreurs.
        # Affichage du résultat final.
        if mot == ''.join(mot_trouver.split(' ')):
            print("C'est gagné !")
        else:
            print("C'est perdu !")

        rejouer = input("Voulez-vous rejouer (oui/non) : ")
        if rejouer == "non":
            return


jouer_au_pendu(mot_choisi, NOMBRE_D_ERREUR)
# jouer_au_pendu("robot", 5)
