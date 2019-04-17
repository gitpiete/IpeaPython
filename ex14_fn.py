""" Python4ABM exercícios Lista 1
    Exercício 14.
    . Escreva um programa que verifica se todas as letras do alfabeto constam no mínimo uma
    vez do parágrafo fornecido pelo usuário.
    """

__author__ = 'Pekka'


def alfabetocheck(paragrafo):
    for i in 'abcedfghijklmnopqrstuvwxyz':
        if i in paragrafo.lower():
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    paragraph = 'Pack my box with five dozen liquor jugs'
    print('O texto', paragraph, 'tem todas as letras do alfabeto: ', alfabetocheck(paragraph))
