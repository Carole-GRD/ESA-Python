
def print_file_4():
    print("===============")
    print(f"file_4.py -> __name__ : {__name__}")  # __name__ :  __main__ ou file_4  (voir ci-dessous et main.py)
    print("===============")
# print_file_4()



# print("file 4")
# print(f"file_4.py -> __name__ : {__name__}")


'''
    __name__ : __main__       -> si lancé à partir de file_4.py
    
    __name__ : file_4          -> si lancé à partir d'un autre fichier (ex.: du fichier main.py) 
                                 dans lequel on importe ce fichier file_4.py
'''

