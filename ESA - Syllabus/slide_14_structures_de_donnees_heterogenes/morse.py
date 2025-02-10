"""
    Travail de groupe
    Exercice 3 : Écrivez un programme permettant de traduire une phrase reçue en morse.

    Pour tester :

    Apprendre le morse est amusant !
    .- .--. .--. .-. . -. -.. . .-.. . -- --- .-. ... . . ... - .- -- ..- ... .- -. - -.-.--

    Salut les gars !
    ... .- .-.. ..- -   .-.. . ...   --. .- .-. ...   -.-.--

    email@test.be
    . -- .- .. .-.. .--.-. - . ... - .-.-.- -... .
"""

# ==============================================================================================
# ====================================  Dictionnaires  =========================================
# ==============================================================================================

dico_utf8_vers_morse = {
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

# print(f"dico_utf8_vers_morse : {dico_utf8_vers_morse}")

dico_morse_vers_utf8 = {value: key for key, value in dico_utf8_vers_morse.items()}
# print(f"dico_morse_vers_utf8 : {dico_morse_vers_utf8}")


# ==============================================================================================
# =======================================  Fonctions  ==========================================
# ==============================================================================================

def transformer_utf8_en_morse(phrase):
    phrase_resultat = []
    for caractere in phrase:
        if caractere == ' ':
            phrase_resultat.append(' ')
            continue
        phrase_resultat.append(dico_utf8_vers_morse[caractere.upper()])

    return f"Votre phrase en morse : {' '.join(phrase_resultat)}"


def transformer_morse_en_utf8(morse):
    mots = morse.split(' ' * 3)
    mots_et_lettres = []
    for mot in mots:
        lettre = mot.split(' ')
        mots_et_lettres.append(lettre)

    mot_resultat = []
    for i, mot in enumerate(mots_et_lettres):
        lettre_resultat = []
        for j, lettre in enumerate(mot):
            if i == 0 and j == 0:
                lettre_resultat.append(dico_morse_vers_utf8[lettre])
            else:
                lettre_resultat.append(dico_morse_vers_utf8[lettre].lower())
        mot_resultat.append(''.join(lettre_resultat))
    return f"Votre phrase en utf8 : {' '.join(mot_resultat)}"


# ==============================================================================================
# ======================================  Programme  ==========================================
# ==============================================================================================

while True:
    transformation = input('phrase vers morse (1) - morse vers phrase (2) - quitter (q) : ')
    while not (transformation == 'q' or transformation == '1' or transformation == '2'):
        print('ERREUR : choisissez 1, 2 ou q')
        transformation = input('vers morse (1) - morse vers phrase (2) - quitter (q) : ')
    if transformation == 'q':
        break
    if transformation == '1':
        phrase = input('Votre phrase (en utf-8) : ')
        print(transformer_utf8_en_morse(phrase))
    if transformation == '2':
        morse = input('Votre phrase (en morse) : ')
        print(transformer_morse_en_utf8(morse))
