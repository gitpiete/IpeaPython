
import pandas as pd
from os import listdir
import seaborn as sns

pricepath = "c:\\abm\\prices\\"

print(listdir(pricepath))

#yearprices = pd.DataFrame()
yearprices = []
testread = pd.read_csv(pricepath + '201803.csv', skiprows=0, sep=';', header=0, encoding = 'cp1252')

counter = 0
for f in listdir(pricepath):
    counter += 1
    print(counter)
    monthprices = pd.read_csv(pricepath + f, skiprows=1, sep=';', decimal=',', encoding = 'cp1252', names = ['ANO',  'MES', 'EMPRESA', 'ORIGEM', 'DESTINO',  'TARIFA',  'ASSENTOS'])
    yearprices.append(monthprices)

yearpriceframe = pd.concat(yearprices, axis=0)

yearpriceframe.ORIGEM.unique()

dfspprices = yearpriceframe[(yearpriceframe['ORIGEM']=='SBBR') & (yearpriceframe['DESTINO'].isin(['SBSP', 'SBGR', 'SBKP']))]
spdfprices = yearpriceframe[(yearpriceframe['DESTINO']=='SBBR') & (yearpriceframe['ORIGEM'].isin(['SBSP', 'SBGR', 'SBKP']))]

print(dfspprices.shape)
#hist = dfspprices.hist(bins=30)
dfspprices = dfspprices.reset_index(drop=True)
dfsppricessep = dfspprices.reindex(dfspprices.index.repeat(dfspprices.ASSENTOS))
print(dfsppricessep.shape)

#hist2 = dfsppricessep.hist(column='TARIFA', bins=31)

max(dfsppricessep.TARIFA)

demanddist = dfsppricessep.TARIFA.value_counts(bins=19)
dfsppricessep.EMPRESA.unique()
ddone = dfsppricessep[dfsppricessep.EMPRESA=='ONE'].TARIFA.value_counts(bins=19)
ddazu = dfsppricessep[dfsppricessep.EMPRESA=='AZU'].TARIFA.value_counts(bins=19)
ddglo = dfsppricessep[dfsppricessep.EMPRESA=='GLO'].TARIFA.value_counts(bins=19)
ddtam = dfsppricessep[dfsppricessep.EMPRESA=='TAM'].TARIFA.value_counts(bins=19)

dd2 = demanddist.reset_index().rename(columns={'index':'bin'})
dd2.head()
ddone2 = ddone.reset_index().rename(columns={'index':'bin'})
ddazu2 = ddazu.reset_index().rename(columns={'index':'bin'})
ddglo2 = ddglo.reset_index().rename(columns={'index':'bin'})
ddtam2 = ddtam.reset_index().rename(columns={'index':'bin'})

ddone2.head()
print(dd2)
#demanddist = dfsppricessep.TARIFA.value_counts(bins=19).reset_index().rename(columns={'index':'bin'})
#demanddist[['l', 'r']] = pd.DataFrame([(x.left, x.right) for x in demanddist['index']])
dd2[['l', 'r']] = pd.DataFrame([(x.left, x.right) for x in dd2['bin']])
for a in [ddone2, ddazu2, ddglo2, ddtam2]:
    a[['l', 'r']] = pd.DataFrame([(x.left, x.right) for x in a['bin']])

print(ddone2)
#demanddist['lower'] = demanddist.index.left
#demanddist['upper'] = demanddist.index.right
print(dd2)
dd3 = dd2[['TARIFA', 'l', 'r']]
dd3.to_dict()
ddone3 = ddone2[['TARIFA', 'l', 'r']]
ddazu3 = ddazu2[['TARIFA', 'l', 'r']]
ddglo3 = ddglo2[['TARIFA', 'l', 'r']]
ddtam3 = ddtam2[['TARIFA', 'l', 'r']]

for a in [ddone3, ddazu3, ddglo3, ddtam3]:
    print(a.to_dict())

len(dfsppricessep.TARIFA)

#priceinf = sns.distplot(dfsppricessep.TARIFA, hist=True, kde=True, bins=31)
#priceinf2 = sns.distplot(dfsppricessep.TARIFA, hist=True, kde=False, bins=31)

#kvalues = sns.kdeplot(dfsppricessep.TARIFA, bw=100)


# import scipy
# import scipy.stats
# import matplotlib
# import matplotlib.pyplot as plt
#
#
# class Distribution(object):
#
#     def __init__(self, dist_names_list=[]):
# #        self.dist_names = ['norm', 'lognorm', 'expon', 'pareto']
#         self.dist_names = ['expon']
#         self.dist_results = []
#         self.params = {}
#
#         self.DistributionName = ""
#         self.PValue = 0
#         self.Param = None
#
#         self.isFitted = False
#
#     def Fit(self, y):
#         self.dist_results = []
#         self.params = {}
#         for dist_name in self.dist_names:
#             dist = getattr(scipy.stats, dist_name)
#             param = dist.fit(y)
#
#             self.params[dist_name] = param
#             # Applying the Kolmogorov-Smirnov test
#             D, p = scipy.stats.kstest(y, dist_name, args=param);
#             self.dist_results.append((dist_name, p))
#
#         # select the best fitted distribution
#         sel_dist, p = (max(self.dist_results, key=lambda item: item[1]))
#         # store the name of the best fit and its p value
#         self.DistributionName = sel_dist
#         self.PValue = p
#
#         self.isFitted = True
#         return self.DistributionName, self.PValue
#
#     def Random(self, n=1):
#         if self.isFitted:
#             dist_name = self.DistributionName
#             param = self.params[dist_name]
#             # initiate the scipy distribution
#             dist = getattr(scipy.stats, dist_name)
#             return dist.rvs(*param[:-2], loc=param[-2], scale=param[-1], size=n)
#         else:
#             raise ValueError('Must first run the Fit method.')
#
#     def Plot(self, y):
#         x = self.Random(n=len(y))
#         plt.hist(x, alpha=0.5, label='Fitted')
#         plt.hist(y, alpha=0.5, label='Actual')
#         plt.legend(loc='upper right')
#
#
# from scipy.stats import expon
# r = expon.rvs(size=5000) #exponential
#
# dst = Distribution()
# #dst.
# dst.Fit(dfsppricessep.TARIFA)
# dst.Plot(dfsppricessep.TARIFA)
#
# p1 = 44.02
# p2 = 236.01597146721505
#
# import numpy as np
# fig, ax = plt.subplots(1, 1)
# #x = np.linspace(expon.ppf(0.01),expon.ppf(0.99), 100)
# x = np.linspace(expon.ppf(0.01, p1, p2),expon.ppf(0.99, p1, p2), 100)
# #ax.plot(x, expon.pdf(x), 'r-', lw=5, alpha=0.6, label='expon pdf')
# ax.plot(x, expon.pdf(x, p1, p2), 'r-', lw=5, alpha=0.6, label='expon pdf')
# rv = expon(p1, p2)
# ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
# vals = expon.ppf([0.001, 0.5, 0.999])
# np.allclose([0.001, 0.5, 0.999], expon.cdf(vals))
# r = expon.rvs(size=1000)
# ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
# ax.legend(loc='best', frameon=False)
# plt.show()
