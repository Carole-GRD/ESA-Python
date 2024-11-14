"""
    Exercice 2 :

    Écrire un programme permettant de simuler la fonction “search and replace” d’un traitement de texte.

"""

# txt = "Hello World ! Hello Python !"
# txt = "apple orange apple apple"
# print(f"TEXTE : {txt}")

txt = input("Entrez une phrase : ")    # Hello World ! Hello Python !
old = input("Find : ")                 # Hello
new = input("Replace : ")              # Hi
# occ = int(input("Occurences : "))       # 2

# modified = txt.replace(old, new, occ)
modified = txt.replace(old, new)

print(modified)  # Hi World! Hi Python !


