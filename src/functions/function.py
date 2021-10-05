import sys
sys.path.append('C:/Users/rayan/Documents/Dev/pratica/Tamagushi') 

from random import randint
from src.classes.classe import Tamagushi



def menu():
    pass


def cardapio():
    print('''
    ________________________________________________
    ################### Cardápio ###################: 

    1- Verduras
    2- Carne
    3- Doces
    4- Legumes
    5- Frutas
    6- Sobremesa
    7- Comida japonesa
    8- Hamburguer
    _________________________________________________''')


def modifica_fome():
    escolha = int(input('Escolha com o que você deseja alimentar seu pet: '))
    while escolha < 1 or escolha > 8 :
        escolha = int(input('Escolha uma opção valida: '))

    if escolha == 1:
        novo_bixinho.alterar_fome(randint(1, 5))
        novo_bixinho.alterar_humor(0 - randint(3, 4))
        novo_bixinho.alterar_saude(randint(1, 3))
    
    elif escolha == 2:
        pass
    

novo_bixinho = Tamagushi('Tata', 1)
print(f'fome = {novo_bixinho.fome}/100')
print(f'Humor = {novo_bixinho.humor}/100')
print(f'Saude = {novo_bixinho.saude}/100')
cardapio()
modifica_fome()
print(f'fome = {novo_bixinho.fome}/100')
print(f'Humor = {novo_bixinho.humor}/100')
print(f'Saude = {novo_bixinho.saude}/100')