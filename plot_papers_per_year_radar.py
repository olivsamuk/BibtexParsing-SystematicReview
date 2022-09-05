# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.interpolate import make_interp_spline, BSpline
#
# font = {'family' : 'Latin Modern Roman'}
# plt.rc('font', **font)
#
# plt.rc('font', size=18)          # controls default text sizes
# plt.rc('axes', titlesize=18)     # fontsize of the axes title
# plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
# plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
# plt.rc('legend', fontsize=18)    # legend fontsize
# plt.rc('figure', titlesize=18)  # fontsize of the figure title
#
# def get_data(csv_file, period):
#     papers = pd.read_csv(csv_file)
#     data = {'attack model': 0, 'attack detection and mitigation': 0, 'diagnosabilty': 0, 'state estimation': 0, 'supervisor synthesis': 0, 'system recovery': 0}
#     for index, each_paper in papers.iterrows():
#         if period == 1:
#             if each_paper['year'] >= 2006 and each_paper['year'] <= 2016:
#                 data[each_paper['problem']] += 1
#         elif period == 2:
#             if each_paper['year'] >= 2017 and each_paper['year'] <= 2020:
#                 data[each_paper['problem']] += 1
#         elif period == 3:
#             if each_paper['year'] >= 2021:
#                 print(each_paper['title'])
#                 data[each_paper['problem']] += 1
#
#     return data
#
# papers_p1 = get_data('papers-categorized_active.csv',1)
# papers_p2 = get_data('papers-categorized_active.csv',2)
# papers_p3 = get_data('papers-categorized_active.csv',3)
#
#
# # categories = list(papers.keys())
# categories = ['attack detection and mitigation', 'attack model', 'supervisor synthesis', 'diagnosabilty', 'state estimation', 'system recovery']
# categories = [*categories, categories[0]]
#
# restaurant_1 = list(papers_p1.values())
# restaurant_1 = [*restaurant_1, restaurant_1[0]]
#
# restaurant_2 = list(papers_p2.values())
# restaurant_2 = [*restaurant_2, restaurant_2[0]]
#
# restaurant_3 = list(papers_p3.values())
# restaurant_3 = [*restaurant_3, restaurant_3[0]]
#
# label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(restaurant_1))
#
#
# plt.figure(figsize=(8, 8))
# plt.subplot(polar=True)
# plt.plot(label_loc, restaurant_1, linewidth=1, linestyle='solid', color='#797D7F', label='2006-2016')
# plt.fill(label_loc, restaurant_1, '#797D7F', alpha=.1, zorder=5)
# plt.plot(label_loc, restaurant_2, linewidth=1, linestyle='solid', color='#154360', label='2017-2020')
# plt.fill(label_loc, restaurant_2, '#154360', alpha=.1, zorder=1)
# plt.plot(label_loc, restaurant_3,linewidth=1, linestyle='solid', color='#7B241C', label='2021-2022')
# plt.fill(label_loc, restaurant_3, '#7B241C', alpha=.1, zorder=0)
#
# lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
# plt.legend()
# plt.show()
#
# =================  PLOT.LY


import plotly.graph_objects as go
import plotly.offline as pyo

def get_data(csv_file, period):
    papers = pd.read_csv(csv_file)
    data = {'attack model': 0, 'attack detection and mitigation': 0, 'diagnosabilty': 0, 'state estimation': 0, 'supervisor synthesis': 0, 'system recovery': 0, 'verification':0, 'enforcement':0}
    for index, each_paper in papers.iterrows():
        if period == 1:
            if each_paper['year'] >= 2006 and each_paper['year'] <= 2016:
                data[each_paper['problem']] += 1
        elif period == 2:
            if each_paper['year'] >= 2017 and each_paper['year'] <= 2020:
                data[each_paper['problem']] += 1
        elif period == 3:
            if each_paper['year'] >= 2021:
                print(each_paper['title'])
                data[each_paper['problem']] += 1

    return data

papers_p1 = get_data('papers-categorized-new.csv',1)
papers_p2 = get_data('papers-categorized-new.csv',2)
papers_p3 = get_data('papers-categorized-new.csv',3)
print(papers_p3)

categories = ['attack model', 'attack detection and mitigation', 'diagnosabilty', 'state estimation',  'supervisor synthesis', 'system recovery', 'verification', 'enforcement']
categories = [*categories, categories[0]]

restaurant_1 = list(papers_p1.values())
restaurant_1 = [*restaurant_1, restaurant_1[0]]

restaurant_2 = list(papers_p2.values())
restaurant_2 = [*restaurant_2, restaurant_2[0]]

restaurant_3 = list(papers_p3.values())
restaurant_3 = [*restaurant_3, restaurant_3[0]]



fig = go.Figure(
    data=[
        go.Scatterpolar(r=restaurant_1, theta=categories, fill='toself', name='Restaurant 1'),
        go.Scatterpolar(r=restaurant_2, theta=categories, fill='toself', name='Restaurant 2'),
        go.Scatterpolar(r=restaurant_3, theta=categories, fill='toself', name='Restaurant 3')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Restaurant comparison'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

pyo.plot(fig)
fig.write_image("fig1.pdf")
