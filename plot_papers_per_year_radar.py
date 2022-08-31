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


categories = list(papers.keys())
categories = [*categories, categories[0]]

restaurant_1 = list(papers.values())

restaurant_1 = [*restaurant_1, restaurant_1[0]]


label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(restaurant_1))
print(label_loc)
plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.plot(label_loc, restaurant_1)

lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
plt.legend()
plt.show()