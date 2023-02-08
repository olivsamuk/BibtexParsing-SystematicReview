# # Import libraries
# from matplotlib import pyplot as plt
# import numpy as np
# import pandas as pd
#
# font = {'family' : 'Latin Modern Roman'}
# plt.rc('font', **font)
#
# plt.rc('font', size=16)          # controls default text sizes
# plt.rc('axes', titlesize=16)     # fontsize of the axes title
# plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
# plt.rc('xtick', labelsize=16)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=16)    # fontsize of the tick labels
# plt.rc('legend', fontsize=16)    # legend fontsize
# plt.rc('figure', titlesize=16)  # fontsize of the figure title
#
# def update_mf(data):
#     modeling_formalisms = {'finite-state automata': 0, 'petri nets': 0, 'finite-state transducer': 0,
#                            'Labeled Transition System (LTS)': 0, 'Markov Models': 0}
#     print(data.keys())
#     for each_mf in data.keys():
#         if each_mf == 'finite-state automata':
#             modeling_formalisms['finite-state automata']+=data[each_mf]
#         elif each_mf == 'petri nets':
#             modeling_formalisms['petri nets'] +=data[each_mf]
#         elif each_mf == 'signal interpreted Petri nets':
#             modeling_formalisms['petri nets'] +=data[each_mf]
#         elif each_mf == 'finite-state transducer':
#             modeling_formalisms['finite-state transducer'] +=data[each_mf]
#         elif each_mf == 'probabilistic finite-state automata':
#             modeling_formalisms['finite-state automata'] +=data[each_mf]
#         elif each_mf == 'Labeled Transition System (LTS)':
#             modeling_formalisms['Labeled Transition System (LTS)'] +=data[each_mf]
#         elif each_mf == 'Hidden Markov Model (HMM)':
#             modeling_formalisms['Markov Models']+=data[each_mf]
#         elif each_mf == 'Stochastic Petri nets':
#             modeling_formalisms['petri nets'] +=data[each_mf]
#         elif each_mf == 'timed finite-state automata':
#             modeling_formalisms['finite-state automata'] +=data[each_mf]
#         elif each_mf == 'Markov Decision Process (MDP)':
#             modeling_formalisms['Markov Models']+=data[each_mf]
#
#     return modeling_formalisms
#
# papers = pd.read_csv("papers-categorized-new.csv")
# data = {}
# # COUNT PAPERS PER YEAR
# counter = 0
# for index, each_paper in papers.iterrows():
#     if data.get(each_paper['modeling']):
#         data[each_paper['modeling']]+=1
#     else:
#         data[each_paper['modeling']] = 1
#
# models = data.keys()
# amount = data.values()
# final = dict(zip(models, amount))
# geral = update_mf(final)
#
#
# # explode = (0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0)
# colors = ( "orange", "cyan", "brown",
#           "grey", "indigo", "beige")
# wp = { 'linewidth' : 1, 'edgecolor' : "green" }
# # porcent = 100.*np.array(list(amount))/np.array(list(amount)).sum()
# # labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(models, porcent)]
# labels = ['{0} - {1}'.format(i,j) for i,j in zip(geral.keys(), geral.values())]
#
# def func(pct, allvalues):
#     absolute = int(pct / 100. * np.sum(allvalues))
#     # return "{:.1f}%\n({:d})".format(pct, absolute)
#     return "{:.1f}%".format(pct)
#
#
# fig, ax = plt.subplots(figsize=(10, 7))
# wedges, texts, autotexts = ax.pie(geral.values(),
#                                   # autopct=lambda pct: func(pct, list(amount)),
#                                     autopct='',
#                                   # explode=explode,
#                                   # labels=models,
#                                   shadow=True,
#                                   colors=colors,
#                                   startangle=90,
#                                   wedgeprops=wp,
#                                   textprops=dict(color="magenta"))
# ax.legend(wedges, labels,
#           title="System Modeling",
#           loc="center left",
#           bbox_to_anchor=(1, 0, 0.5, 1))
#
# plt.setp(autotexts, size=8, weight="bold")
# # show plot
# plt.show()



#--------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)

