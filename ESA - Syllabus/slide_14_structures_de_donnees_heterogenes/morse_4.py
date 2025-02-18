"""
Programme de conversion entre texte et code Morse.
Les lettres en Morse sont séparées par un espace, et les mots par deux espaces.
La sortie en texte commence par une majuscule, sauf pour les e-mails qui restent en minuscules.
La constante "SEPARATEUR_MOT" permet de choisir la séparation entre les mots en morse :
    - 2 espaces : ' ' * 2
    - 3 espaces : ' ' * 3
    - backslash avec espaces : ' / '

Un menu permet à l'utilisateur de choisir la transformation à effectuer.

Pour tester :
    Salut les gars !
    ¡Hola, chicos! ¿Cómo va todo?
    email-48@test.be

Date : 10-02-2025
Auteurs : Gwenaël, Hyacinthe, Alfred, Edith, Franck, Boris, Carole, Christian
"""

# Constante
SEPARATEUR_MOT = ' ' * 2

# Dictionnaire pour la traduction du texte en morse
dico_texte_vers_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '@': '.--.-.',
    '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '"': '.-..-.',
    "'": '.----.', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '_': '..--.-', '$': '...-..-', '&': '.-...', ' ': ' '
}

# Dictionnaire pour la traduction du morse en texte
dico_morse_vers_texte = {value: key for key, value in dico_texte_vers_morse.items()}


def transformer_texte_en_morse(phrase, dico_txt_morse, sep_mot):
    """
    Convertit une phrase en code Morse.
    :param phrase: (str) La phrase en texte à transformer.
    :param dico_txt_morse: (dict) Dictionnaire de conversion texte → Morse.
    :param sep_mot: (str) Séparateur entre les mots en Morse.
    :return: (str) La phrase transformée en code Morse.
    """
    phrase = phrase.upper()

    if not all(c in dico_txt_morse for c in phrase):
        return "ERREUR : L'entrée contient des caractères non pris en charge."

    mots = phrase.split(' ')
    mot_resultat = []

    for mot in mots:
        lettre_resultat = []

        for lettre in mot:
            lettre_resultat.append(dico_txt_morse.get(lettre, ''))

        mot_resultat.append(' '.join(lettre_resultat))

    texte = sep_mot.join(mot_resultat)

    return f"Résultat (en morse) : {texte}"


def transformer_morse_en_texte(morse, dico_morse_txt, sep_mot):
    """
    Convertit du code Morse en texte.
    :param morse: (str) La phrase en Morse à transformer.
    :param dico_morse_txt: (dict) Dictionnaire de conversion Morse → Texte.
    :param sep_mot: (str) Séparateur entre les mots en Morse.
    :return: (str) La phrase transformée en texte.
    """
    if not all(c in ".- /" for c in morse):  # Vérifie que seuls des caractères morse sont présents
        return "ERREUR : L'entrée Morse contient des caractères invalides."

    mots = morse.split(sep_mot)
    mot_resultat = []

    for mot in mots:
        lettre_resultat = []
        lettres = mot.split(' ')

        for lettre in lettres:
            lettre_resultat.append(dico_morse_txt[lettre])

        mot_resultat.append(''.join(lettre_resultat))

    texte = ' '.join(mot_resultat)

    # Si l'adresse e-mail est détectée (présence de '@'), on garde la casse d'origine (minuscules).
    # Sinon, on met la première lettre en majuscule.
    texte = texte.lower() if '@' in texte else texte.capitalize()
    return f"Résultat (en texte) : {texte}"


# Programme principal
while True:
    print("\n--- Convertisseur Texte ↔ Morse ---")
    choix = input("Texte → Morse (1) - Morse → Texte (2) - Quitter (q) : ").strip().lower()

    match choix:
        case 'q':
            print("\nMerci d'avoir utilisé le convertisseur. Au revoir !")
            break
        case '1':
            phrase = input("Votre phrase (en texte) : ").strip()
            print(transformer_texte_en_morse(phrase, dico_texte_vers_morse, SEPARATEUR_MOT), '\n')
        case '2':
            morse = input("Votre phrase (en Morse) : ").strip()
            print(transformer_morse_en_texte(morse, dico_morse_vers_texte, SEPARATEUR_MOT), '\n')
        case _:
            print("ERREUR : Veuillez choisir 1, 2 ou q.\n")
