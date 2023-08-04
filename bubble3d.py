import plotly.graph_objects as go
import pandas as pd

distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
density = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638, 2095]
gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
planet_diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]

# -----
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


y_labels = ['Passive attacks', 'Sensor attacks', 'Actuator attacks', 'Sensor-actuator attacks', 'DoS attacks']
x_labels = ['Verification of properties', 'Enforcement of properties', 'Attack synthesis', 'Attack detection', 'Supervisor synthesis', 'Fault diagnosis', 'Fault Prognosis', 'State estimation', 'System recovery']
y_cols = ['passive', 'sensor', 'actuator', 'sensor-actuator', 'denial of service']

a,b,c,d=[],[],[],[]

for each_problem in data2.keys():
    for each_attack in y_cols:
        for each_modeling in data2[each_problem][each_attack]['formalisms'].keys():
            a.append(each_problem)
            b.append(each_attack)
            c.append(each_modeling)

            if each_problem == 'verification' or each_problem == 'enforcement':
                d.append(data2[each_problem][each_attack]['formalisms'][each_modeling])
            else:
                d.append(data2[each_problem][each_attack]['formalisms'][each_modeling]*5)
print(a,b,c,d)

# Create trace, sizing bubbles by planet diameter
fig = go.Figure(data=go.Scatter3d(
    x = a,
    y = c,
    z = b,
    # text = planets,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 0, # info on sizeref: https://plotly.com/python/reference/scatter/#scatter-marker-sizeref
        size = d
        )
))

fig.update_layout(width=1000, height=800, title = 'Cybersecurity Strategies',
                  scene = dict(xaxis=dict(title='Distance from Sun', titlefont_color='black'),
                               yaxis=dict(title='Density', titlefont_color='black'),
                               zaxis=dict(title='Gravity', titlefont_color='black')
                               # bgcolor = 'rgb(20, 24, 54)'
                           ))

fig.show()