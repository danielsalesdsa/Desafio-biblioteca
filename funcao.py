# from random import random

# numeroAleatorio = random()
# print(numeroAleatorio)

class seresHumanos():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

jose = seresHumanos("José", 12345678900)
print(jose.nome)
print(jose.cpf)