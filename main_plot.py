import matplotlib.pyplot as plt
import pandas as pd

papers = pd.read_csv("papers.csv")
data = {}
# COUNT PAPERS PER YEAR
counter = 0
for index, each_paper in papers.iterrows():
    if data.get(each_paper['year']):
        data[each_paper['year']]+=1
    else:
        data[each_paper['year']] = 1

years = list(dict(sorted(data.items())).keys())
amount_per_year = list(dict(sorted(data.items())).values())

print(years, amount_per_year)

width = .8       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(years, amount_per_year, width, label='Men')
# ax.bar(years, women_means, width, bottom=men_means, label='Women')


plt.xticks(years)

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()