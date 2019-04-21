""" Python4ABM exercícios Lista 1
    Exercício 7.
    Escreva um programa que, dada uma lista de números [2, 34, 5, 6, 5, 4, 32] qualquer,
    retorne: o primeiro valor, o número de valores, o último valor, a soma, a média e a mediana.
    Obs. Para listas com tamanho ímpar, a mediana é o valor do meio, quando ordenada
    (sorted()). Para listas pares, os dois valores do meio.
    """

__author__ = 'Pekka'


def soma_manual(numlist):
    # função conta a soma da lista de números
    soma = 0
    for i in range(len(numlist)):
        soma += numlist[i]
    return soma


def media_manual(numlist):
    # função devolve média dos números da lista
    return float('{:.2f}'.format(soma_manual(numlist)/len(numlist)))  # dois decimais


def mediana_manual(numlist):
    # função devolve mediana da lista de números
    otherlist = numlist.copy()  # senão a lista original é classificada
    otherlist.sort()
    return (otherlist[int((len(otherlist)-0.1)/2)] + otherlist[int(len(otherlist)/2)]) / 2


def ex7(numlist):
    # função devolve os itens mencionados no exercício
    return[numlist[0], len(numlist), numlist[-1], soma_manual(numlist), media_manual(numlist), mediana_manual(numlist)]


if __name__ == '__main__':
    umalista = [2, 34, 5, 6, 5, 4, 32]
    print('O primeiro valor, o número de valores, o último valor, a soma, a média e a mediana da lista',
          umalista, 'são, respectivamente:', ex7(umalista))
