""" Python4ABM exercícios Lista 1
    Exercício 1
    Escreva um programa que ache os números divisíveis por 7 e por 13, entre o seu ano de nascimento e 2701.
    """

__author__ = 'Pekka'

def print_anos(ano_nasc, ano_fim):
    div_7 = []
    div_13 = []
    div_7_13 = []
    for i in range(ano_nasc, ano_fim + 1):
        if i % 7 == 0:
            div_7.append(i)
        if i % 13 == 0:
            div_13.append(i)
            if i % 7 == 0:
                div_7_13.append(i)

    print('div por 7', div_7)
    print('div por 13', div_13)
    print('div por 7 e 13 ', div_7_13)


if __name__ == '__main__':
    ano_nasc = 1973
    ano_fim = 2701

    print_anos(ano_nasc, ano_fim)
