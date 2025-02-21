# from random import random

# numeroAleatorio = random()
# print(numeroAleatorio)



# class seresHumanos():
#     def __init__(self, nome, cpf):
#         self.nome = nome
#         self.cpf = cpf

# jose = seresHumanos("José", 12345678900)

# print(jose.nome)
# print(jose.cpf)


class animal():
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def desc(self):
        return f'{self.nome} é um animal da espécie {self.especie}'

class passaro(animal):
    def __init__(self, nome, especie, cor):
        super().__init__(nome, especie)
        self.cor = cor

    def desc(self):
        return f'{self.nome} é um pássaro da espécie {self.especie} e da cor {self.cor}'
    
class peixe(animal):
    def __init__(self, nome, especie):
        super().__init__(nome, especie)
    
    def desc(self):
        return f'{self.nome} é um peixe da espécie {self.especie} e vive em cardume'

passaro1 = passaro('Piu', 'Canario', 'Amarelo')
print(passaro1.desc())

#printe o tipo de passaro1
print(type(passaro1))
peixe1 = peixe('Nemo', 'Peixe-palhaço')
print(peixe1.desc())
animal1 = animal('Frajola', 'Gato')
print(animal1.desc())
print(type(animal))