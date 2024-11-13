# ==================================================================================================================

# Exercice 9 : qui calcul la somme des n premiers entiers positifs (n étant lu)

# ==================================================================================================================

# =============
# Boucle WHILE
# =============


# def sum_first_integers(n):
#     the_sum = 0
#     next_val = 0
#     while next_val <= n:
#         the_sum += next_val
#         next_val += 1
#     return the_sum
#
#
# input_num = int(input('Entrez un entier positif : '))
#
# while input_num < 0:
#     print(f'You entered {input_num} !!!')
#     input_num = int(input('Entrez un entier positif : '))
#
#
# if input_num >= 0:
#     total = sum_first_integers(input_num)
#     print(f'La somme des n premiers entiers de {input_num} est {total}.')




# =============
# Boucle FOR
# =============


def sum_first_integers(n):
    the_sum = 0
    for i in range(n + 1):
        the_sum += i
    return the_sum


input_num = int(input('Entrez un entier positif : '))

while input_num < 0:
    print(f'You entered {input_num} !!!')
    input_num = int(input('Entrez un entier positif : '))


if input_num >= 0:
    total = sum_first_integers(input_num)
    print(f'La somme des n premiers entiers de {input_num} est {total}.')