import time
# from Python.exercicios_padawan.adivinhação_frutas.classes.frutas import Frutas
# from Python.exercicios_padawan.adivinhação_frutas.services.buscar_frutas import Verificacao
# Frutas()

frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']

print(f'Opções de frutas disponíveis: {frutas}')
input_letra = input('Digite a letra inicial da fruta que desejas: ').lower()
print(f'Buscando frutas com a inicial " {input_letra} "... \n')

for i in frutas:
    if input_letra in i[0]:
        print(i)

time.sleep(3)
