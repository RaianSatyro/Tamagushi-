from random import randint

class Tamagushi:
    def __init__(self, nome, fome, saude, idade, humor = 100):
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

        
    
    def alterar_saude(self):
        pass
    
    
    def alterar_idade(self):
        pass
        

    def brincar(self):
        self.humor += randint(1, 4)
        self.fome -= randint(1, 6)
        return self.humor , self.fome

novo_bixinho = Tamagushi('generico', 100, 100, 1)
novo_bixinho.alterar_fome(3)
print(novo_bixinho.fome)


