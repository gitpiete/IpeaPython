

from tarefa2 import Agent, Shop
import random


def creation(f, n, i):
    lf = list()
    for k in range(n):
        lf.append(f(k, i))
        i += 1
    return lf


def resources(a):
    for i in range(len(a)):
        a[i].account.deposit(random.randrange(10, 50))


def interaction(agents, shops):
    #print([[a.fun, a.account.balance] for a in agents])
    for i in range(len(agents)):
        s1 = random.choice(shops)
        #print(s1.id, s1.capacity, s1.cost)
        if s1.check_capacity() and agents[i].check_funds(s1):
            s1.visit()
            s1.account.deposit(agents[i].account.pay(s1.cost))
            agents[i].get_fun(s1.fun)
        else:
            #print('No capacity or funds!')
            continue
        #print([[a.fun, a.account.balance] for a in agents])


def averages(a, s):

    avg_balance = sum(i.account.balance for x in [a, s] for i in x) / (len(a) + len(s))

def main(n1, n2):
# cria
# cria
# mistura (shuffle)
# mistura
# salários
# interact
    list_agents = creation(Agent, n1, 1)
    list_shops = creation(Shop, n2, n1 + 1)
    resources(list_agents)
    interaction(list_agents, list_shops)

    return list_agents, list_shops

if __name__ == '__main__':
    n_agents = 13
    n_shops = 3
    # OS SEGUINTES COMANDOS FORAM TRANSFERIDOS NA FUNÇAÕ MAIN, PARA A ESTATÍSTICA PODER CHAMÁ-LA
    # list_agents = creation(Agent, n_agents, 1)
    # list_shops = creation(Shop, n_shops, n_agents+1)
    # resources(list_agents)
    # interaction(list_agents, list_shops)
    main(n_agents, n_shops)
