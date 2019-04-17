""" Python4ABM exercícios Lista 1
    Exercício 13.
    Escreva um programa que substitua ‘,’ por ‘.’ e ‘.’ por ‘,’ em uma string. Exemplo: 1,000.54 por 1.000,54.
    """

__author__ = 'Pekka'


def subst_pontos(uma_string):
    stringlista = list(uma_string)
    for i in range(len(stringlista)):
        if stringlista[i] == ',':
            stringlista[i] = '.'
        elif stringlista[i] == '.':
            stringlista[i] = ','
    return ''.join(stringlista)


if __name__ == '__main__':
    a_string = '1,000.54'
    print('String', a_string, 'com pontos e vírgulas trocados vira', subst_pontos(a_string))
