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


def convertir_texte_en_morse(phrase, dico_texte_morse, separateur_mots):
    """
    Convertit une phrase en code Morse.
    :param phrase: (str) La phrase en texte à convertir.
    :param dico_texte_morse: (dict) Dictionnaire de conversion texte → Morse.
    :param separateur_mots: (str) Séparateur entre les mots en Morse.
    :return: (str) La phrase transformée en code Morse ou un message d'erreur.
    """
    phrase = phrase.lower().strip()
    mots = phrase.split()
    mots_en_morse = []

    for mot in mots:
        lettres_en_morse = []

        for caractere in mot:
            code_morse = dico_texte_morse.get(caractere)
            if code_morse is None:
                return 'Erreur : L\'entrée "Texte" contient des caractères non pris en charge.'
            lettres_en_morse.append(code_morse)
        mots_en_morse.append(" ".join(lettres_en_morse))

    return separateur_mots.join(mots_en_morse)


def convertir_morse_en_texte(morse, dico_morse_texte, separateur_mots):
    """
    Convertit du code Morse en texte.
    :param morse: (str) La phrase en Morse à convertir.
    :param dico_morse_texte: (dict) Dictionnaire de conversion Morse → Texte.
    :param separateur_mots: (str) Séparateur entre les mots en Morse.
    :return: (str) La phrase transformée en texte ou un message d'erreur.
    """

    morse = morse.strip()
    mots_morse = morse.split(separateur_mots)
    mots_en_texte = []

    for mot in mots_morse:
        codes = mot.split()
        lettres_en_texte = []

        for code in codes:
            lettre_texte = dico_morse_texte.get(code)
            if lettre_texte is None:
                return 'Erreur : L\'entrée "Morse" contient des caractères non pris en charge.'
            lettres_en_texte.append(lettre_texte)
        mots_en_texte.append("".join(lettres_en_texte))

    texte = " ".join(mots_en_texte)
    return texte.lower() if "@" in texte else texte.capitalize()


# Programme principal
with open('code_morse', 'r') as fichier:
    lignes = fichier.readlines()

    lignes_nettoyees = []
    for ligne in lignes:
        ligne_nettoyee = ligne.strip('\n')
        lignes_nettoyees.append(ligne_nettoyee)

    # del code_morse_nettoie[0]
    # code_morse_nettoie_first_element = lignes_nettoyees.pop(0)

    SEPARATEUR_MOT = ' ' * 2
    # SEPARATEUR_MOT = ' / '
    dico_texte_vers_morse = {}
    dico_morse_vers_texte = {}
    for entree in lignes_nettoyees:
        cle_valeur = entree.split(',')
        dico_texte_vers_morse[cle_valeur[0]] = cle_valeur[1]
        dico_morse_vers_texte[cle_valeur[1]] = cle_valeur[0]

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
