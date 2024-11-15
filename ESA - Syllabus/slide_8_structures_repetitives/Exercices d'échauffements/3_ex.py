"""
     Exercice 3 :

     Écrire un programme permettant de convertir le nombre 127 en binaire, octal et hexadécimal.

"""


# ================================================================================================
# =============================  BINAIRE - OCTAL - HEXADECIMAL  ==================================
# ================================================================================================


def convert_number(n, b):
    """
        Convertit un nombre de la base décimale vers une autre base (2, 8, 16)

    :param n: nombre à convertir
    :param b: base dans laquelle le nombre doit être converti (2, 8, 16)

    :return: le nombre convrerti dans la base choisie
    """
    q = -1
    res = ''
    while q != 0:
        q = n // b
        r = n % b
        if b == 16:
            match r:
                case 10:
                    r = 'A'
                case 11:
                    r = 'B'
                case 12:
                    r = 'C'
                case 13:
                    r = 'D'
                case 14:
                    r = 'E'
                case 15:
                    r = 'F'
        res = str(r) + res
        n = q
    return res


# print(f"127 en binaire : {convert_number(127, 2)}")         # 1111111
# print(f"127 en octal : {convert_number(127, 8)}")          # 177
# print(f"127 en hexadecimal : {convert_number(127, 16)}")   # 7F

# numb = 19514
# print(f"{numb} en binaire : {convert_number(numb, 2)}")         # 100110000111010
# print(f"{numb} en octal : {convert_number(numb, 8)}")          # 46072
# print(f"{numb} en hexadecimal : {convert_number(numb, 16)}")   # 4c3a


# =============================   VERSION AMELIOREE PAR CHATGPT  ================================


def convert_number_to(n, b):
    """
    Convertit un nombre de la base décimale vers une autre base (2, 8, 16).

    Cette fonction prend un nombre en base décimale et le convertit dans la base spécifiée,
    puis retourne le nombre sous forme de chaîne avec un préfixe indiquant la base.

    Args:
        n (int): Le nombre à convertir (doit être un entier positif).
        b (int): La base dans laquelle le nombre doit être converti. Peut être 2 (binaire),
                8 (octale) ou 16 (hexadécimale).

    Returns:
        str: Le nombre converti dans la base spécifiée, avec le préfixe approprié ('0b', '0o', '0x').

    Raises:
        ValueError: Si la base `b` est différente de 2, 8 ou 16.

    Example:
        >>> convert_number_to(127, 2)
        '0b1111111'
        >>> convert_number_to(127, 8)
        '0o177'
        >>> convert_number_to(127, 16)
        '0x7f'
    """
    if b not in [2, 8, 16]:
        raise ValueError("La base doit être 2, 8 ou 16.")

    if n == 0:
        return '0'

    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    res = ''
    while n > 0:
        r = n % b
        if b == 16 and r >= 10:
            r = hex_dict[r]
        res = str(r) + res
        n = n // b

    if b == 2:
        return '0b' + res
    elif b == 8:
        return '0o' + res
    elif b == 16:
        return '0x' + res


# numb = 127
# print(f"{numb} en binaire : {convert_number_to(numb, 2)}")
# print(f"{numb} en octal : {convert_number_to(numb, 8)}")
# print(f"{numb} en hexadecimal : {convert_number_to(numb, 16)}")


# ================================================================================================
# =====================================  BIN - OCT - HEX =========================================
# ================================================================================================


def convert_number_bases(n):
    """
        Convertit un nombre entier donné en ses représentations binaire, octale et hexadécimale.

        Args:
            n (int): Le nombre entier à convertir.

        Returns:
            dict: Un dictionnaire contenant les représentations du nombre dans les bases suivantes :
                - 'binaire' (str) : Représentation binaire du nombre (sans le préfixe '0b').
                - 'octal' (str) : Représentation octale du nombre (sans le préfixe '0o').
                - 'hexadécimal' (str) : Représentation hexadécimale du nombre (sans le préfixe '0x').

        Example:
            >>> convert_number_bases(127)
            {'binaire': '1111111', 'octal': '177', 'hexadécimal': '7f'}
    """

    # Conversion sans les préfixes en utilisant le découpage de chaîne
    binary = bin(n)[2:]       # Binaire sans '0b'
    octal = oct(n)[2:]        # Octal sans '0o'
    hexadecimal = hex(n)[2:]  # Hexadécimal sans '0x'

    # Retourner un dictionnaire avec les résultats
    return {
        'décimal': n,
        'binaire': binary,
        'octal': octal,
        'hexadécimal': hexadecimal
    }


number = 127
converted_number = convert_number_bases(number)

print(f"{converted_number['décimal']} en binaire : {converted_number['binaire']}")
print(f"{converted_number['décimal']} en octal : {converted_number['octal']}")
print(f"{converted_number['décimal']} en hexadécimal : {converted_number['hexadécimal']}")
