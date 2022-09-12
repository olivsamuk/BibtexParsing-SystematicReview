import json, ast
import pandas as pd

# file = open("json.txt", "r")
# contents = file.read()
# after_ce1 = ast.literal_eval(contents)
# file.close()

def substring_after(s, delim):
    return s.partition(delim)[0]

papers = pd.read_csv("papers-categorized-new.csv")
data = {}

ev_counter = 0
ieee_counter = 0
scopus_counter = 0
sd_counter = 0
wos_counter = 0

for index, each_paper in papers.iterrows():
    base = substring_after(each_paper['bases'], "-")
    data[index] = {'title': each_paper['title'], 'base': base}

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

print(data, '\nEV: ', ev_counter, '\nIEEE: ', ieee_counter, '\nSCOPUS: ', scopus_counter, '\nSD: ', sd_counter, '\nWOS: ', wos_counter, '\nTotal: ', ev_counter+ieee_counter+scopus_counter+sd_counter+wos_counter)


