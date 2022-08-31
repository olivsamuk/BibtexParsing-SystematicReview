import matplotlib.pyplot as plt
import pandas as pd

font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)

plt.rc('font', size=18)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.rc('legend', fontsize=18)    # legend fontsize
plt.rc('figure', titlesize=18)  # fontsize of the figure title

# papers = pd.read_csv("papers-categorized.csv")
# data = {}
# # COUNT PAPERS PER YEAR
# counter = 0
# for index, each_paper in papers.iterrows():
#     if data.get(each_paper['year']):
#         data[each_paper['year']]+=1
#     else:
#         data[each_paper['year']] = 1
#
# years = list(dict(sorted(data.items())).keys())
# amount_per_year = list(dict(sorted(data.items())).values())

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

width = .8       # the width of the bars: can also be len(x) sequence



fig, ax = plt.subplots()

bars = ax.bar(papers.keys(), papers.values(), width, label='Artigos', zorder=2,color='#27AE60', edgecolor='#145A32')
ax.bar_label(bars)



plt.xticks(list(papers.keys()), rotation=45, ha='right')

plt.tick_params(
    axis='y',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom=False,  # ticks along the bottom edge are off
    top=False,  # ticks along the top edge are off
    labelbottom=False)  # labels along the bottom edge are off

plt.grid(axis='y', zorder=1, linestyle='-', color='#EAEDED')

counter = 0
for spine in plt.gca().spines.values():
    if counter == 2 or counter == 0:
        spine.set_visible(True)
    else:
        spine.set_visible(False)
    counter += 1


plt.show()