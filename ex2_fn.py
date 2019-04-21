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
    # este função imprime o 'piramide' de lado
    fim = 5  # altura do piramide

    for i in range(1, fim+1):  # primeira metade
        for j in range(1, i+1):  # inclui o 'pico'
            print('* ', end='')
        print('')

    for k in reversed(range(1, fim+1)):
        for l in range(1, k):  # na volta não precisa incluir o pico
            print('* ', end='')
        print('')


if __name__ == '__main__':
    piramide()
