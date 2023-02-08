import matplotlib.pyplot as plt
import pandas as pd
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

def change_names(values):
    new_values = []
    for i in values:
        if i == 'attack detection and mitigation':
            if 'Attack detection and mitigation' not in new_values:
                new_values.append('Attack detection and mitigation')
        elif i == 'verification':
            if 'Formalization and verification of properties' not in new_values:
                new_values.append('Formalization and verification of properties')
        elif i == 'enforcement':
            if 'Enforcement of properties' not in new_values:
                new_values.append('Enforcement of properties')
        elif i == 'attack model':
            if 'Attack synthesis' not in new_values:
                new_values.append('Attack synthesis')
        elif i == 'supervisor synthesis':
            if 'Supervisor synthesis' not in new_values:
                new_values.append('Supervisor synthesis')
        elif i == 'diagnosability':
            if 'Diagnosability' not in new_values:
                new_values.append('Diagnosability')
        elif i == 'state estimation':
            if 'State estimation' not in new_values:
                new_values.append('State estimation')
        elif i == 'system recovery':
            if 'System recovery' not in new_values:
                new_values.append('System recovery')
    return new_values

def get_data(csv_file):
    papers = pd.read_csv(csv_file)
    data = {}
    for index, each_paper in papers.iterrows():
        if data.get(each_paper['problem']):
            data[each_paper['problem']] += 1
        else:
            data[each_paper['problem']] = 1
    return data

papers = get_data('papers-categorized-new.csv')

names = change_names(list(papers.keys()))
print(papers)
amount = list(papers.values())

strategies_grouped          = [papers['verification']+papers['enforcement'], papers['attack model'], papers['attack detection and mitigation']+papers['supervisor synthesis']+papers['system recovery'], papers['diagnosability'], papers['state estimation']]
strategies_grouped_label    = ['Protection of secrets', 'Attack synthesis', 'Attack-tolerant control', 'Fault diagnosis', 'State estimation']
strategies_ungrouped        = [papers['verification'],papers['enforcement'], papers['attack model'], papers['attack detection and mitigation'],papers['supervisor synthesis'],papers['system recovery'], papers['diagnosability'], papers['state estimation']]
strategies_ungrouped_label  = ['Verification', 'Enforcement', 'Attack synthesis', 'Attack detection', 'Supervisor synthesis', 'System recovery', 'Fault diagnosis', 'State estimation']

fig, ax = plt.subplots()
size = 0.3

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(p=pct,v=val)
    return my_autopct


ax.pie(strategies_ungrouped,
       # labels=strategies_ungrouped_label,
        colors=['#4ddbb6', '#4ddbb6', '#FFFFFF', '#929afc', '#929afc', '#929afc','#FFFFFF', '#FFFFFF'],
        # autopct=make_autopct(strategies_ungrouped),
        pctdistance=0.8,
        radius=1, wedgeprops=dict(width=size, edgecolor='w', linewidth=2))


ax.pie(strategies_grouped,
       # labels=strategies_grouped_label,
       colors=['#4dbbb6', '#4047a3', '#636efa', '#9763fa', '#fa63ee'],
       # autopct=make_autopct(strategies_grouped),
       pctdistance=.7,<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   version="1.1"
   id="svg185066"
   width="39.573299"
   height="24.901339"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs185070" />
  <sodipodi:namedview
     id="namedview185068"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageshadow="2"
     inkscape:pageopacity="0.0"
     inkscape:pagecheckerboard="0" />
  <inkscape:clipboard
     style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:37.33334173px;line-height:1.25;font-family:'Latin Modern Roman';-inkscape-font-specification:'Latin Modern Roman, Normal';font-variant-ligatures:normal;font-variant-position:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-alternates:normal;font-variant-east-asian:normal;font-feature-settings:normal;font-variation-settings:normal;text-indent:0;text-align:start;text-decoration-line:none;text-decoration-style:solid;text-decoration-color:#000000;letter-spacing:normal;word-spacing:normal;text-transform:none;writing-mode:lr-tb;direction:ltr;text-orientation:mixed;dominant-baseline:auto;baseline-shift:baseline;white-space:normal;opacity:1;vector-effect:none;fill:#ffffff;fill-opacity:1;stroke-width:0.99999874;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;-inkscape-stroke:none;stop-color:#000000;stop-opacity:1"
     min="-187.30959,529.95841"
     max="-147.73629,554.85975"
     geom-min="-187.30959,529.95841"
     geom-max="-147.73629,554.85975" />
  <g
     id="g185072"
     transform="matrix(3.7795276,0,0,3.7795276,349.75301,-567.58885)">
    <text
       xml:space="preserve"
       style="font-size:9.87778px;line-height:1.25;font-family:'Latin Modern Roman';-inkscape-font-specification:'Latin Modern Roman, Normal';stroke-width:0.264583;stroke-linecap:butt;stroke-linejoin:round"
       x="-92.854904"
       y="156.65437"
       id="text156265-1"><tspan
         sodipodi:role="line"
         id="tspan156263-5"
         style="font-weight:bold;font-size:9.87778px;fill:#ffffff;stroke-width:0.264583"
         x="-92.854904"
         y="156.65437">45</tspan></text>
  </g>
</svg>

       radius=1-size, wedgeprops=dict(width=size, edgecolor='w', linewidth=2))
# plt.title('Population')
plt.show()