""" Projeto final
    Arquivo de criação de classes básicas
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

    def pay(self, amount):  # Esta função só é chamada se check_balance == True
        self.balance -= amount
        return amount


class Flight:
    def __init__(self, idf, company="", day=0, price=0, seats=0, location=None, origin=None, destination=None):
        #self.n_seats = seats
        self.location = location
        self.origin = origin
        self.destination = destination
        self.company = company
        self.day = day
        #self.price = price
        self.id = idf
        #self.seat_prices = {price: seats}
        self.seat_prices = dict()
        self.add_price(price, seats)

    def add_price(self, price, seats):
        self.seat_prices[price] = seats

    def occupy_seat(self, seat):
        pass

    def check_capacity(self):
        pass

    def update_prices(self):
        pass


class Airline:
    def __init__(self, ids, idacc, name=None):
        self.name = name
        self.id = ids
        self.account = Account(idacc)
        # self.fun = random.randrange(100, 105)
        self.capacity = random.randrange(4, 8)
#        self.cost = self.fun / self.capacity
        self.cost = random.randrange(20, 30)

    def visit(self):  # só será chamada se check_capacity == True
        self.capacity -= 1

    def sell(self, amount):
        pass
#        if self.fun >= amount:
#            self.fun -= amount
#        return amount
#        else:
#            return False

    def check_capacity(self):
        if self.capacity == 0:
            return False
        else:
            return True

    def __str__(self):
        print(self.name)


class Passenger:
    def __init__(self, idag, iacc, *noneparm):
        self.utility = 0
        self.id = idag
        self.account = Account(iacc)
        self.local = None
        self.have_ticket = False
        self.destination = None

    def buy_ticket(self, price):
        pass

    def travel(self, destination):
        pass

    def get_utility(self, amount):
        self.utility += amount

    def check_funds(self, shop):
        if self.account.balance > shop.cost:
            return True
        else:
            return False

    def get_local(self):
        return self.local

    def set_local(self, local):
        self.local = local


if __name__ == '__main__':
    a1 = Passenger(0, 0)
    s1 = Airline(1, 1)
    # bb = Account('023')
    # print(bb.balance)
    # print(a1.account.balance)
    # print(s1.account.balance)
    # print(a1.account.id)
    a1.account.deposit(10)
    s1.account.deposit(s1.cost)
    a1.account.pay(s1.cost)
    # print('O custo da loja {} é R${:.2f} e a fun é {}.'.format(s1.id, s1.cost, s1.utility))
    print('O balanço corrente da loja {} é R${:.2f}'.format(s1.id, s1.account.balance))
    print('O agente tem R${:.2f} em caixa'.format(a1.account.balance))
