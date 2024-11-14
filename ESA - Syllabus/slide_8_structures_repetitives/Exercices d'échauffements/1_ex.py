"""
    Exercice 1 :

    Écrire un programme permettant d’afficher à l’envers une phrase lue.
"""

# ========================================================================
# ==========================  MES TESTS  =================================
# ========================================================================

# Inverser les mots
# -----------------

# # read_phrase = "Ma phrase test."
# read_phrase = input("Entrez une phrase : ")
# words = read_phrase.rstrip(".").split(" ")
#
# inverse_phrase = ""
#
# for i in range(len(words)):
#     if i == len(words)-1:
#         inverse_phrase = words[i].capitalize() + " " + inverse_phrase
#     elif i == 0:
#         inverse_phrase = words[i].lower() + "." + inverse_phrase
#     else:
#         inverse_phrase = words[i] + " " + inverse_phrase
#
#
# print(inverse_phrase)


# =================================================


# # Inverser les lettres
# # --------------------

# # read_phrase = "Ma phrase test."
# read_phrase = input("Entrez une phrase : ")
#
# inverse_phrase = ""
#
# for i in range(len(read_phrase)):
#     inverse_phrase = read_phrase[i] + inverse_phrase
#
# print(inverse_phrase)


# Avec majuscule en début de phrase et point à la fin.
# ----------------------------------------------------

# # read_phrase = "Ma phrase test."
# read_phrase = input("Entrez une phrase : ")
# read_phrase = read_phrase.rstrip(".")
#
# words = read_phrase.rstrip(".").split(" ")
#
# inverse_phrase = ""
#
# for i in range(len(read_phrase)):
#     if i == 0:
#         inverse_phrase = read_phrase[i].lower() + "." + inverse_phrase
#     elif i == len(read_phrase)-1:
#         inverse_phrase = read_phrase[i].capitalize() + inverse_phrase
#     else:
#         inverse_phrase = read_phrase[i] + inverse_phrase
#
# print(inverse_phrase)


# ========================================================================
# ==========================  LE SLICING   ==============================
# ========================================================================


# # Demande à l'utilisateur d'entrer une phrase
# phrase = input("Entrez une phrase : ")
#
# # Inverse la phrase en utilisant le slicing
# phrase_inversee = phrase[::-1]
#
# # Affiche la phrase inversée
# print("La phrase à l'envers est :", phrase_inversee)


# ========================================================================
# =======================  TROIS METHODES  ===============================
# ========================================================================

"""
    ----------
    Le Slicing
    ----------
    
    word = "Bonjour"
    reversed_word = word[::-1]
    print(reversed_word)  # Output: "ruojnoB"
    
    Ici, nous prenons la chaîne et utilisons le slicing [::-1] pour obtenir une sous-chaîne allant de la fin au début.
    
    
    --------------------
    La fonction reversed
    --------------------
    
    word = "Bonjour"
    reversed_word = ''.join(reversed(word))
    print(reversed_word)  # Output: "ruojnoB"
    
    La fonction reversed retourne un itérable inversé.
    
    La méthode join permet de fusionner les éléments pour obtenir la chaîne inversée.
    
    
    -------------------------------
    Avec une fonction personnalisée
    -------------------------------
    
    def invert_word(word):
        reversed_word = ""
        for caractere in word:
            reversed_word = caractere + reversed_word
        return reversed_word
    
    word = "Bonjour"
    print(invert_word(word))  # Output: "ruojnoB"
    
    Cette fonction parcourt la chaîne caractère par caractère et les ajoute au début de la chaîne inversée.
    
"""
