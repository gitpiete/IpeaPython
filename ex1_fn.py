""" Python4ABM exercícios Lista 1
    Exercício 1
    Escreva um programa que ache os números divisíveis por 7 e por 13, entre o seu ano de nascimento e 2701.
    """

__author__ = 'Pekka'


def print_anos(ano_nasc, ano_fim):
    # função para procurar números divisíveis por 7, 13 e ambos
    # inicializar as listas para coletar os números divisíveis
    div_7 = []
    div_13 = []
    div_7_13 = []
    for i in range(ano_nasc, ano_fim + 1):  # +1 para incluir também o ano final
        if i % 7 == 0:  # i módulo 7 = 0 => i divisível por 7
            div_7.append(i)  # inclui na lista
        if i % 13 == 0:
            div_13.append(i)
            if i % 7 == 0:
                div_7_13.append(i)
    print('Números divisíveis por 7:', str(div_7)[1:-1])  # este slice tira os colchetes do redor da lista
    print('Números divisíveis por 13:', str(div_13)[1:-1])
    print('Números divisíveis por 7 e 13:', str(div_7_13)[1:-1])


if __name__ == '__main__':
    ano_nascimento = 1973
    ano_final = 2701
    print_anos(ano_nascimento, ano_final)
