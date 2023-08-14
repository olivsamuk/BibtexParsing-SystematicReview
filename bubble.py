# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.patheffects as path_effects
#
#
# papers = pd.read_csv("papers-categorized-final.csv")
# data = {'verification':{}, 'enforcement':{}, 'attack model':{}, 'attack detection and mitigation':{}, 'supervisor synthesis':{}, 'diagnosability':{}, 'prognosability':{}, 'state estimation':{}, 'system recovery':{}}
# data2 = {'verification':{}, 'enforcement':{}, 'attack model':{}, 'attack detection and mitigation':{}, 'supervisor synthesis':{}, 'diagnosability':{}, 'prognosability':{}, 'state estimation':{}, 'system recovery':{}}
#
# for index, each_paper in papers.iterrows():
#         # if attack nests already exists
#         if data2.get(each_paper['problem']):
#             data2[each_paper['problem']][each_paper['attack']]['qtd'] += 1
#             # if each_paper['modeling'] already exists
#             if each_paper['modeling'] in data2[each_paper['problem']][each_paper['attack']]['formalisms'].keys():
#                 data2[each_paper['problem']][each_paper['attack']]['formalisms'][each_paper['modeling']] += 1
#             else:
#                 data2[each_paper['problem']][each_paper['attack']]['formalisms'].update({each_paper['modeling']: 1})
#
#         # creating attacks nest
#         else:
#             data2[each_paper['problem']] = {'passive':{'qtd':0,'formalisms':{}}, 'sensor': {'qtd':0,'formalisms':{}}, 'actuator':{'qtd':0,'formalisms':{}}, 'sensor-actuator':{'qtd':0,'formalisms':{}}, 'denial of service':{'qtd':0,'formalisms':{}}}
#             data2[each_paper['problem']][each_paper['attack']]['qtd'] +=1
#             data2[each_paper['problem']][each_paper['attack']]['formalisms'].update({each_paper['modeling']: 1})
#
# def getypos(s):
#     if s <= 2:
#         return s-.15
#     elif s > 2 and s <= 5:
#         return s-.3
#     elif s > 5 and s <=7:
#         return s-.5
#     elif s > 7 and s <=11:
#         return s-.6
#
#
# # for index, each_paper in papers.iterrows():
# #         if data.get(each_paper['problem']):
# #             data[each_paper['problem']][each_paper['attack']] += 1
# #         else:
# #             data[each_paper['problem']] = {'passive':0, 'sensor': 0, 'actuator':0, 'sensor-actuator':0, 'denial of service':0}
# #             data[each_paper['problem']][each_paper['attack']] += 1
#
# y_labels = ['Passive attacks', 'Sensor attacks', 'Actuator attacks', 'Sensor-actuator attacks', 'DoS attacks', 'finite-state automata', 'Labeled Transition System (LTS)', 'probabilistic finite-state automata', 'petri nets', 'Markov Models', 'Stochastic Petri nets', 'fuzzy automata', 'timed finite-state automata', 'finite-state transducer', 'signal interpreted Petri nets']
# x_labels = ['Verification of properties', 'Enforcement of properties', 'Attack synthesis', 'Attack detection', 'Supervisor synthesis', 'Fault diagnosis', 'Fault Prognosis', 'State estimation', 'System recovery']
# # y_cols = data2.keys()
# y_cols = ['passive', 'sensor', 'actuator', 'sensor-actuator', 'denial of service', 'finite-state automata', 'Labeled Transition System (LTS)', 'probabilistic finite-state automata', 'petri nets', 'Markov Models', 'Stochastic Petri nets', 'fuzzy automata', 'timed finite-state automata', 'finite-state transducer', 'signal interpreted Petri nets']
#
#
# colors = ['#4ddbb6', '#4ddbb6', '#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#4ddbb6', '#4ddbb6', '#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#4ddbb6', '#4ddbb6', '#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa']
# final_list = []
#
# for each_problem in data2.keys():
#     temp = []
#     # formalisms_temp = {'fsa': 0, 'pa': 0, 'ta': 0, 'fa': 0, 'mm': 0, 'lts': 0, 'fst': 0, 'sipn': 0, 'spn': 0, 'pn': 0}
#     formalisms_temp = {'fsa': 0, 'lts': 0, 'pa': 0, 'pn': 0, 'mm': 0, 'spn': 0, 'fa': 0, 'ta': 0, 'fst': 0, 'sipn': 0}
#     for each_attack in data2[each_problem].keys():
#         temp.append(data2[each_problem][each_attack]['qtd'])
#         for each_formalism in data2[each_problem][each_attack]['formalisms'].keys():
#             if each_formalism == 'finite-state automata':
#                 formalisms_temp['fsa']+= data2[each_problem][each_attack]['formalisms']['finite-state automata']
#             elif each_formalism == 'Labeled Transition System (LTS)':
#                 formalisms_temp['lts']+= data2[each_problem][each_attack]['formalisms']['Labeled Transition System (LTS)']
#             elif each_formalism == 'probabilistic finite-state automata':
#                 formalisms_temp['pa']+= data2[each_problem][each_attack]['formalisms']['probabilistic finite-state automata']
#             elif each_formalism == 'petri nets':
#                 formalisms_temp['pn']+= data2[each_problem][each_attack]['formalisms']['petri nets']
#             elif each_formalism == 'Hidden Markov Model (HMM)':
#                 formalisms_temp['mm']+= data2[each_problem][each_attack]['formalisms']['Hidden Markov Model (HMM)']
#             elif each_formalism == 'Markov Decision Process (MDP)':
#                 formalisms_temp['mm'] += data2[each_problem][each_attack]['formalisms']['Markov Decision Process (MDP)']
#             elif each_formalism == 'Stochastic Petri nets':
#                 formalisms_temp['spn']+= data2[each_problem][each_attack]['formalisms']['Stochastic Petri nets']
#             elif each_formalism == 'fuzzy automata':
#                 formalisms_temp['fa']+= data2[each_problem][each_attack]['formalisms']['fuzzy automata']
#             elif each_formalism == 'timed finite-state automata':
#                 formalisms_temp['ta']+= data2[each_problem][each_attack]['formalisms']['timed finite-state automata']
#             elif each_formalism == 'finite-state transducer':
#                 formalisms_temp['fst']+= data2[each_problem][each_attack]['formalisms']['finite-state transducer']
#             elif each_formalism == 'signal interpreted Petri nets':
#                 formalisms_temp['sipn']+= data2[each_problem][each_attack]['formalisms']['signal interpreted Petri nets']
#
#     for i in list(formalisms_temp.values()):
#         temp.append(i)
#     final_list.append(temp)
#
# print(final_list)
# print(list(zip(*final_list)))
# df = pd.DataFrame(final_list, columns=y_cols, index=list(data2.keys()))
# df = df.transpose()
# dfu = df.unstack().reset_index()
# dfu.columns = list("XYS")
# dfu_orig = dfu.copy()
#
#
# dfu["S"] *= 40
#
# print(dfu)
#
# plt.scatter(x="X", y="Y", s="S", data=dfu, zorder=3, alpha=.8)
# papers_count = 0
# for each_line in range(len(dfu_orig)):
#     a = dfu_orig.iloc[each_line]
#     if a["S"] > 0:
#         papers_count+=a["S"]
#         plt.annotate(str(a["S"]), (a["X"], a["Y"]), ha='center', va="center", color='white')
#
# # for each_line in range(len(dfu_orig)):
# #     a = dfu_orig.iloc[each_line]
# #     b = dfu.iloc[each_line]
# #     if a["S"] > 0:
# #         temp = (a["S"] / papers_count) * 100
# #         plt.annotate(str(round(temp,1)) + '%',(list(data2).index(a["X"]), getypos(y_cols.index(a["Y"]))), ha='left', va='baseline',size=10)
#
#
#
# plt.xticks(list(data2.keys()), x_labels, rotation=30, ha='right')
# plt.yticks(y_cols, y_labels)
#
#
# plt.margins(.2)
# plt.grid(color='#cccccc', linestyle='--', linewidth=1, zorder=0)
#
#
# plt.gca().spines['right'].set_visible(False)
# plt.gca().spines['top'].set_visible(False)
# # plt.text(6, 1-.3, 'teste', fontsize=10)
#
# plt.show()








