from matplotlib import pyplot as plt
import pandas as pd
from upsetplot import plot, from_indicators, generate_counts, from_memberships, UpSet
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)


# movies = pd.read_csv("final_list_papers_categorized.csv")
# movies_by_genre = from_memberships(movies.bases.str.split('-'), data=movies)
#
# UpSet(movies_by_genre, show_counts=True, facecolor='#365841', shading_color='#efefef').plot()
# plt.show()

papers = pd.read_csv("papers-categorized-final.csv")

for index, each_paper in papers.iterrows():
    for index2, each_paper2 in papers.iterrows():
        if index != index2:
            # print(index, index2)
            if similar(each_paper['title'],each_paper2['title']) > .9:
                print('Paper 1: ', each_paper['title'], '\n Paper2: ', each_paper2['title'], '\n Similarity: ',
                    similar(each_paper['title'],each_paper2['title']))