"""
Travail de groupe N°1 :

Reprenez le programme de conversion du morse en utilisant le fichier "code_morse"
se trouvant sur Smartschool qui reprend le code morse sous format CSV.

Programme de conversion entre texte et code Morse.
Les lettres en Morse sont séparées par un espace, et les mots par deux espaces.
La sortie en texte commence par une majuscule, sauf pour les e-mails qui restent en minuscules.
La constante "SEPARATEUR_MOT" permet de choisir la séparation entre les mots en morse :
    - 2 espaces : ' ' * 2
    - 3 espaces : ' ' * 3
    - backslash avec espaces : ' / '

Un menu permet à l'utilisateur de choisir la transformation à effectuer.

Pour tester :
    Salut les gars !                 # ... .- .-.. ..- -  .-.. . ...  --. .- .-. ...  -.-.--
    ¡Hola, chicos! ¿Cómo va todo?    # ERREUR : L'entrée "texte" contient des caractères non pris en charge."
    email-48@test.be                 # ERREUR : L'entrée "texte" contient des caractères non pris en charge."
    email.48@test.be                 # . -- .- .. .-.. .-.-.- ....- ---.. .--.-. - . ... - .-.-.- -... .
    SOS                              # ... --- ...
    ... -o- ...                      # ERREUR : L'entrée "Morse" contient des caractères invalides.

Date : 10-02-2025
Auteurs : Gwenaël, Hyacinthe, Alfred, Edith, Franck, Boris, Carole, Christian
"""

import csv


def convertir_texte_en_morse(phrase, dico_txt_morse, sep_mot):
    """
    Convertit une phrase en code Morse.
    :param phrase: (str) La phrase en texte à convertir.
    :param dico_txt_morse: (dict) Dictionnaire de conversion texte → Morse.
    :param sep_mot: (str) Séparateur entre les mots en Morse.
    :return: (str) La phrase transformée en code Morse ou un message d'erreur.
    """
    phrase = phrase.lower().strip()
    mots = phrase.split()
    mot_resultat = []

    for mot in mots:
        lettre_resultat = []

        for lettre in mot:
            lettre_morse = dico_txt_morse.get(lettre)
            if lettre_morse is None:
                return 'Erreur : L\'entrée "Texte" contient des caractères non pris en charge.'
            lettre_resultat.append(lettre_morse)
        mot_resultat.append(" ".join(lettre_resultat))

    return sep_mot.join(mot_resultat)


def convertir_morse_en_texte(morse, dico_morse_txt, sep_mot):
    """
    Convertit du code Morse en texte.
    :param morse: (str) La phrase en Morse à convertir.
    :param dico_morse_txt: (dict) Dictionnaire de conversion Morse → Texte.
    :param sep_mot: (str) Séparateur entre les mots en Morse.
    :return: (str) La phrase transformée en texte ou un message d'erreur.
    """

    morse = morse.strip()
    mots = morse.split(sep_mot)
    mot_resultat = []

    for mot in mots:
        lettres = mot.split()
        lettre_resultat = []

        for lettre in lettres:
            lettre_texte = dico_morse_txt.get(lettre)
            if lettre_texte is None:
                return 'Erreur : L\'entrée "Morse" contient des caractères non pris en charge.'
            lettre_resultat.append(lettre_texte)
        mot_resultat.append("".join(lettre_resultat))

    texte = " ".join(mot_resultat)
    return texte.lower() if "@" in texte else texte.capitalize()


# Programme principal

with open('code_morse', 'r') as code_morse_fichier_csv:
    lecteur = csv.reader(code_morse_fichier_csv)
    next(lecteur, None)

    SEPARATEUR_MOT = ' ' * 2
    # SEPARATEUR_MOT = ' / '
    dico_texte_vers_morse = {}
    dico_morse_vers_texte = {}
    for ligne in lecteur:
        dico_texte_vers_morse[ligne[0]] = ligne[1]
        dico_morse_vers_texte[ligne[1]] = ligne[0]

    while True:
        print("\n--- Convertisseur Texte ↔ Morse ---")
        choix = input("Texte → Morse (1) - Morse → Texte (2) - Quitter (q) : ").strip().lower()

        match choix:
            case 'q':
                print("\nMerci d'avoir utilisé le convertisseur. Au revoir !")
                break
            case '1':
                phrase = input("Votre phrase (en texte) : ").strip()
                print(convertir_texte_en_morse(phrase, dico_texte_vers_morse, SEPARATEUR_MOT), '\n')
            case '2':
                morse = input("Votre phrase (en Morse) : ").strip()
                print(convertir_morse_en_texte(morse, dico_morse_vers_texte, SEPARATEUR_MOT), '\n')
            case _:
                print("ERREUR : Veuillez choisir 1, 2 ou q.\n")
