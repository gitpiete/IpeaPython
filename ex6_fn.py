""" Python4ABM exercícios Lista 1
    Exercício 6.
    Escreva um programa que conte o número de letras de uma string.
    """

__author__ = 'Pekka'


def numero_letras(umastring):
    # função conta o número de letras no string
    numeroletr = 0  # inicializa o contador
    for i in umastring:
        if i.lower() in 'abcedfghijklmnopqrstuvwxyz':
            numeroletr += 1
    return numeroletr


if __name__ == '__main__':
    astring = 'ASDFJA89080DAF'
    print('Número de letras na string', astring, 'é', numero_letras(astring))
