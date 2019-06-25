""" Projeto final
    Arquivo do modelo
    """

__author__ = 'Pekka'


from project1 import Airline, Passenger, Flight
import random
import pandas as pd
from numpy.random import choice
from time import localtime, strftime
import os


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
        origin = flighttab.loc[j][4]
        destination = flighttab.loc[j][5]

        if flightlist != []:
            added = False
            for i in flightlist:
                if i.company == name and i.day == day and i.origin == origin and i.destination == destination:
                    i.add_price(price, seats)
                    added = True
                    break
            if added == False:
                flightlist.append(Flight(k, name, day, price, seats, origin, destination))

        elif len(flightlist) == 0:
            flightlist.append(Flight(k, name, day, price, seats, origin, destination))
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
    return passenger.have_ticket




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
    f = open('flights_'+strftime("%Y-%m-%d_%H%M%S", localtime())+'.txt', 'w')
    # from actual 2018 sales data
    demand = pd.DataFrame({'pax': {0: 369829, 1: 107078, 2: 47366, 3: 31385, 4: 20517, 5: 13535, 6: 8377, 7: 7356,
                                   8: 5257, 9: 3286, 10: 1834, 11: 595, 12: 133, 13: 41, 14: 17, 15: 16, 16: 1, 17: 1,
                                   18: 0},
                           'l': {0: 41.062000000000005, 1: 199.645, 2: 355.271, 3: 510.896, 4: 666.521, 5: 822.146,
                                 6: 977.772, 7: 1133.397, 8: 1289.022, 9: 1444.647, 10: 1600.273, 11: 1755.898,
                                 12: 1911.523, 13: 2378.399, 14: 2067.148, 15: 2222.774, 16: 2534.024, 17: 2845.275,
                                 18: 2689.649},
                           'r': {0: 199.645, 1: 355.271, 2: 510.896, 3: 666.521, 4: 822.146, 5: 977.772, 6: 1133.397,
                                 7: 1289.022, 8: 1444.647, 9: 1600.273, 10: 1755.898, 11: 1911.523, 12: 2067.148,
                                 13: 2534.024, 14: 2222.774, 15: 2378.399, 16: 2689.649, 17: 3000.9, 18: 2845.275}})
    onedemand = pd.DataFrame({'pax': {0: 39073, 1: 29807, 2: 23858, 3: 9631, 4: 8448, 5: 5141, 6: 4308, 7: 2722, 8: 1918, 9: 1532, 10: 1472, 11: 547, 12: 392, 13: 35, 14: 19, 15: 15, 16: 8, 17: 5, 18: 3}, 'l': {0: 76.923, 1: 188.277, 2: 297.555, 3: 406.832, 4: 516.109, 5: 625.387, 6: 734.664, 7: 843.942, 8: 953.219, 9: 1171.774, 10: 1062.496, 11: 1281.051, 12: 1390.328, 13: 1827.438, 14: 1499.606, 15: 1936.715, 16: 2045.993, 17: 1608.883, 18: 1718.161}, 'r': {0: 188.277, 1: 297.555, 2: 406.832, 3: 516.109, 4: 625.387, 5: 734.664, 6: 843.942, 7: 953.219, 8: 1062.496, 9: 1281.051, 10: 1171.774, 11: 1390.328, 12: 1499.606, 13: 1936.715, 14: 1608.883, 15: 2045.993, 16: 2155.27, 17: 1718.161, 18: 1827.438}})
    azudemand = pd.DataFrame({'pax': {0: 58765, 1: 15535, 2: 8647, 3: 7624, 4: 5161, 5: 2844, 6: 1755, 7: 792, 8: 285, 9: 253, 10: 152, 11: 57, 12: 13, 13: 5, 14: 4, 15: 1, 16: 0, 17: 0, 18: 0}, 'l': {0: 41.062000000000005, 1: 199.645, 2: 355.271, 3: 510.896, 4: 666.521, 5: 822.146, 6: 977.772, 7: 1133.397, 8: 1289.022, 9: 1444.647, 10: 1600.273, 11: 1755.898, 12: 2222.774, 13: 2067.148, 14: 1911.523, 15: 2845.275, 16: 2689.649, 17: 2378.399, 18: 2534.024}, 'r': {0: 199.645, 1: 355.271, 2: 510.896, 3: 666.521, 4: 822.146, 5: 977.772, 6: 1133.397, 7: 1289.022, 8: 1444.647, 9: 1600.273, 10: 1755.898, 11: 1911.523, 12: 2378.399, 13: 2222.774, 14: 2067.148, 15: 3000.9, 16: 2845.275, 17: 2534.024, 18: 2689.649}})
    glodemand = pd.DataFrame({'pax': {0: 95943, 1: 30333, 2: 12131, 3: 8716, 4: 5335, 5: 3414, 6: 3309, 7: 2931, 8: 2225, 9: 1835, 10: 1772, 11: 1655, 12: 1618, 13: 1150, 14: 1102, 15: 694, 16: 324, 17: 182, 18: 54}, 'l': {0: 49.951, 1: 154.426, 2: 256.953, 3: 359.479, 4: 462.005, 5: 667.058, 6: 564.532, 7: 769.584, 8: 872.111, 9: 974.637, 10: 1179.689, 11: 1077.163, 12: 1282.216, 13: 1384.742, 14: 1487.268, 15: 1589.795, 16: 1692.321, 17: 1794.847, 18: 1897.374}, 'r': {0: 154.426, 1: 256.953, 2: 359.479, 3: 462.005, 4: 564.532, 5: 769.584, 6: 667.058, 7: 872.111, 8: 974.637, 9: 1077.163, 10: 1282.216, 11: 1179.689, 12: 1384.742, 13: 1487.268, 14: 1589.795, 15: 1692.321, 16: 1794.847, 17: 1897.374, 18: 1999.9}})
    tamdemand = pd.DataFrame({'pax': {0: 144961, 1: 29896, 2: 11440, 3: 7535, 4: 3802, 5: 2810, 6: 2492, 7: 1772, 8: 1680, 9: 1647, 10: 1081, 11: 903, 12: 501, 13: 96, 14: 45, 15: 34, 16: 8, 17: 4, 18: 3}, 'l': {0: 42.404, 1: 181.579, 2: 318.158, 3: 454.737, 4: 591.316, 5: 727.895, 6: 864.474, 7: 1137.632, 8: 1274.211, 9: 1001.053, 10: 1410.789, 11: 1547.368, 12: 1683.947, 13: 1820.526, 14: 1957.105, 15: 2366.842, 16: 2503.421, 17: 2093.684, 18: 2230.263}, 'r': {0: 181.579, 1: 318.158, 2: 454.737, 3: 591.316, 4: 727.895, 5: 864.474, 6: 1001.053, 7: 1274.211, 8: 1410.789, 9: 1137.632, 10: 1547.368, 11: 1683.947, 12: 1820.526, 13: 1957.105, 14: 2093.684, 15: 2503.421, 16: 2640.0, 17: 2230.263, 18: 2366.842}})

    demand = demand.sort_values('l')
    onedemand = onedemand.sort_values('l')
    azudemand = azudemand.sort_values('l')
    glodemand = glodemand.sort_values('l')
    tamdemand = tamdemand.sort_values('l')
    demandlist = [onedemand, azudemand, glodemand, tamdemand]

    load_factor2018 = 0.813  # grau de ocupação
    lf_glo = 0.808
    lf_azu = 0.808
    lf_one = 0.844
    lf_tam = 0.813

    totalpax_sales = sum(demand.pax)  # 616624, less than a third from realized
    totalpax_2018 = 2076582
    pax_one_2018 = 312427
    pax_azu_2018 = 249442
    pax_glo_2018 = 608699
    pax_tam_2018 = 906014

    cap_one = round(pax_one_2018 / lf_one)
    cap_azu = round(pax_azu_2018 / lf_azu)
    cap_glo = round(pax_glo_2018 / lf_glo)
    cap_tam = round(pax_tam_2018 / lf_tam)
    caplist = [cap_one, cap_azu, cap_glo, cap_tam]
    caplist = [i//1000 for i in caplist]  # to compensate the division of passengers below

    df_habitantes2018 = 2974703

    prob_pax = totalpax_2018 / df_habitantes2018
    prob_pax /= load_factor2018  # to make possible to fill the flights

    n_passengers = totalpax_2018//1000  # to speed up the simulation
    n_airlines = 4
    airline_names = ['ONE', 'AZU', 'GLO', 'TAM']
    locations = ['DF', 'SP']
    # income = 1000
    # OS SEGUINTES COMANDOS FORAM TRANSFERIDOS NA FUNÇAÕ MAIN, PARA A ESTATÍSTICA PODER CHAMÁ-LA
    # list_agents = creation(Agent, n_agents, 1)
    # list_shops = creation(Shop, n_shops, n_agents+1)
    # resources(list_agents)
    # interaction(list_agents, list_shops)
    list_airlines = create_agents(Airline, n_airlines, 1, airline_names)
    list_passengers = create_agents(Passenger, n_passengers, n_airlines + 1)
    for a in range(len(list_airlines)):
        list_airlines[a].capacity = caplist[a]
    # initial flight values
    # company, day, price, seats
    #daylist = [str(i) for i in range(0, 8)]
    daylist = [1] # we are temporarily inspecting the whole year
    daily_sales = 100
#    daylist = [str(i) for i in range(1, 3)]
    for p in list_passengers:
#        p.travel_day = random.randint(1,7)
        p.travel_day = 1  # temporário
#        randomlocalindex = random.randint(0,1)
        randomlocalindex = 0
        p.local = locations[randomlocalindex]
        p.destination = locations[1-randomlocalindex]
        p.maxprice = choice(demand.r, p=demand.pax/sum(demand.pax))
#    flighttable = pd.read_csv('flights3.csv', sep=';', index_col=False)
#    flights = init_flights(flighttable)
    flight_archive = {} # create archive of flights to enable comparison of the flight stock
#    resources(list_passengers, income)

#    passengers, airlines = main(n_passengers, n_airlines, airline_names)
#    print(airlines)
    # print(i.name for i in list_airlines)

#    pax_counter = 1
    #for p in list_passengers:


    for d in daylist:
        print('Day', d)
        print('======')
        f.write('Period ' + str(d) + '\n')
        f.write('======\n')
#        random.shuffle(list_airlines)
#        for a in list_airlines:
#            update_prices(a)
#        dayseatcounter = 0
#        flight_archive[int(d)] = flights.copy()
#        for n in flights:
#            if n.day == int(d):
#                dayseatcounter += sum(n.seat_prices.values())
#        print('Flights for day: {}'.format(dayseatcounter))
#        random.shuffle(list_passengers)
#        sampled_list_passengers = random.sample(list_passengers, daily_sales)
        #random.shuffle(flights)
        pax_counter = 1
        for p in list_passengers:
#        for p in sampled_list_passengers:
#            if not check_trip(p):
            flights = list()
            for fl in range(len(airline_names)):
                if list_airlines[fl].capacity > 0:
                    flights.append(Flight(idf=fl, company=airline_names[fl], day=1, price=choice(demandlist[fl].r, p=demandlist[fl].pax/sum(demandlist[fl].pax)), seats=2, origin='DF', destination='SP'))
            if random.random() < prob_pax:
#                print('Passenger {} of {}'.format(pax_counter, len(list_passengers)))
                #print('Passenger {} of {}'.format(pax_counter, len(sampled_list_passengers)))
                #p.buy_ticket(flights, list_airlines, d)
                p.buy_ticket(flights, list_airlines, d-1)
#                pax_counter += 1
            else:
                print('not a passenger candidate')
#                 print('Already has a ticket')
#                 if int(d) == p.travel_day:
#                     print('Travelling today from {} to {}'.format(p.local, p.destination))
#                     newlocal = p.destination
#                     p.destination = p.local
#                     p.local = newlocal

            pax_counter += 1
            # print('Passenger {} of {}'.format(pax_counter, len(list_passengers)))
            # print('-----------------------')
            # if not check_trip(p):
            #     p.buy_ticket(flights, list_airlines, d)
            # else:
            #     print('Already has a ticket')
            # pax_counter += 1
    total_pax_flown = 0
    for a in list_airlines:
        print('Airline {}:\t Tickets sold: {} \t Revenue: {:.2f}\t Average price: {:.2f}'.format(a.name, a.sold_tickets, a.account.balance, a.account.balance/a.sold_tickets))
        f.write('Airline {}:\t Tickets sold: {} \t Revenue: {:.2f}\t Average price: {:.2f}\n'.format(a.name, a.sold_tickets, a.account.balance, a.account.balance/a.sold_tickets))
        total_pax_flown += a.sold_tickets
    print('Total passengers for period: {}'.format(total_pax_flown))
    f.write('Total passengers for period: {}\n'.format(total_pax_flown))
    f.close()
