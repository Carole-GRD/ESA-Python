"""
Programme de conversion entre texte et code Morse.
Les lettres en Morse sont séparées par un espace, et les mots par trois espaces.
La sortie en texte commence par une majuscule, sauf pour les e-mails qui restent en minuscules.

Un menu permet à l'utilisateur de choisir la transformation à effectuer.

Pour tester :
    Salut les gars !
    ¡Hola, chicos!
    email@test.be

Date : 10-02-2025
Auteurs : Gwenaël, Hyacinthe, Alfred, Edith, Franck, Boris, Carole, Christian
"""

# Dictionnaire pour la traduction en morse
dico_texte_vers_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-', '?': '..--..', '!': '-.-.--', '@': '.--.-.'
}

dico_morse_vers_texte = {value: key for key, value in dico_texte_vers_morse.items()}


def transformer_texte_en_morse(phrase):
    """
    :param phrase: (str) La phrase en texte à transformer.
    :return: (str) La phrase transformée en code Morse.
    """
    phrase = phrase.upper()
    code_resultat = []

    for caractere in phrase:
        if caractere == ' ':
            code_resultat.append(' ')
            continue

        code = dico_texte_vers_morse.get(caractere, '')  # '' ignore les caractères inconnus
        if code != '':
            # Ajouter uniquement si le caractère a une correspondance en Morse.
            # Sinon, éviter d'insérer une chaîne vide, ce qui générerait un espace superflu lors du join().
            code_resultat.append(code)

    return f"Résultat (en morse) : {' '.join(code_resultat)}"


def transformer_morse_en_texte(morse):
    """
    :param morse: (str) La phrase en Morse à transformer.
    :return: (str) La phrase transformée en texte.
    """
    mots = morse.split(' ' * 3)
    mot_resultat = []

    for mot in mots:
        lettre_resultat = []
        lettres = mot.split(' ')

        for lettre in lettres:
            lettre_resultat.append(dico_morse_vers_texte.get(lettre, ''))  # '' ignore les caractères inconnus

        mot_resultat.append(''.join(lettre_resultat))

    texte = ' '.join(mot_resultat)

    # Si l'adresse e-mail est détectée (présence de '@'), on garde la casse d'origine (minuscules).
    # Sinon, on met la première lettre en majuscule.
    texte = texte.lower() if '@' in texte else texte.capitalize()
    return f"Résultat (en texte) : {texte}"


# Programme principal
while True:
    transformation = input("texte 👉 morse (1) - morse ➡️ texte (2) - quitter (q) : ")

    if transformation == 'q':
        break
    elif transformation == '1':
        phrase = input("Votre phrase (en texte) : ").strip()
        print(transformer_texte_en_morse(phrase), '\n')
    elif transformation == '2':
        morse = input("Votre phrase (en Morse) : ").strip()
        print(transformer_morse_en_texte(morse), '\n')
    else:
        print("ERREUR : choisissez 1, 2 ou q.\n")
