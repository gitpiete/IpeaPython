""" Python4ABM exercícios Lista 1
    Exercício 3.
    Altere o programa acima para que o usuário possa entrar com o número máximo de estrelas.
    """

__author__ = 'Pekka'


def piramide(fim):
    for i in range(1, fim + 1):
        for j in range(1, i + 1):
            print('* ', end='')
        print('')

    for k in reversed(range(1, fim + 1)):
        for l in range(1, k):
            print('* ', end='')
        print('')
        

if __name__ == '__main__':
    fim = 13
    piramide(fim)