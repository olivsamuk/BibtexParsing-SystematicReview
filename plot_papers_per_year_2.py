# Import Library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline



font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)
#
plt.rc('font', size=28)          # controls default text sizes
plt.rc('axes', titlesize=28)     # fontsize of the axes title
plt.rc('axes', labelsize=28)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=28)    # fontsize of the tick labels
plt.rc('ytick', labelsize=28)    # fontsize of the tick labels
plt.rc('legend', fontsize=28)    # legend fontsize
plt.rc('figure', titlesize=28)  # fontsize of the figure title

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

    for i in range(2005, 2024):
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

x_axis = np.arange(19)

# Multi bar Chart
bar1 = ax.bar(x_axis -0.25, papers_passive, width=0.20, label = 'Passive attacks',color='#4ddbb6', edgecolor='#2e836d',zorder=2)
bar2 = ax.bar(x_axis +0.0, papers_active, width=0.20, label = 'Active Attacks',color='#636efa', edgecolor='#31367c',zorder=2)
bar3 = ax.bar(x_axis +0.25, get_sum(list(papers_active), list(papers_passive)), width=0.20, label = 'Total',color='#D5D8DC', edgecolor='#717D7E',zorder=2)
print(len(get_sum(list(papers_active), list(papers_passive))))
# plt.bar_label(bar1)
# plt.bar_label(bar2)
# plt.bar_label(bar3)
# Xticks
x = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
plt.xticks(x_axis, x)
plt.yticks(np.arange(0, 50, 2.0))

total_sum = get_sum(list(papers_active), list(papers_passive))
# lin = np.linspace(total_sum[0],total_sum[-1], len(total_sum))
# plt.plot(lin, color='black', linewidth=.5)


y = np.array(total_sum)


#calculate equation for quadratic trendline
z = np.polyfit(x_axis, y, 2)
p = np.poly1d(z)
# plt.plot(x_axis, p(x_axis))

X_Y_Spline = make_interp_spline(x_axis, p(x_axis))
X_ = np.linspace(x_axis.min(), x_axis.max(), 500)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_+.8, color='#717D7E', linewidth='.7')

plt.grid(zorder=1, linestyle='-', color='#EAEDED')
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