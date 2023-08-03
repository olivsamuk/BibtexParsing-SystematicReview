import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects


papers = pd.read_csv("papers-categorized-final.csv")
data = {'verification':{}, 'enforcement':{}, 'attack model':{}, 'attack detection and mitigation':{}, 'supervisor synthesis':{}, 'diagnosability':{}, 'state estimation':{}, 'system recovery':{}, 'testbed':{}}

def getypos(s):
    if s <= 2:
        return s-.15
    elif s > 2 and s <= 5:
        return s-.3
    elif s > 5 and s <=7:
        return s-.5
    elif s > 7 and s <=11:
        return s-.6


for index, each_paper in papers.iterrows():
        if data.get(each_paper['problem']):
            data[each_paper['problem']][each_paper['attack']] += 1
        else:
            data[each_paper['problem']] = {'passive':0, 'sensor': 0, 'actuator':0, 'sensor-actuator':0, 'denial of service':0}
            data[each_paper['problem']][each_paper['attack']] += 1

y_labels = ['Passive attacks', 'Sensor attacks', 'Actuator attacks', 'Sensor-actuator attacks', 'DoS attacks']
x_labels = ['Verification of properties', 'Enforcement of properties', 'Attack synthesis', 'Attack detection', 'Supervisor synthesis', 'Fault diagnosis', 'Fault Prognosis', 'State estimation', 'System recovery']
y_cols = ['passive', 'sensor', 'actuator', 'sensor-actuator', 'denial of service']

colors = ['#4ddbb6', '#4ddbb6', '#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa']

final_list = []
for each_problem in data.keys():
   final_list.append(list(data[each_problem].values()))


df = pd.DataFrame(final_list, columns=y_cols, index=list(data.keys()))
df = df.transpose()
dfu = df.unstack().reset_index()
dfu.columns = list("XYS")
dfu_orig = dfu.copy()


dfu["S"] *= 50

plt.scatter(x="X", y="Y", s="S", data=dfu, c=colors, zorder=3, alpha=.8)
papers_count = 0
for each_line in range(len(dfu_orig)):
    a = dfu_orig.iloc[each_line]
    if a["S"] > 0:
        papers_count+=a["S"]
        plt.annotate(str(a["S"]), (a["X"], a["Y"]), ha='center', va="center", color='white')
print(papers_count)
for each_line in range(len(dfu_orig)):
    a = dfu_orig.iloc[each_line]
    b = dfu.iloc[each_line]
    if a["S"] > 0:
# <<<<<<< HEAD
        # num = float(a["S"] / papers_count)


        num = float((a["S"]/papers_count)*100)
        # print(round(num,2))
        plt.annotate(str(round(num,1)) + '%',
# =======
#         temp = (a["S"] / papers_count) * 100
#         # plt.annotate(str((a["S"]*papers_count)/100)+'%', (list(data).index(a["X"]), y_cols.index(a["Y"])-(b["S"]/100000)), ha='left', va='baseline', size=10)
#         plt.annotate(str(round(temp,1)) + '%',
# >>>>>>> 16172451eabb5e3f07247d5a61ca997249bf94eb
                     (list(data).index(a["X"]), getypos(y_cols.index(a["Y"]))), ha='left', va='baseline',
                     size=10)


plt.xticks(list(data.keys()), x_labels, rotation=30, ha='right')
plt.yticks(y_cols, y_labels)
plt.margins(.2)
plt.grid(color='#cccccc', linestyle='--', linewidth=1, zorder=0)


plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.text(6, 1-.3, 'teste', fontsize=10)

plt.show()