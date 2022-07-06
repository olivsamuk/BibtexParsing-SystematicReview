import pandas
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)

plt.rc('font', size=18)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.rc('legend', fontsize=18)    # legend fontsize
plt.rc('figure', titlesize=18)  # fontsize of the figure title



data = pandas.read_csv('test.csv')
# print(data)

qtd_pa = {'2014':0, '2015':0, '2016':0, '2017':0, '2018':0, '2019':0, '2020':0, '2021':0, '2022':0}
qtd_ga = {'2014':0, '2015':0, '2016':0, '2017':0, '2018':0, '2019':0, '2020':0, '2021':0, '2022':0}
qtd_sa = {'2014':0, '2015':0, '2016':0, '2017':0, '2018':0, '2019':0, '2020':0, '2021':0, '2022':0}
qtd_aa = {'2014':0, '2015':0, '2016':0, '2017':0, '2018':0, '2019':0, '2020':0, '2021':0, '2022':0}
qtd_saa = {'2014':0, '2015':0, '2016':0, '2017':0, '2018':0, '2019':0, '2020':0, '2021':0, '2022':0}
for each_row in data.values.tolist():
    if each_row[4] != '-' or each_row[4] == 'review':
        if each_row[4] == 'passive attacks':
            qtd_pa[str(each_row[2])]+=1
        elif each_row[4] == 'general attacks':
            qtd_ga[str(each_row[2])] += 1
        elif each_row[4] == 'sensor attacks ':
            qtd_sa[str(each_row[2])] += 1
        elif each_row[4] == 'actuator attacks':
            qtd_aa[str(each_row[2])] += 1
        elif each_row[4] == 'sensor-actuator attacks':
            qtd_saa[str(each_row[2])] += 1

final = [['2014'],
         ['2015'],
         ['2016'],
         ['2017'],
         ['2018'],
         ['2019'],
         ['2020'],
         ['2021'],
         ['2022']]
for each_dict in [qtd_pa, qtd_ga, qtd_sa, qtd_aa, qtd_saa]:
    for each_row in range(len(list(each_dict.values()))):
        final[each_row].append(list(each_dict.values())[each_row])



print('Passive attacks: ', qtd_pa, '\n General Attacks: ', qtd_ga, '\n Sensor attacks: ', qtd_sa, '\n Actuator attacks: ', qtd_aa, '\n Sensor and Actuator attacks: ', qtd_saa)
# print(sum(qtd_pa.values()))
# print(sum(qtd_ga.values()))
# print(sum(qtd_sa.values()))
# print(sum(qtd_aa.values()))
# print(sum(qtd_saa.values()))
#
print(final)
# print('Total: ', sum(qtd_pa.values())+sum(qtd_ga.values())+sum(qtd_sa.values())+sum(qtd_aa.values())+sum(qtd_saa.values()))


df = pandas.DataFrame(final)
#df.rename(columns = {0:"mes", 1: "Temp. media mes", 2: "Temp. máxima media", 3: "Temp. mínima media", 4: "Media lluvias mensual", 5:"Humedad media rel"}, inplace = True)
df.rename(columns = {0:"Year", 1: "Passive attacks", 2: "General attacks", 3: "Sensor attacks", 4: "Actuator attacks", 5:"Sensor-actuator attacks"}, inplace = True)

# Setting the positions and width for the bars
pos = list(range(len(df)))
num_col = len(df.columns) - 1
width = 0.95 / num_col

fig, ax = plt.subplots(figsize=(16,10))

bar_colors = ['#feb24c', '#f03b20', '#ffeda0', '#43a2ca', '#a8ddb5']
bar_labels = df.columns[1:]

for i, (colname, color, lbl) in enumerate(zip(df.columns[1:], bar_colors, bar_labels)):
    delta_p = 0.125 + width*i
    plt.bar([p + delta_p for p in pos],
            df[colname], width, color=color, label=lbl)
    # for j in range(len(df)):
    #     ax.annotate(df[colname][j],
    #                 xy=(pos[j] + delta_p, df[colname][j] + 1),
    #                 ha='center')

# ax.set_ylabel('Amount of papers')
# ax.set_title('Attacks')
# ax.set_xticks(pos)

def update_ticks(x, pos):
    return df['Year'][pos]

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(ticker.FuncFormatter(update_ticks))
ax.xaxis.set_minor_locator(ticker.FixedLocator([p+0.5 for p in pos]))
for tick in ax.xaxis.get_minor_ticks():
    tick.tick1line.set_markersize(0)
    tick.tick2line.set_markersize(0)
    tick.label1.set_horizontalalignment('center')
plt.xlim(min(pos), max(pos)+1)
plt.ylim([0, 10+max([max(df[colname]) for colname in df.columns[1:]])])
plt.legend()
# plt.grid()
plt.grid(axis='y', zorder=0, linestyle='--')
plt.show()