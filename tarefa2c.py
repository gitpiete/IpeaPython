""" exercicio 2: agentes e interações
    Arquivo de cálculo de médias
    """

from tarefa2b import main
import os
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # agentlist = [10, 100, 200, 500, 1000, 2000, 5000, 10000]
    agentlist = [10, 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 4000,
                 5000, 6000, 7000, 8000, 9000, 10000]
    # shoplist = [4, 10, 20, 50, 100, 200, 500, 1000]
    shoplist = [20] * len(agentlist)  # simular com um tamanho de loja
    filename = 'results.csv'
    # inicializar listas dos resultados para facilitar o desenho de gráfico
    funlist = []
    agballist = []
    shballist = []
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'a') as f:
        f.write('No. Agents; No. Shops; Average Fun; Average Agent Account Balance; '
                'Average Shop Account Balance; Average Cost\n')
        for i in range(len(agentlist)):
            # print(i)
            agents, shops = main(agentlist[i], shoplist[i])
            avg_fun = sum([a.fun for a in agents])/len(agents)
            avg_agent_balance = sum([a.account.balance for a in agents])/len(agents)
            avg_shop_balance = sum([s.account.balance for s in shops])/len(shops)
            avg_cost = sum([s.cost for s in shops])/len(shops)
#            print(avg_fun, avg_agent_balance, avg_shop_balance, avg_cost)
#            f.write(str([agentlist[i], shoplist[i], avg_fun, avg_agent_balance, avg_shop_balance, avg_cost]))
            f.write('{}; {}; {:.2f}; {:.2f}; {:.2f}; {:.2f}'
                    .format(agentlist[i], shoplist[i], avg_fun, avg_agent_balance, avg_shop_balance, avg_cost))
            f.write('\n')
            funlist.append(avg_fun)
            agballist.append(avg_agent_balance)
            shballist.append(avg_shop_balance)

    plt.plot(agentlist, funlist, 'ro-', label='Average Fun')
    plt.plot(agentlist, agballist, 'bo-', label='Average Agent Account Balance')
    plt.plot(agentlist, shballist, 'go-', label='Average Shop Account Balance')
    legend = plt.legend(loc='center', shadow=True)
    xlabel = plt.xlabel('No. of Agents')
    plt.show()
