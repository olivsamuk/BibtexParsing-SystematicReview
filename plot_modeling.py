# Import libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)

plt.rc('font', size=16)          # controls default text sizes
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=16)    # fontsize of the tick labels
plt.rc('ytick', labelsize=16)    # fontsize of the tick labels
plt.rc('legend', fontsize=16)    # legend fontsize
plt.rc('figure', titlesize=16)  # fontsize of the figure title

papers = pd.read_csv("papers-categorized-new.csv")
data = {}
# COUNT PAPERS PER YEAR
counter = 0
for index, each_paper in papers.iterrows():
    if data.get(each_paper['modeling']):
        data[each_paper['modeling']]+=1
    else:
        data[each_paper['modeling']] = 1

models = data.keys()
amount = data.values()
print(models)
explode = (0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
colors = ( "orange", "cyan", "brown",
          "grey", "indigo", "beige")
wp = { 'linewidth' : 1, 'edgecolor' : "green" }
porcent = 100.*np.array(list(amount))/np.array(list(amount)).sum()
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(models, porcent)]

def func(pct, allvalues):
    absolute = int(pct / 100. * np.sum(allvalues))
    # return "{:.1f}%\n({:d})".format(pct, absolute)
    return "{:.1f}%".format(pct)


fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(amount,
                                  # autopct=lambda pct: func(pct, list(amount)),
                                    autopct='',
                                  explode=explode,
                                  # labels=models,
                                  shadow=True,
                                  colors=colors,
                                  startangle=90,
                                  wedgeprops=wp,
                                  textprops=dict(color="magenta"))
ax.legend(wedges, labels,
          title="System Modeling",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
# show plot
plt.show()