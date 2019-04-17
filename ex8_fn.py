""" Python4ABM exercícios Lista 1
    Exercício 8.
    Dicionários. Dado o dicionário: d = {‘a’: 0}: faça programas que 8.1 acrescente um par
    (chave, valor) {‘b’: 1}, ao dicionário; 8.2 verifique se a key ‘c’ está presente? 8.3
    Concatene um dicionário a um outro dicionário: e = {z : 23}. Use o método ‘update’!
    """

__author__ = 'Pekka'


def acrescenta(dicio, um_par):
    dicio.update(um_par)
#    return dicio


def verifica_presenca(dicio, chave):
    return chave in dicio.keys()


def concatena(dicio1, dicio2):
    return acrescenta(dicio1, dicio2)


if __name__ == '__main__':
    d = {'a': 0}
    print('Dicionário original: ', d)
    acrescenta(d, {'b': 1})
    print('Dicionário acrescentada por um par:', d)
    chave_c = 'c'
    print('Chave', chave_c, 'presente no dicionário', d, ':', verifica_presenca(d, chave_c))
    e = {'z': 23}
    print('Dicionário', d, end=' ')  # necessário separar os prints em linhas diferentes
    print('concatenado com dicionário', e, ':', concatena(d, e))  # senão a concatenação já afeta a impressão do d
