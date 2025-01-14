def typographie(phrase):

 """verifions si la phrase commence par une majuscule et se termine par un point"""

 if not phrase:
     return "votre phrase est vide"
 if not phrase[0].isupper():
     return "votre phrase doit commencer par une majuscule "
 if not phrase.endswith('.'):
     return "votre phrase doit se terminer par un point"

       ###verification des espaces autour du mots
 mots = phrase.split()
 for i, mot in enumerate(mots):
     if ','in mot:    #verification de la virgule
         if not (mot.endswith(',') and i+1 < len(mots)):
          return "la virgule doit être colé au mot qui le précède et suivie d'un espace"

     if '.'in mot and mot != mots[-1]:
        return "le point doit être colé au mot et uniquement en fin de phrase"

     if ';'in mot or ":" in mot or "?"in mot:
         if not(mot.startswith(';') or mot.startswith(':') or mot.startswith('?')):
             return "le point virgule , la virgule et le point d'interrogation doivent être entourés d'espaces"

 return "phrase correcte"




phrase = input("entrer une phrase")
resultat = typographie(phrase)
print(resultat)


"""
OK : 
- Majuscule en début de phrase
- Point en fin de phrases

À corriger :
- "."
    OK : Est-ce qu'il y a quelqu'un. je suis arrivée.
        -> le point doit être colé au mot et uniquement en fin de phrase
        
    Est-ce qu'il y a quelqu'un, je suis arrivée .
        -> phrase correcte 
        -> or le point doit être colé au mot

- les espaces autour de la virgule 
    Le point virgule , la virgule et le point d'interrogation doivent être entourés d'espaces. 
        -> phrase correcte
        -> or, la virgule doit être collée au mot qui la précède (et sont suivie par un espace mais cela c'est ok)
        
    OK : Le point virgule ,la virgule et le point d'interrogation doivent être entourés d'espaces.
        -> la virgule doit être colé au mot qui le précède et suivie d'un espace
        
    OK : Le point virgule, la virgule et le point d'interrogation doivent être entourés d'espaces.
        -> phrase correcte

- ";", ":", "?"
    Le commentaire (ce n'est pas la virgule mais les deux points) :
        le point virgule , la virgule et le point d'interrogation doivent être entourés d'espaces

    Est-ce qu'il y a quelqu'un :je suis arrivée.
        -> phrase correcte
        -> or, manque l'espace après
        -> idem pour ";" et "?"
        
    OK : Est-ce qu'il y a quelqu'un ? Je suis arrivée.
    OK : Est-ce qu'il y a quelqu'un?Je suis arrivée.
    OK : Est-ce qu'il y a quelqu'un? Je suis arrivée.
    

À ajouter :
- pre et post conditions dans la docstring
"""