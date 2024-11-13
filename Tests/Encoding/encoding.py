
# TESTS ENCODING

# # initializing string
# String = "geeksforgeeks"
#
# encoded_string = String.encode('utf-8')
# print('The encoded string in base64 format is :')
# print(encoded_string)
#
# decoded_string = encoded_string.decode('utf-8')
# print('The decoded string is :')
# print(decoded_string)


# # initializing string
# string = "é - @ - # 52 - §"
#
# print(string)
#
# encoded_string = string.encode('utf-8')
# print('The encoded string in base64 format is :')
# print(encoded_string)
#
# decoded_string = encoded_string.decode('utf-8')
# print('The decoded string is :')
# print(decoded_string)


# txt = "My name is Ståle"
#
# print(txt)
# print(txt.encode("UTF-8"))
# print(txt.encode("UTF-8").decode("UTF-8"))


# str="Hello! Welcome to Tutorialspoint."
# str_encoded = str.encode('utf_16','strict')
# print("The encoded string is: ", str_encoded)
# str_decoded = str_encoded.decode('utf_16', 'strict')
# print("The decoded string is: ", str_decoded)


# string = "Café"
#
# encoded_bytes = string.encode('utf-8')
# print(encoded_bytes)  # Affiche : b'Caf\xc3\xa9'
#
# decoded_string = encoded_bytes.decode('utf-8')
# print(decoded_string)  # Affiche : Café
