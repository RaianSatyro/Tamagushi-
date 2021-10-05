from random import randint

class Tamagushi:
    def __init__(self, nome, idade, fome = 50, saude = 50, humor = 50):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = humor
        
    
    def alterar_nome(self):
        self.nome = str(input('Digite o nome do seu bixinho: '))
        return self.nome
    
    def alterar_fome(self, valor):
        self.fome += valor
        return self.fome
        
    def alterar_saude(self, valor):
        self.saude += valor
        return self.saude
     
        
    def brincar(self):
        self.humor += randint(1, 4)
        self.fome -= randint(1, 6)
        return self.humor , self.fome
    
    def alterar_humor(self, valor):
        self.humor += valor
        return self.humor


    def alterar_idade(self):
        pass




tata = Tamagushi('tata', 1)
print(tata.saude)
tata.alterar_saude(-2)
print(tata.saude)