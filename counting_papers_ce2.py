import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import pandas as pd
import re

def normalize_titles(title):
    return re.sub(re.compile('<.*?>'), '', title.upper().replace("\n", " "))

with open('new_citations/EV.bib') as ev:
    ev_database = bibtexparser.load(ev)
with open('new_citations/ieeexplore.bib') as ieeexplore:
    ieeexplore_database = bibtexparser.load(ieeexplore)
with open('new_citations/scopus.bib') as scopus:
    scopus_database = bibtexparser.load(scopus)
with open('new_citations/SD.bib') as sd:
    sd_database = bibtexparser.load(sd)
with open('new_citations/WOS.bib') as wos:
    wos_database = bibtexparser.load(wos)

ev_citations_list = ev_database.entries
ieeexplore_citations_list = ieeexplore_database.entries
scopus_citations_list = scopus_database.entries
sd_citations_list = sd_database.entries
wos_citations_list = wos_database.entries

def substring_after(s, delim):
    return s.partition(delim)[0]

papers = pd.read_csv("papers-categorized-new.csv")
data = {}

ev_counter = 0
ieee_counter = 0
scopus_counter = 0
sd_counter = 0
wos_counter = 0

final_bib = []

for index, each_paper in papers.iterrows():
    base = substring_after(each_paper['bases'], "-")
    flag = base
    data[index] = {'title': each_paper['title'], 'base': base}

    if base == 'Engineering Village':
        ev_counter+=1
        for each_ref in ev_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
                flag = ''
        if flag != '':
            final_bib.append({'nao': 'achei'})
    elif base == 'IEEExplore':
        ieee_counter+=1
        for each_ref in ieeexplore_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
                flag = ''
        if flag != '':
            final_bib.append({'nao': 'achei'})
    elif base == 'Scopus':
        scopus_counter+=1
        for each_ref in scopus_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
    elif base == 'Science Direct':
        sd_counter+=1
        for each_ref in sd_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
                flag = ''
        if flag != '':
            final_bib.append({'nao': 'acheiSD'})
    elif base == 'Web of Science':
        wos_counter+=1
        for each_ref in wos_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)

# print(data, '\nEV: ', ev_counter, '\nIEEE: ', ieee_counter, '\nSCOPUS: ', scopus_counter, '\nSD: ', sd_counter, '\nWOS: ', wos_counter, '\nTotal: ', ev_counter+ieee_counter+scopus_counter+sd_counter+wos_counter)

new_db = BibDatabase()
new_db.entries = final_bib
# bibtex_str = bibtexparser.dumps(new_db)
#
# print(bibtex_str)
for each_ref in new_db.entries:
    # print(each_ref.keys())
    if 'journal' in each_ref.keys():
        print(each_ref['journal'])
    elif 'booktitle' in each_ref.keys():
        print(each_ref['booktitle'])
    else:
        print('manoooo: ', each_ref['title'], each_ref['doi'])