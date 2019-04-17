""" Python4ABM exercícios Lista 1
    Exercício 10.
    Escreva uma função que retorna os máximos e mínimos de um dicionário.
    """

__author__ = 'Pekka'


def retorna_max(dicio):
    return dicio[max(dicio)]


def retorna_min(dicio):
    return dicio[min(dicio)]


if __name__ == '__main__':
    d = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
    print('O máximo do dicionário', d, 'é', retorna_max(d))
    print('O mínimo do dicionário', d, 'é', retorna_min(d))