import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects


papers = pd.read_csv("papers-categorized-final.csv")
data = {'verification':{}, 'enforcement':{}, 'attack model':{}, 'attack detection and mitigation':{}, 'supervisor synthesis':{}, 'diagnosability':{}, 'prognosability':{}, 'state estimation':{}, 'system recovery':{}}
data2 = {'verification':{}, 'enforcement':{}, 'attack model':{}, 'attack detection and mitigation':{}, 'supervisor synthesis':{}, 'diagnosability':{}, 'prognosability':{}, 'state estimation':{}, 'system recovery':{}}

for index, each_paper in papers.iterrows():
        # if attack nests already exists
        if data2.get(each_paper['problem']):
            data2[each_paper['problem']][each_paper['attack']]['qtd'] += 1
            # if each_paper['modeling'] already exists
            if each_paper['modeling'] in data2[each_paper['problem']][each_paper['attack']]['formalisms'].keys():
                data2[each_paper['problem']][each_paper['attack']]['formalisms'][each_paper['modeling']] += 1
            else:
                data2[each_paper['problem']][each_paper['attack']]['formalisms'].update({each_paper['modeling']: 1})

        # creating attacks nest
        else:
            data2[each_paper['problem']] = {'passive':{'qtd':0,'formalisms':{}}, 'sensor': {'qtd':0,'formalisms':{}}, 'actuator':{'qtd':0,'formalisms':{}}, 'sensor-actuator':{'qtd':0,'formalisms':{}}, 'denial of service':{'qtd':0,'formalisms':{}}}
            data2[each_paper['problem']][each_paper['attack']]['qtd'] +=1
            data2[each_paper['problem']][each_paper['attack']]['formalisms'].update({each_paper['modeling']: 1})

