""" Python4ABM exercícios Lista 1
    Exercício 2
    Escreva um programa que imprima o seguinte padrão.
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    """

__author__ = 'Pekka'


def piramide():
    fim = 5

    for i in range(1, fim+1):
        for j in range(1, i+1):
            print('* ', end='')
        print('')

    for k in reversed(range(1, fim+1)):
        for l in range(1, k):
            print('* ', end='')
        print('')


if __name__ == '__main__':
    piramide()
