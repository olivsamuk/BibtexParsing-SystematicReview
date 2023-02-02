import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)

plt.rc('font', size=18)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.rc('legend', fontsize=18)    # legend fontsize
plt.rc('figure', titlesize=18)  # fontsize of the figure title

papers = pd.read_csv("papers-categorized-new.csv")
data = {}
# COUNT PAPERS PER YEAR

for index, each_paper in papers.iterrows():

        # if data.get(each_paper['problem']):
        #     if each_paper['attack'] in data[each_paper['problem']].keys():
        #         data[each_paper['problem']][each_paper['attack']]+=1
        #     else:
        #         data[each_paper['problem']].update({each_paper['attack']: 1})
        # else:
        #     data[each_paper['problem']] = {each_paper['attack']: 1}

        if data.get(each_paper['problem']):
            data[each_paper['problem']][each_paper['attack']] += 1
        else:
            data[each_paper['problem']] = {'passive':0, 'sensor': 0, 'actuator':0, 'sensor-actuator':0, 'denail of service':0}
            data[each_paper['problem']][each_paper['attack']] += 1



final_list = []
for each_problem in data.keys():
   final_list.append(list(data[each_problem].values()))

print(data.keys())

# d1 = {'col1': [1, 2], 'col2': [3, 4]}


# df = pd.DataFrame([[300,500,700],[200,400,600],[150,150,150]], columns=['x1', 'x2', 'x3'], index=['y1', 'y2', 'y3'])
df = pd.DataFrame(final_list, columns=['passive', 'sensor', 'actuator', 'sensor-actuator', 'denail of service'], index=list(data.keys()))
df = df.transpose()
dfu = df.unstack().reset_index()
dfu.columns = list("XYS")
print(dfu['X'])

dfu["S"] *= 100
plt.scatter(x="X", y="Y", s="S", data=dfu)



plt.xticks(rotation='vertical')
plt.margins(.2)
plt.show()