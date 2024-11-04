
if __name__ == '__main__':
    print("""\
    
    ---------------------------------------
    Tableau des carrés et sommes des carrés
    ---------------------------------------
    """)


# n = 1
# sum_1 = 0  # Initialiser b à 0 pour bien accumuler la somme des carrés
# sum_2 = 1
#
# while n <= 10:
#     n_squared = n ** 2
#     sum_1 += n_squared
#     sum_2 = n * (n + 1) * (2 * n + 1) // 6  # Calcul exact de la somme des carrés pour comparaison
#     print(f"{n:<6} {n_squared:<6} {sum_1:<6} {sum_2:<6}")  # Affichage avec alignement fixe
#     n += 1




# sum_1 = 0
# sum_2 = 0
# i = 1
#
# while i < 11:
#     i_squared = i**2
#     sum_1 += i_squared
#     sum_2 = i*(i + 1)*(2*i + 1)//6
#     # print(i, "\t", i**2, "\t", sum, "\t", sum_2)
#     print(f"{i:<6} {i_squared:<6} {sum_1:<6} {sum_2:<6}")  # Largeurs fixes pour l'alignement
#     i+=1





def calculate_sums(text):
    sum_1 = 0
    sum_2 = 0
    i = 1

    while i < 11:
        i_squared = i**2
        sum_1 += i_squared
        sum_2 = i * (i + 1) * (2 * i + 1) // 6
        # print(i, "\t", i**2, "\t", sum, "\t", sum_2)
        print(f"{i:<6} {i_squared:<6} {sum_1:<6} {sum_2:<6}")  # Largeurs fixes pour l'alignement
        i += 1

    print(text)

    return sum_1, sum_2




if __name__ == '__main__':
    calculate_sums('A partir du fichier : "calcul_sums"')

