from tarefa2b import main


if __name__ == '__main__':
    agentlist = [10, 100, 200, 500, 1000, 2000, 5000, 10000]
    shoplist = [4, 10, 20, 50, 100, 200, 500, 1000]
    with open('results.csv', 'a') as f:
        for i in range(len(agentlist)):
            print(i)

            agents, shops = main(agentlist[i], shoplist[i])
            avg_fun = sum([agents[j].fun for j in range(len(agents))])/len(agents)
            avg_balance = sum([agents[j].account.balance for j in range(len(agents))])/len(agents)
            avg_cost = sum([shops[j].cost for j in range(len(shops))])/len(shops)
            print(avg_fun, avg_balance, avg_cost)
            f.write(str([agentlist[i], shoplist[i], avg_fun, avg_balance, avg_cost]))

