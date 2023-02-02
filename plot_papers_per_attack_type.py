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
        if i == 'passive':
            if 'Passive attacks (Eavesdropping)' not in new_values:
                new_values.append('Passive attacks (Eavesdropping)')
        elif i == 'actuator':
            if 'Actuator attacks' not in new_values:
                new_values.append('Actuator attacks')
        elif i == 'sensor':
            if 'Sensor attacks' not in new_values:
                new_values.append('Sensor attacks')
        elif i == 'sensor-actuator':
            if 'Sensor-actuator attacks' not in new_values:
                new_values.append('Sensor-actuator attacks')
        elif i == 'denail of service':
            if 'Denail of Service (DoS)' not in new_values:
                new_values.append('Denail of Service (DoS)')
    return new_values

def get_data(csv_file):
    papers = pd.read_csv(csv_file)
    data = {}
    for index, each_paper in papers.iterrows():
        if data.get(each_paper['attack']):
            data[each_paper['attack']] += 1
        else:
            data[each_paper['attack']] = 1
    return data

papers = get_data('papers-categorized-new.csv')
print(papers)

names = change_names(list(papers.keys()))
amount = list(papers.values())
print(names)

# # Create a circle at the center of the plot
# my_circle = plt.Circle((0, 0), 0.7, color='white')
#
# # Not enough colors --> colors will cycle
# plt.pie(size,wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' }, colors=['#6495ED', '#CCCCFF', '#DE3163', '#9FE2BF', '#40E0D0', '#FFBF00', '#FF7F50', '#7A1B9D'])
# p = plt.gcf()
# p.gca().add_artist(my_circle)
# plt.legend(names,
#           title="Attack types",
#           loc="center left",
#           bbox_to_anchor=(1, 0, 0.5, 1))
#
# # Show the graph
# plt.show()


fig, ax = plt.subplots()
size = 0.3

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(p=pct,v=val)
    return my_autopct


ax.pie([papers['actuator'], papers['sensor'], papers['sensor-actuator'], papers['denail of service'],papers['passive']],
       # labels=['Actuator attacks', 'Sensor attacks', 'Sensor-actuator attacks', 'Denail of Service (DoS)', 'Passive attacks (Eavesdropping)'],
        colors=['#929afc', '#929afc', '#929afc', '#929afc', '#FFFFFF','#40E0D0', '#FFBF00', '#FF7F50', '#7A1B9D'],
        # autopct=make_autopct([papers['actuator'], papers['sensor'], papers['sensor-actuator'], papers['denail of service'],papers['passive']]),
        pctdistance=0.8,
        radius=1, wedgeprops=dict(width=size, edgecolor='w', linewidth=2))
ax.pie([papers['actuator']+papers['sensor']+papers['sensor-actuator']+papers['denail of service'], papers['passive']],
       colors=['#636efa', '#4ddbb6'],
       # autopct=make_autopct([papers['actuator']+papers['sensor']+papers['sensor-actuator']+papers['denail of service'], papers['passive']]),
       pctdistance=.7,
       radius=1-size, wedgeprops=dict(width=size, edgecolor='w', linewidth=2))
# plt.title('Population')
plt.show()