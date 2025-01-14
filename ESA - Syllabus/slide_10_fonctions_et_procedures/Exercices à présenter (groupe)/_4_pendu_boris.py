def clear_screen():
    print("\n" * 100)  # Crée beaucoup de nouvelles lignes pour pousser le texte hors de l'écran


def pendu(chances, mot):
    # Initialisation du jeu
    mot_trouver = len(mot) * "_"
    nombre_d_echec = 0
    mauvaise_lettre = ""

    # Jeu
    while (nombre_d_echec < chances) and (mot != mot_trouver):
        # clear_screen()
        print("__")
        print("le mot à trouver : ", mot_trouver)
        lettre_trouve = False
        print("les mauvaises lettres deja utlise sont : ", mauvaise_lettre)
        print("il te reste : ", (chances - nombre_d_echec), "vie")
        lettre = input("veuillez introduire une lettre (en minuscule) : ")
        for i, caractere in enumerate(mot):
            if lettre == caractere:
                lettre_trouve = True
                # todo : completer la chaine
                mot_trouver = list(mot_trouver)
                mot_trouver[i] = caractere
                mot_trouver = ''.join(mot_trouver)

        if not lettre_trouve:
            nombre_d_echec += 1
            mauvaise_lettre += lettre

    # Affichage du resultat

    if mot_trouver == mot:
        exit("c'est gagner!!!!!!!!!!!")
    else:
        exit("c'est perdu!!!!!!!!!!")


# debut du jeu
choix = input("Veux tu jouer ? (oui/non) : ")
if choix == "oui":
    mot = input("donne un mot à faire deviner : ").lower()
    pendu(4, mot)
else:
    exit("A bientot !")
