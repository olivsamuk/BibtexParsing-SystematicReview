# Import Library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)

plt.rc('font', size=18)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.rc('legend', fontsize=18)    # legend fontsize
plt.rc('figure', titlesize=18)  # fontsize of the figure title
# Define Data
# team = ['Team 1','Team 2','Team 3','Team 4','Team 5']
# female = [5, 10, 15, 20, 25]
# male = [15, 20, 30, 16, 13]
def get_sum(p,q):
    result = []
    for i in range(len(p)):
        result.append(int(q[i])+int(p[i]))
    return result

def get_data(csv_file):
    papers = pd.read_csv(csv_file)
    data = {}
    # COUNT PAPERS PER YEAR
    # counter = 0
    # for index, each_paper in papers.iterrows():
    #     if data.get(each_paper['year']):
    #         data[each_paper['year']] += 1
    #     else:
    #         data[each_paper['year']] = 1
    #
    # years = list(dict(sorted(data.items())).keys())
    # amount_per_year = list(dict(sorted(data.items())).values())
    #
    # return [years, amount_per_year]

    for i in range(2006, 2023):
        data[i] = 0
        for index, each_paper in papers.iterrows():
            if each_paper['year'] == i:
                data[i] += 1
    return data.values()

papers_active = get_data('papers-categorized_active.csv')
print('active: ', papers_active)
papers_passive = get_data('papers-categorized_passive.csv')
print('\npassive: ', papers_passive)

fig, ax = plt.subplots()

x_axis = np.arange(17)

# Multi bar Chart
bar1 = ax.bar(x_axis -0.25, papers_passive, width=0.24, label = 'Privacy',color='#D98880', hatch='.', edgecolor='#7B241C',zorder=2)
bar2 = ax.bar(x_axis +0.0, papers_active, width=0.24, label = 'Integrity/Availability',color='#5499C7', hatch='///', edgecolor='#154360',zorder=2)
bar3 = ax.bar(x_axis +0.25, get_sum(list(papers_active), list(papers_passive)), width=0.24, label = 'Sum',color='#CACFD2', hatch='o', edgecolor='#797D7F',zorder=2)

# plt.bar_label(bar1)
# plt.bar_label(bar2)
# plt.bar_label(bar3)
# Xticks

plt.xticks(x_axis, [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])


plt.grid(axis='y', zorder=1, linestyle='-', color='#EAEDED')
plt.legend()
counter = 0
for spine in plt.gca().spines.values():
    if counter == 2 or counter == 0:
        spine.set_visible(True)
    else:
        spine.set_visible(False)
    counter += 1
# Display

plt.show()