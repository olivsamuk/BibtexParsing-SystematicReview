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

def change_names(values):
    new_values = []
    for i in values:
        if i == 'attack detection and mitigation':
            if 'Attack detection and mitigation' not in new_values:
                new_values.append('Attack detection and mitigation')
        elif i == 'verification':
            if 'Formalization and verification of properties' not in new_values:
                new_values.append('Formalization and verification of properties')
        elif i == 'enforcement':
            if 'Enforcement of properties' not in new_values:
                new_values.append('Enforcement of properties')
        elif i == 'attack model':
            if 'Attack synthesis' not in new_values:
                new_values.append('Attack synthesis')
        elif i == 'supervisor synthesis':
            if 'Supervisor synthesis' not in new_values:
                new_values.append('Supervisor synthesis')
        elif i == 'diagnosabilty':
            if 'Diagnosability' not in new_values:
                new_values.append('Diagnosability')
        elif i == 'state estimation':
            if 'State estimation' not in new_values:
                new_values.append('State estimation')
        elif i == 'system recovery':
            if 'System recovery' not in new_values:
                new_values.append('System recovery')
    return new_values

def get_data(csv_file):
    papers = pd.read_csv(csv_file)
    data = {}
    for index, each_paper in papers.iterrows():
        if data.get(each_paper['problem']):
            data[each_paper['problem']] += 1
        else:
            data[each_paper['problem']] = 1
    return data

papers = get_data('papers-categorized-new.csv')

# ------------------ BAR CHART ---------------------------------------------------------------
# width = .8       # the width of the bars: can also be len(x) sequence
#
#
#
# fig, ax = plt.subplots()
#
# bars = ax.bar(papers.keys(), papers.values(), width, label='Artigos', zorder=2,color='#27AE60', edgecolor='#145A32')
# ax.bar_label(bars)
#
#
# plt.xticks(list(papers.keys()), rotation=45, ha='right')
#
# plt.tick_params(
#     axis='y',  # changes apply to the x-axis
#     which='both',  # both major and minor ticks are affected
#     bottom=False,  # ticks along the bottom edge are off
#     top=False,  # ticks along the top edge are off
#     labelbottom=False)  # labels along the bottom edge are off
#
# plt.grid(zorder=1, linestyle='-', color='#EAEDED')
#
# counter = 0
# for spine in plt.gca().spines.values():
#     if counter == 2 or counter == 0:
#         spine.set_visible(True)
#     else:
#         spine.set_visible(False)
#     counter += 1
#
#
# plt.show()
# ------------------ DONUT CHART ---------------------------------------------------------------


names = change_names(list(papers.keys()))
print(papers)
amount = list(papers.values())

strategies_grouped          = [papers['verification']+papers['enforcement'], papers['attack model'], papers['attack detection and mitigation']+papers['supervisor synthesis']+papers['system recovery'], papers['diagnosabilty'], papers['state estimation']]
strategies_grouped_label    = ['Protection of secrets', 'Attack synthesis', 'Attack-tolerant control', 'Fault diagnosis', 'State estimation']
strategies_ungrouped        = [papers['verification'],papers['enforcement'], papers['attack model'], papers['attack detection and mitigation'],papers['supervisor synthesis'],papers['system recovery'], papers['diagnosabilty'], papers['state estimation']]
strategies_ungrouped_label  = ['Verification', 'Enforcement', 'Attack synthesis', 'Attack detection', 'Supervisor synthesis', 'System recovery', 'Fault diagnosis', 'State estimation']

fig, ax = plt.subplots()
size = 0.3

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(p=pct,v=val)
    return my_autopct


ax.pie(strategies_ungrouped,
       labels=strategies_ungrouped_label,
        colors=['#929afc', '#929afc', '#FFFFFF', '#f48876', '#f48876', '#f48876','#FFFFFF', '#FFFFFF'],
        # autopct=make_autopct(strategies_ungrouped),
        pctdistance=0.8,
        radius=1, wedgeprops=dict(width=size, edgecolor='w', linewidth=2))


ax.pie(strategies_grouped,
       labels=strategies_grouped_label,
       colors=['#636efa', '#4ddbb6', '#ef553b', '#c492fc', '#ffbd8c'],
       autopct=make_autopct(strategies_grouped),
       pctdistance=.7,
       radius=1-size, wedgeprops=dict(width=size, edgecolor='w', linewidth=2))
# plt.title('Population')
plt.show()