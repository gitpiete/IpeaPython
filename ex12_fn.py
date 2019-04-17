""" Python4ABM exercícios Lista 1
    Exercício 12.
    Escreva uma função que liste todos os números primos até 200. Utilize a divisão modular (%).
    """

__author__ = 'Pekka'


def primos(limite):
    primolista = []
    for i in range(2, limite + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primolista.append(i)
    return primolista


if __name__ == '__main__':
    limnum = 200
    print('Lista de números primos até', limnum, 'é: ', primos(limnum))
