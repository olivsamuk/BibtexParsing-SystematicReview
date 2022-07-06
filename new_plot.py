import numpy as np
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

X = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
Ygirls = [2,1,0,2,4,4,5]
Zboys = [2,4,6,15,18,15,9]

X_axis = np.arange(len(X))
bar_colors = ['mediumaquamarine', '#365841', '#ffeda0', '#43a2ca', '#a8ddb5']
plt.bar(X_axis - 0.2, Ygirls, 0.4, label='Passive Attacks', color=bar_colors[0],zorder=3)
plt.bar(X_axis + 0.2, Zboys, 0.4, label='Active Attacks', color=bar_colors[1],zorder=3)

plt.xticks(X_axis, X)
# plt.xlabel("Groups")
# plt.ylabel("Number of Students")
# plt.title("Number of Students in each group")
plt.grid(axis='y', zorder=0, linestyle='--')
plt.legend()
plt.show()