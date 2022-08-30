import json, ast
import pandas as pd

# file = open("json.txt", "r")
# contents = file.read()
# after_ce1 = ast.literal_eval(contents)
# file.close()

def substring_after(s, delim):
    return s.partition(delim)[0]

papers = pd.read_csv("papers-categorized.csv")
data = {}

ev_counter = 0
ieee_counter = 0
scopus_counter = 0
sd_counter = 0
wos_counter = 0

for index, each_paper in papers.iterrows():
    base = substring_after(each_paper['bases'], "-")

    if base == 'Engineering Village':
        ev_counter+=1
    elif base == 'IEEExplore':
        ieee_counter+=1
    elif base == 'Scopus':
        scopus_counter+=1
    elif base == 'Science Direct':
        sd_counter+=1
    elif base == 'Web of Science':
        wos_counter+=1

print('EV: ', ev_counter, '\nIEEE: ', ieee_counter, '\nSCOPUS: ', scopus_counter, '\nSD: ', sd_counter, '\nWOS: ', wos_counter)

# for each_paper in after_ce1.values():
#
#     if each_paper['bases'][0] == 'EV':
#         ev_counter+=1
#     elif each_paper['bases'][0] == 'IEEE':
#         ieee_counter+=1
#     elif each_paper['bases'][0] == 'SCOPUS':
#         scopus_counter+=1
#     elif each_paper['bases'][0] == 'SD':
#         sd_counter+=1
#     elif each_paper['bases'][0] == 'WOS':
#         wos_counter+=1
#
# print('EV: ', ev_counter, '\nIEEE: ', ieee_counter, '\nSCOPUS: ', scopus_counter, '\nSD: ', sd_counter, '\nWOS: ', wos_counter)



# f = open("json.txt", "w")
# f.write(str(after_ce1))
# f.close()