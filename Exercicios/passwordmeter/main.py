from classes.view import *

booleano = None
while booleano != True:
    senha = pedir_senha()
    booleano = numero_carateres(senha)


maiusculos(senha)
minusculas(senha)
numbers(senha)
symbol(senha)
numero_carateres(senha)