def getypos(s):
    if s <= 2:
        return s-.15
    elif s > 2 and s <= 5:
        return s-.3
    elif s > 5 and s <=7:
        return s-.5
    elif s > 7 and s <=11:
        return s-.6


# for index, each_paper in papers.iterrows():
#         if data.get(each_paper['problem']):
#             data[each_paper['problem']][each_paper['attack']] += 1
#         else:
#             data[each_paper['problem']] = {'passive':0, 'sensor': 0, 'actuator':0, 'sensor-actuator':0, 'denial of service':0}
#             data[each_paper['problem']][each_paper['attack']] += 1

x_labels = ['Passive attacks', 'Sensor attacks', 'Actuator attacks', 'Sensor-actuator attacks', 'DoS attacks', 'finite-state automata', 'Labeled Transition System (LTS)', 'probabilistic finite-state automata', 'petri nets', 'Markov Models', 'Stochastic Petri nets', 'fuzzy automata', 'timed finite-state automata', 'finite-state transducer', 'signal interpreted Petri nets']
x_cols = ['passive', 'sensor', 'actuator', 'sensor-actuator', 'denial of service', 'finite-state automata', 'Labeled Transition System (LTS)', 'probabilistic finite-state automata', 'petri nets', 'Markov Models', 'Stochastic Petri nets', 'fuzzy automata', 'timed finite-state automata', 'finite-state transducer', 'signal interpreted Petri nets']

y_labels = ['Verification of properties', 'Enforcement of properties', 'Attack synthesis', 'Attack detection', 'Supervisor synthesis', 'Fault diagnosis', 'Fault Prognosis', 'State estimation', 'System recovery']
y_cols = list(data2.keys())

