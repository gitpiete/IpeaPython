""" Python4ABM exercícios Lista 1
    Exercício 4.
    Escreva um programa que corre os números de 1 a 50 e imprime. Mas, quando for múltiplo
    de três, imprima ‘Oops’, quando for múltiplo de 5 imprima ‘Doo’, quando for de ambos
    imprima ‘OopsDoo’.
    """

__author__ = 'Pekka'


def print_numeros():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print('OopsDoo')
        elif i % 3 == 0:
            print('Oops')
        elif i % 5 == 0:
            print('Doo')
        else:
            print(i)


if __name__ == '__main__':
    print_numeros()