plt.rc('font', size=18)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.rc('legend', fontsize=18)    # legend fontsize
plt.rc('figure', titlesize=18)  # fontsize of the figure title

def update_mf(data):
    modeling_formalisms = {'finite-state automata': 0, 'petri nets': 0, 'finite-state transducer': 0,
                           'Labeled Transition System (LTS)': 0, 'Markov Models': 0}
    for each_mf in data.keys():
        if each_mf == 'finite-state automata':
            modeling_formalisms['finite-state automata']+=data[each_mf]
        elif each_mf == 'petri nets':
            modeling_formalisms['petri nets'] +=data[each_mf]
        elif each_mf == 'signal interpreted Petri nets':
            modeling_formalisms['petri nets'] +=data[each_mf]
        elif each_mf == 'finite-state transducer':
            modeling_formalisms['finite-state transducer'] +=data[each_mf]
        elif each_mf == 'probabilistic finite-state automata':
            modeling_formalisms['finite-state automata'] +=data[each_mf]
        elif each_mf == 'Labeled Transition System (LTS)':
            modeling_formalisms['Labeled Transition System (LTS)'] +=data[each_mf]
        elif each_mf == 'Hidden Markov Model (HMM)':
            modeling_formalisms['Markov Models']+=data[each_mf]
        elif each_mf == 'Stochastic Petri nets':
            modeling_formalisms['petri nets'] +=data[each_mf]
        elif each_mf == 'timed finite-state automata':
            modeling_formalisms['finite-state automata'] +=data[each_mf]
        elif each_mf == 'Markov Decision Process (MDP)':
            modeling_formalisms['Markov Models']+=data[each_mf]

    return modeling_formalisms

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
final = dict(zip(models, amount))
geral = update_mf(final)
print('final: ', final.keys(), '\n', 'geral: ', geral.keys(), '\ndata: ', data)

fig, ax = plt.subplots()
size = 0.3

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(p=pct,v=val)
    return my_autopct


ax.pie([final['finite-state automata'], final['probabilistic finite-state automata'], final['timed finite-state automata'], final['Hidden Markov Model (HMM)'], final['Markov Decision Process (MDP)'], final['petri nets'], final['signal interpreted Petri nets'], final['Stochastic Petri nets'], final['finite-state transducer'], final['Labeled Transition System (LTS)']],
#        labels=['finite-state automata',
# 'probabilistic finite-state automata',
# 'timed finite-state automata',
# 'Hidden Markov Model (HMM)',
# 'Markov Decision Process (MDP)',
# 'petri nets',
# 'signal interpreted Petri nets',
# 'Stochastic Petri nets',
# 'finite-state transducer',
# 'Labeled Transition System (LTS)'],
        colors=['#85C1E9', '#2E86C1', '#21618C', '#FFFFFF','#FFFFFF', '#D68910', '#F4D03F', '#F9E79F', '#FFFFFF','#FFFFFF' ],
        # autopct=make_autopct([papers['actuator'], papers['sensor'], papers['sensor-actuator'], papers['denail of service'],papers['passive']]),
        pctdistance=0.8,
        radius=1, wedgeprops=dict(width=size, edgecolor='w', linewidth=2))

ax.pie([final['finite-state automata']+final['probabilistic finite-state automata']+final['timed finite-state automata'], final['Hidden Markov Model (HMM)']+final['Markov Decision Process (MDP)'], final['petri nets']+final['signal interpreted Petri nets']+final['Stochastic Petri nets'], final['finite-state transducer'], final['Labeled Transition System (LTS)']],
       # labels=['finite-state automata',
       #  'Markov Models',
       # 'petri nets',
       # 'finite-state transducer',
       # 'Labeled Transition System (LTS)'],
       # colors=['#929afc','#40E0D0', '#FFBF00', '#FF7F50', '#7A1B9D', '#cccccc'],
        colors=['#1B4F72', '#186A3B', '#7E5109', '#626567', '#78281F'],
       # autopct=make_autopct([papers['actuator']+papers['sensor']+papers['sensor-actuator']+papers['denail of service'], papers['passive']]),
       pctdistance=.7,
       radius=1-size, wedgeprops=dict(width=size, edgecolor='w', linewidth=2))
# plt.title('Population')


plt.show()