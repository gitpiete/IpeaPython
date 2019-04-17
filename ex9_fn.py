""" Python4ABM exercícios Lista 1
    Exercício 9.
    Escreva uma função que faz um loop as keys de um dicionário. Se as keys forem vogais,
    eleve o valor ao quadrado. Caso contrário, set o valor para 0. Use if k in ‘aeiou’
    """

__author__ = 'Pekka'


def eleva_vogal(dicio):
    for k in dicio.keys():
        if k in 'aeiou':
            dicio.update({k:dicio[k]**2})
        else:
            dicio.update({k:0})


if __name__ == '__main__':
    d = {'a':2, 'b':3, 'c':4, 'd':5, 'e':6}
    eleva_vogal(d)
    print(d)
