""" Python4ABM exercícios Lista 1
    Exercício 6.
    Escreva um programa que conte o número de letras de uma string.
    """

__author__ = 'Pekka'


def numero_letras(umastring):
    numeroletr = 0
    for i in umastring:
        if i.lower() in 'abcedfghijklmnopqrstuvwxyz':
            numeroletr += 1
    return numeroletr


if __name__ == '__main__':
    print(numero_letras('ASDFJA89080DAF'))
