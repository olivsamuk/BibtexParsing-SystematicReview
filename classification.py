import bibtexparser
import json, ast
from main import normalize_titles

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


file = open("json.txt", "r")
contents = file.read()
after_ce1 = ast.literal_eval(contents)
file.close()

_counter = 0
for each_paper in after_ce1.values():
    if 'classification' not in each_paper or 'attack_type' not in each_paper or 'methods' not in each_paper:

        if each_paper['bases'][0] == 'EV':
            for each_ref in ev_citations_list:
                if normalize_titles(each_ref['title']) == each_paper['title']:
                    print(_counter, ' - ', each_ref['title'], '(', each_ref['year'] , ')' , '\n', each_ref['author'],'\n', each_ref['abstract'])
        elif each_paper['bases'][0] == 'IEEE':
            for each_ref in ieeexplore_citations_list:
                if normalize_titles(each_ref['title']) == each_paper['title']:
                    print(_counter, ' - ', each_ref['title'], '(', each_ref['year'] , ')' , '\n', each_ref['author'],'\n', each_ref['abstract'])
        elif each_paper['bases'][0] == 'SCOPUS':
            for each_ref in scopus_citations_list:
                if normalize_titles(each_ref['title']) == each_paper['title']:
                    print(_counter, ' - ', each_ref['title'], '(', each_ref['year'] , ')' , '\n', each_ref['author'],'\n', each_ref['abstract'])
        elif each_paper['bases'][0] == 'SD':
            for each_ref in sd_citations_list:
                if normalize_titles(each_ref['title']) == each_paper['title']:
                    print(_counter, ' - ', each_ref['title'], '(', each_ref['year'] , ')' , '\n', each_ref['author'],'\n', each_ref['abstract'])
        elif each_paper['bases'][0] == 'WOS':
            for each_ref in wos_citations_list:
                if normalize_titles(each_ref['title']) == each_paper['title']:
                    print(_counter, ' - ', each_ref['title'], '(', each_ref['year'] , ')' , '\n', each_ref['author'],'\n', each_ref['abstract'])

        _counter += 1

        # Classification
        if 'classification' not in each_paper:
            classification = input('\nEnter the classification, or -1 to quit: ')
            if classification == '-1':
                f = open("json.txt", "w")
                f.write(str(after_ce1))
                f.close()

                break
            else:
                each_paper['classification'] = classification
        else:
            print('\nClassification: ', each_paper['classification'])

        #Type of Attack
        if 'attack_type' not in each_paper:
            attack_type = input('\nEnter the attack type, or -1 to quit: ')

            if attack_type == '-1':
                f = open("json.txt", "w")
                f.write(str(after_ce1))
                f.close()

                break
            else:
                each_paper['attack_type'] = attack_type
        else:
            print('\nAttack type: ', each_paper['attack_type'])

        # methods
        if 'methods' not in each_paper:
            methods = input('\nEnter the methods, or -1 to quit: ')

            if methods == '-1':
                f = open("json.txt", "w")
                f.write(str(after_ce1))
                f.close()

                break
            else:
                each_paper['methods'] = methods

        # modelling

        modelling = input('\nEnter the modelling, or -1 to quit: ')

        if modelling == '-1':
            f = open("json.txt", "w")
            f.write(str(after_ce1))
            f.close()

            break
        else:
            each_paper['modelling'] = modelling

        print('\n' * 50)
    else:
        _counter+=1

f = open("json.txt", "w")
f.write(str(after_ce1))
f.close()