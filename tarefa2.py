""" exercicio 2: agentes e interações
    """

import random


class Account:
    def __init__(self, ida):
        self.id = ida
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def check_balance(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            return True

    def pay(self, amount):
        self.balance -= amount
        return amount

    # def withdraw(self, value):
    #     if self.balance < value:
    #         print('Saldo insuficiente')
    #         return False
    #     else:
    #         self.balance -= value
    #         return value


class Shop:
    def __init__(self, i, ids):
        self.id = ids
        self.account = Account(i)
        self.fun = random.randrange(100, 105)
        self.capacity = random.randrange(4, 8)
#        self.cost = self.fun / self.capacity
        self.cost = random.randrange(20, 30)

    def visit(self):
        self.capacity -= 1

    def sell(self, amount):
        if self.fun >= amount:
            self.fun -= amount
            return amount
        else:
            return False

    def check_capacity(self):
        if self.capacity == 0:
            return False
        else:
            return True


class Agent:
    def __init__(self, i, idag):
        self.fun = 0
        self.id = idag
        self.account = Account(i)

    def get_fun(self, amount):
        self.fun += amount

    def check_funds(self, shop):
        if self.account.balance > shop.cost:
            return True
        else:
            return False


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
    a1.account.pay(s1.cost)
    print('O custo da loja {} é R${:.2f} e a fun é {}.'.format(s1.id, s1.cost, s1.fun))
    print('O balanço corrente da loja {} é R${:.2f}'.format(s1.id, s1.account.balance))
    print('O agente tem R${:.2f} em caixa'.format(a1.account.balance))
