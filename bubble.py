import pandas as pd
import matplotlib.pyplot as plt



papers = pd.read_csv("papers-categorized-new.csv")
data = {}
# COUNT PAPERS PER YEAR

for index, each_paper in papers.iterrows():

        if data.get(each_paper['problem']):
            if each_paper['attack'] in data[each_paper['problem']].keys():
                data[each_paper['problem']][each_paper['attack']]+=1
            else:
                data[each_paper['problem']].update({each_paper['attack']: 1})
        else:
            data[each_paper['problem']] = {each_paper['attack']: 1}

print(data)

x = [1, 2, 3, 4, 5, 6]
y = [1, 5, 3, 5, 7, 8]

plt.plot(x, y)
plt.show()