from matplotlib import pyplot as plt
import pandas as pd
from upsetplot import plot, from_indicators, generate_counts, from_memberships, UpSet
font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)

# plt.rc('font', size=18)          # controls default text sizes
# plt.rc('axes', titlesize=18)     # fontsize of the axes title
# plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
# plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
# plt.rc('legend', fontsize=18)    # legend fontsize
# plt.rc('figure', titlesize=18)  # fontsize of the figure title

movies = pd.read_csv("papers.csv")
movies_by_genre = from_memberships(movies.bases.str.split('-'), data=movies)

UpSet(movies_by_genre, show_counts=True, facecolor='#365841', shading_color='#efefef').plot()
plt.show()