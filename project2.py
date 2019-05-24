""" Projeto final
    Arquivo do modelo
    """

__author__ = 'Pekka'


from project1 import Airline, Passenger, Flight
import random
import pandas as pd


def create_agents(f, n, i, names=None):
    # o primeiro argumento desta função é a classe, assim ela pode ser usada tanto para agentes como para lojas
    lf = list()
    for k in range(n):
        lf.append(f(k, i, names[k] if names!=None else None))
        i += 1
    return lf


def init_flights(flighttab, airlinelist=None):
    k = 0
    flightlist = []
#    flightdict = {}
    #for j in airlinelist:
    for j in range(flighttab.shape[0]):
            # if j.name == flighttab.loc[i][0]:
        print(k, j, len(flightlist))
        name = flighttab.loc[j][0]
        day = flighttab.loc[j][1]
        price = flighttab.loc[j][2]
        seats = flighttab.loc[j][3]
        if flightlist != []:
            added = False
            for i in flightlist:
                if i.company == name and i.day == day:
                    i.add_price(price, seats)
                    added = True
                    break
            if added == False:
                flightlist.append(Flight(k, name, day, price, seats))
        elif len(flightlist) == 0:
            flightlist.append(Flight(k, name, day, price, seats))
        #flightlist.append(Flight(k, name, day, price, seats))  # original that didn't join prices
        k += 1
    return flightlist
    #return flightdict


def resources(a, average):
    for i in range(len(a)):
        a[i].account.deposit(random.randrange(average-0.1*average, average+0.1*average))


def interaction(a, s):
    # print([[a.fun, a.account.balance] for a in agents]) # é usado para ver se tudo funciona direito
    for i in range(len(a)):
        s1 = random.choice(s)
        # print(s1.id, s1.capacity, s1.cost) # mostra propriedades da loja
        if s1.check_capacity() and a[i].check_funds(s1):
            s1.visit()
            s1.account.deposit(a[i].account.pay(s1.cost))
            a[i].get_fun(s1.fun)
        else:
            # print('No capacity or funds!')
            continue
        # print([[a.fun, a.account.balance] for a in agents]) # mostra como mudou o estado dos agentes


def update_prices(airline):
    pass


def check_trip(passenger):
    pass
    return False




# def main(n1, n2, names):
#     # cria
#     # cria
#     # mistura (shuffle)
#     # mistura
#     # salários
#     # interact
#     list_airlines = create_agents(Airline, n2, 1, names)
#     list_passengers = create_agents(Passenger, n1, n2 + 1)
#     #random.shuffle(list_agents)
#     #random.shuffle(list_shops)
#     #resources(list_agents)
#     #interaction(list_agents, list_shops)
#     return list_passengers, list_airlines


if __name__ == '__main__':
    n_passengers = 13
    n_airlines = 4
    airline_names = ['ONE', 'AZU', 'GLO', 'TAM']
    locations = ['DF', 'SP']
    income = 1000
    # OS SEGUINTES COMANDOS FORAM TRANSFERIDOS NA FUNÇAÕ MAIN, PARA A ESTATÍSTICA PODER CHAMÁ-LA
    # list_agents = creation(Agent, n_agents, 1)
    # list_shops = creation(Shop, n_shops, n_agents+1)
    # resources(list_agents)
    # interaction(list_agents, list_shops)
    list_airlines = create_agents(Airline, n_airlines, 1, airline_names)
    list_passengers = create_agents(Passenger, n_passengers, n_airlines + 1)
    # initial flight values
    # company, day, price, seats
    # Avianca
    daylist = [str(i) for i in range(1, 8)]
    flighttable = pd.read_csv('flights2.csv', sep=';', index_col=False)
    flights = init_flights(flighttable)
    resources(list_passengers, income)

#    passengers, airlines = main(n_passengers, n_airlines, airline_names)
#    print(airlines)
    # print(i.name for i in list_airlines)

    for d in daylist:
        print('Day', d)
        for a in list_airlines:
            update_prices(a)

        for p in list_passengers:
            if not check_trip(p):
                p.buy_ticket(flights, list_airlines)

