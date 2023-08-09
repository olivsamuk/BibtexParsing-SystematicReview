import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import pandas as pd
import re

def normalize_titles(title):
    return re.sub(re.compile('<.*?>'), '', title.upper().replace("\n", " "))

with open('citations_FULL/EV.bib') as ev:
    ev_database = bibtexparser.load(ev)
with open('citations_FULL/ieeexplore.bib') as ieeexplore:
    ieeexplore_database = bibtexparser.load(ieeexplore)
with open('citations_FULL/scopus.bib', encoding="utf8") as scopus:
    scopus_database = bibtexparser.load(scopus)
with open('citations_FULL/SD.bib', encoding="utf8") as sd:
    sd_database = bibtexparser.load(sd)
with open('citations_FULL/WOS.bib') as wos:
    wos_database = bibtexparser.load(wos)
with open('citations_FULL/complementary.bib') as comp:
    comp_database = bibtexparser.load(comp)

ev_citations_list = ev_database.entries
ieeexplore_citations_list = ieeexplore_database.entries
scopus_citations_list = scopus_database.entries
sd_citations_list = sd_database.entries
wos_citations_list = wos_database.entries
comp_citations_list = comp_database.entries

def substring_after(s, delim):
    return s.partition(delim)[0]

papers = pd.read_csv("papers-categorized-final.csv")[lambda x: x['modeling'] == 'finite-state transducer']

data = {}

ev_counter = 0
ieee_counter = 0
scopus_counter = 0
sd_counter = 0
wos_counter = 0
comp_counter = 0

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
            final_bib.append({'nao': 'acheiEV '+each_paper['title']})
    elif base == 'IEEExplore':
        ieee_counter+=1
        for each_ref in ieeexplore_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
                flag = ''
        if flag != '':
            final_bib.append({'nao': 'acheiIEEE '+each_paper['title']})
    elif base == 'Scopus':
        scopus_counter+=1
        for each_ref in scopus_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
                flag = ''
        if flag != '':
            final_bib.append({'nao': 'acheiSCOPUS ' + each_paper['title']})
    elif base == 'Science Direct':
        sd_counter+=1
        for each_ref in sd_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
                flag = ''
        if flag != '':
            final_bib.append({'nao': 'acheiSD '+each_paper['title']})
    elif base == 'Web of Science':
        wos_counter+=1
        for each_ref in wos_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
                flag = ''
        if flag != '':
            final_bib.append({'nao': 'acheiWOS ' + each_paper['title']})
    elif base == 'Complementary':
        comp_counter+=1
        for each_ref in comp_citations_list:
            if normalize_titles(each_ref['title']) == each_paper['title']:
                final_bib.append(each_ref)
                flag = ''
        if flag != '':
            final_bib.append({'nao': 'acheiCOMP ' + each_paper['title']})

print(data, '\nEV: ', ev_counter, '\nIEEE: ', ieee_counter, '\nSCOPUS: ', scopus_counter, '\nSD: ', sd_counter, '\nWOS: ', wos_counter, '\nCOMP: ', comp_counter, '\nTotal: ', ev_counter+ieee_counter+scopus_counter+sd_counter+wos_counter+comp_counter)

new_db = BibDatabase()
new_db.entries = final_bib

print('Tamanho do bib:', len(final_bib))
# bibtex_str = bibtexparser.dumps(new_db)
#
# print(bibtex_str)
# print(final_bib)

new_counter=0
ids = []
for each_ref in new_db.entries:
    new_counter+=1
    # print(each_ref.keys())

    if 'title' in each_ref.keys():
        ids.append(each_ref['ID'])
        # print(new_counter, '= ID:', each_ref['ID'], ', Title: ' , each_ref['title'])
        # if 'journal' in each_ref.keys():
        #     print(new_counter, ': ', each_ref['title'], ' - ', each_ref['journal'])
        #
        # elif 'booktitle' in each_ref.keys():
        #     print(new_counter, ': ', each_ref['title'], ' - ', each_ref['booktitle'])
        #
        # else:
        #     print(new_counter, ': ', each_ref['title'], ' - ', 'Erro1: Unknown venue')
    else:
        print(new_counter, ': ', '(Erro 2) ', each_ref)
print(ids)
