""" Projeto final
    Arquivo de criação de classes básicas
    """

__author__ = 'Pekka'


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
    def __init__(self, idf, company="", day=0, price=0, seats=0, origin=None, destination=None):
        #self.n_seats = seats
        #self.location = location
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

    def check_capacity(self, price):
        if self.seat_prices[price] > 0:
            return True
        elif self.seat_prices[price] == 0:
            try:
                del self.seat_prices[price]
                print('Company {} has no more seats'.format(self.company))
            except KeyError:
                print('Strange keyerror')
                pass
            return False
        else:
            print("Strangely there has been overbooking")
            return False

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

    # def visit(self):  # só será chamada se check_capacity == True
    #     self.capacity -= 1

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

    #def __str__(self):
     #   print(self.name)


class Passenger:
    def __init__(self, idag, iacc, *noneparm):
        self.utility = 0
        self.id = idag
        self.account = Account(iacc)
        self.local = None
        self.have_ticket = False
        self.destination = None
        self.travel_day = 99  # currently an integer, later possibly a date

    def buy_ticket(self, flights, airlines, shop_day):
        list_options = []
        minprice = 1000000
        minflight = None
        random.shuffle(flights)
        for f in flights:
            #print(f.company)
            if self.travel_day == f.day and len(f.seat_prices.keys()) > 0 and int(shop_day) < f.day:
                list_options.append(f)
                newprice = min(f.seat_prices.keys())
                if newprice < minprice:
                    minprice = newprice
                    minflight = f
                    #print(minflight)
            elif len(f.seat_prices.keys()) == 0:
                print('No more seats for the day on {}'.format(f.company))
        if minflight != None and self.check_funds(minflight):
            #s1.account.deposit(a[i].account.pay(s1.cost))
            for a in airlines:
                #print(a.name)
                if a.name == minflight.company:
                    # print(a.name)
                    break
            if minflight.check_capacity(minprice):
                a.account.deposit(self.account.pay(minprice))
                minflight.seat_prices[minprice] -= 1
                print('Ticket was sold for {} on {} for day {}. Seats remaining: {}'.format(minprice, minflight.company, minflight.day, minflight.seat_prices[minprice]))
                minflight.check_capacity(minprice)
                self.have_ticket = True
        elif minflight == None:
            print('No more seats for the day on any company.')



    def travel(self, destination):
        pass

    def get_utility(self, amount):
        self.utility += amount

    def check_funds(self, flight):
        if self.account.balance > min(flight.seat_prices.keys()):
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