colors = ['#4ddbb6', '#4ddbb6', '#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#4ddbb6', '#4ddbb6', '#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#4ddbb6', '#4ddbb6', '#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#4ddbb6','#4ddbb6', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa', '#636efa']
final_list = []

for each_problem in data2.keys():
    temp = []
    # formalisms_temp = {'fsa': 0, 'pa': 0, 'ta': 0, 'fa': 0, 'mm': 0, 'lts': 0, 'fst': 0, 'sipn': 0, 'spn': 0, 'pn': 0}
    formalisms_temp = {'fsa': 0, 'lts': 0, 'pa': 0, 'pn': 0, 'mm': 0, 'spn': 0, 'fa': 0, 'ta': 0, 'fst': 0, 'sipn': 0}
    for each_attack in data2[each_problem].keys():
        temp.append(data2[each_problem][each_attack]['qtd'])
        for each_formalism in data2[each_problem][each_attack]['formalisms'].keys():
            if each_formalism == 'finite-state automata':
                formalisms_temp['fsa']+= data2[each_problem][each_attack]['formalisms']['finite-state automata']
            elif each_formalism == 'Labeled Transition System (LTS)':
                formalisms_temp['lts']+= data2[each_problem][each_attack]['formalisms']['Labeled Transition System (LTS)']
            elif each_formalism == 'probabilistic finite-state automata':
                formalisms_temp['pa']+= data2[each_problem][each_attack]['formalisms']['probabilistic finite-state automata']
            elif each_formalism == 'petri nets':
                formalisms_temp['pn']+= data2[each_problem][each_attack]['formalisms']['petri nets']
            elif each_formalism == 'Hidden Markov Model (HMM)':
                formalisms_temp['mm']+= data2[each_problem][each_attack]['formalisms']['Hidden Markov Model (HMM)']
            elif each_formalism == 'Markov Decision Process (MDP)':
                formalisms_temp['mm'] += data2[each_problem][each_attack]['formalisms']['Markov Decision Process (MDP)']
            elif each_formalism == 'Stochastic Petri nets':
                formalisms_temp['spn']+= data2[each_problem][each_attack]['formalisms']['Stochastic Petri nets']
            elif each_formalism == 'fuzzy automata':
                formalisms_temp['fa']+= data2[each_problem][each_attack]['formalisms']['fuzzy automata']
            elif each_formalism == 'timed finite-state automata':
                formalisms_temp['ta']+= data2[each_problem][each_attack]['formalisms']['timed finite-state automata']
            elif each_formalism == 'finite-state transducer':
                formalisms_temp['fst']+= data2[each_problem][each_attack]['formalisms']['finite-state transducer']
            elif each_formalism == 'signal interpreted Petri nets':
                formalisms_temp['sipn']+= data2[each_problem][each_attack]['formalisms']['signal interpreted Petri nets']

    for i in list(formalisms_temp.values()):
        temp.append(i)
    final_list.append(temp)


print(final_list)


def TotalByAttackAndFormalism(multilist):
    result = []
    for each_item in multilist:
        result.append(sum(each_item))
    return(result)

print(TotalByAttackAndFormalism(list(zip(*final_list))))


df = pd.DataFrame(list(zip(*final_list)), columns=y_cols, index=x_cols)
df = df.transpose()
dfu = df.unstack().reset_index()
dfu.columns = list("XYS")
dfu_orig = dfu.copy()


dfu["S"] *= 40

# print(dfu)

plt.scatter(x="X", y="Y", s="S", data=dfu, zorder=3, alpha=.8)
papers_count = 0
for each_line in range(len(dfu_orig)):
    a = dfu_orig.iloc[each_line]
    if a["S"] > 0:
        papers_count+=a["S"]
        plt.annotate(str(a["S"]), (a["X"], a["Y"]), ha='center', va="center", color='white')

# for each_line in range(len(dfu_orig)):
#     a = dfu_orig.iloc[each_line]
#     b = dfu.iloc[each_line]
#     if a["S"] > 0:
#         temp = (a["S"] / papers_count) * 100
#         plt.annotate(str(round(temp,1)) + '%',(list(data2).index(a["X"]), getypos(y_cols.index(a["Y"]))), ha='left', va='baseline',size=10)


plt.xticks(x_cols, x_labels, rotation=30, ha='right')
plt.yticks(y_cols, y_labels)

# plt.gca().invert_xaxis()


plt.margins(.2)
plt.grid(color='#cccccc', linestyle='--', linewidth=1, zorder=0)


plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
# plt.text(6, 1-.3, 'teste', fontsize=10)

# plt.show()