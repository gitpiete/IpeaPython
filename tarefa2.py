""" exercicio 2: canja de galinha
    """

import random

class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            print('Saldo insuficiente')
            return False
        else:
            self.balance -= value
            return True

class Shop:
    def __init__(self, id, i):
        self.id = id
        self.account = Account(i)
        self.fun = random.randrange(1, 10)
        self.capacity = random.randrange(1, 10)
        self.cost = self.fun / self.capacity


class Agent:
    def __init__(self, id, i):
        self.id = id
        self.account = Account(i)


if __name__ == '__main__':
    a1 = Agent(0, 0)
    s1 = Shop(1, 1)
    # bb = Account('023')
    # print(bb.balance)
    # print(a1.account.balance)
    # print(s1.account.balance)
    # print(a1.account.id)
    a1.account.deposit(10)
    s1.account.deposit(s1.cost)
    a1.account.withdraw(s1.cost)
    print('O custo da loja {} é R${:.2f} e a fun é {}.'.format(s1.id, s1.cost, s1.fun))
    print('O balanço corrente da loja {} é R${:.2f}'.format(s1.id, s1.account.balance))
    print('O agente tem R${:.2f} em caixa'.format(a1.account.balance))