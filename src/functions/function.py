import sys
sys.path.append('C:/Users/rayan/Documents/Dev/pratica/Tamagushi') 


from src.classes.classe import Tamagushi

def menu():
    pass


def alimentacao():
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
    escolha = int(input('Escolha com o que você deseja alimentar seu pet: '))
    while escolha < 1 or escolha > 8 :
        escolha = int(input('Escolha uma opção valida: '))
    return escolha


def modifica_fome():
    pass

