""" Python4ABM exercícios Lista 1
    Exercício 5.
    Escreva um programa que recebe uma letra e identifica se ela é vogal ou consoante.
    """

__author__ = 'Pekka'


def vogal_ou_consoante(letra):
    if letra.lower() in 'aeiou':
        print(letra + ' é vogal')
    else:
        print(letra + ' é consoante')


if __name__ == '__main__':
    caractere = input("Escreve uma letra: ")
    while len(caractere) != 1 or caractere.lower() not in 'abcedfghijklmnopqrstuvwxyz':
        caractere = input("Escreve uma letra: ")
    vogal_ou_consoante(caractere)
