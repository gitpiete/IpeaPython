""" Python4ABM exercícios Lista 1
    Exercício 7.
    Escreva um programa que, dada uma lista de números [2, 34, 5, 6, 5, 4, 32] qualquer,
    retorne: o primeiro valor, o número de valores, o último valor, a soma, a média e a mediana.
    Obs. Para listas com tamanho ímpar, a mediana é o valor do meio, quando ordenada
    (sorted()). Para listas pares, os dois valores do meio.
    """

__author__ = 'Pekka'


def soma_manual(numlist):
    soma = 0
    for i in range(len(numlist)):
        soma += numlist[i]
    return soma


def media_manual(numlist):
    return sum(numlist)/len(numlist)


def mediana_manual(numlist):
    numlist.sort()
    return (numlist[int((len(numlist)-0.1)/2)] + numlist[int(len(numlist)/2)]) / 2


def ex7(numlist):
    return[numlist[0], len(numlist), numlist[-1], soma_manual(numlist), media_manual(numlist), mediana_manual(numlist)]


if __name__ == '__main__':
    print(ex7([2, 34, 5, 6, 5, 4, 32]))
