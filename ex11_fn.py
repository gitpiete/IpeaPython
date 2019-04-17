""" Python4ABM exercícios Lista 1
    Exercício 11.
    Escreva uma função que recebe uma lista e organiza os valores em keys e conta a frequência
    de cada uma. Por exemplo: a lista [0, 0, 1, 1, 1, 2, 5], resultaria em: {1: 3, 0: 2, 2: 1, 5: 1}.
    """

__author__ = 'Pekka'


def histograma(lista):
    d = dict()
    for cada in lista:
        d[cada] = d.get(cada, 0) + 1
    return d


if __name__ == '__main__':
    list_a = [0, 0, 1, 1, 1, 2, 5]
    print(histograma(list_a))
