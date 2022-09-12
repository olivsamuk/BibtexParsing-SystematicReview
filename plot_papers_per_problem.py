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
print(names, papers.values())
size = list(papers.values())

# Create a circle at the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# Not enough colors --> colors will cycle
plt.pie(size,wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' }, colors=['#6495ED', '#CCCCFF', '#DE3163', '#9FE2BF', '#40E0D0', '#FFBF00', '#FF7F50', '#7A1B9D'])
p = plt.gcf()
p.gca().add_artist(my_circle)

plt.legend(names,
          title="Strategies in Cyber-security of DES",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Show the graph
plt.show()