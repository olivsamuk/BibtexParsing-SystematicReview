import bibtexparser
import re
import sys
import csv
import matplotlib.pyplot as plt

font = {'family' : 'Latin Modern Roman'}
plt.rc('font', **font)

plt.rc('font', size=18)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.rc('legend', fontsize=18)    # legend fontsize
plt.rc('figure', titlesize=18)  # fontsize of the figure title


def new_csv(dict):
    fields = ['id']
    for item in list(dict[0].keys()): fields.append(item)

    with open('papers.csv', 'w', newline='') as csvfile:
        w = csv.DictWriter(csvfile, fieldnames=fields)
        w.writeheader()
        for key, val in sorted(dict.items()):
            row = {'id': key}
            row.update(val)
            w.writerow(row)
    # return w

def normalize_titles(title):
    return re.sub(re.compile('<.*?>'), '', title.upper().replace("\n", " "))

def check_for_existance(full_list, title):
    for i in range(len(full_list.values())):
        if title in full_list[i].values():
            return i


def GetFullList(bases):
    FullList = dict()

    # Generate Full List of Titles
    counter = 0
    for each_base in bases:
        for each_ref in each_base:
            if normalize_titles(each_ref['title']) not in FullList.values():
                FullList.update(
                    {counter: normalize_titles(each_ref['title']) })
                counter += 1

    return FullList

def ce1(FullList,ev_list,ieeexplore_list,scopus_list,sd_list,wos_list):
    NewFullList = dict()
    counter = 0
    for each_paper_title in FullList.values():

        # Check each paper in Engineering Village base
        for each_ref in ev_list:
            if each_paper_title == normalize_titles(each_ref['title']):
                found_paper_index = check_for_existance(NewFullList, normalize_titles(each_ref['title']))
                if found_paper_index is not None:
                    NewFullList[found_paper_index]['bases'].update(
                        {list(NewFullList[found_paper_index]['bases'].keys())[-1] + 1: 'EV'})
                else:
                    NewFullList.update({counter: {'title': normalize_titles(each_ref['title']),
                                                  'year': each_ref['year'], 'bases': {0: 'EV'}}})
                    counter += 1

        # Check each paper in IEEExplore base
        for each_ref in ieeexplore_list:
            if each_paper_title == normalize_titles(each_ref['title']):
                found_paper_index = check_for_existance(NewFullList, normalize_titles(each_ref['title']))
                if found_paper_index is not None:
                    NewFullList[found_paper_index]['bases'].update(
                        {list(NewFullList[found_paper_index]['bases'].keys())[-1] + 1: 'IEEE'})
                else:
                    NewFullList.update({counter: {'title': normalize_titles(each_ref['title']),
                                                  'year': each_ref['year'], 'bases': {0: 'IEEE'}}})
                    counter += 1

        # Check each paper in SCOPUS base
        for each_ref in scopus_list:
            if each_paper_title == normalize_titles(each_ref['title']):
                found_paper_index = check_for_existance(NewFullList, normalize_titles(each_ref['title']))
                if found_paper_index is not None:
                    NewFullList[found_paper_index]['bases'].update(
                        {list(NewFullList[found_paper_index]['bases'].keys())[-1] + 1: 'SCOPUS'})
                else:
                    NewFullList.update({counter: {'title': normalize_titles(each_ref['title']),
                                                  'year': each_ref['year'], 'bases': {0: 'SCOPUS'}}})
                    counter += 1

        # Check each paper in Science Direct base
        for each_ref in sd_list:
            if each_paper_title == normalize_titles(each_ref['title']):
                found_paper_index = check_for_existance(NewFullList, normalize_titles(each_ref['title']))
                if found_paper_index is not None:
                    NewFullList[found_paper_index]['bases'].update(
                        {list(NewFullList[found_paper_index]['bases'].keys())[-1] + 1: 'SD'})
                else:
                    NewFullList.update({counter: {'title': normalize_titles(each_ref['title']),
                                                  'year': each_ref['year'], 'bases': {0: 'SD'}}})
                    counter += 1

        # Check each paper in Web of Science base
        for each_ref in wos_list:
            if each_paper_title == normalize_titles(each_ref['title']):
                found_paper_index = check_for_existance(NewFullList, normalize_titles(each_ref['title']))
                if found_paper_index is not None:
                    NewFullList[found_paper_index]['bases'].update(
                        {list(NewFullList[found_paper_index]['bases'].keys())[-1] + 1: 'WOS'})
                else:
                    NewFullList.update({counter: {'title': normalize_titles(each_ref['title']),
                                                  'year': each_ref['year'], 'bases': {0: 'WOS'}}})
                    counter += 1

    return NewFullList

def join_bases(dict):
    for each_paper in dict.values():
        bases = []
        for each_base in list(each_paper['bases'].values()):
            if each_base == 'EV':
                bases.append('Engineering Village')
            elif each_base == 'IEEE':
                bases.append('IEEExplore')
            elif each_base == 'SCOPUS':
                bases.append('Scopus')
            elif each_base == 'SD':
                bases.append('Science Direct')
            elif each_base == 'WOS':
                bases.append('Web of Science')

        s = '-'.join(bases)
        each_paper['bases'] = s

    return dict

def main():

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

    BasesList = [ev_citations_list, ieeexplore_citations_list, scopus_citations_list, sd_citations_list, wos_citations_list]
    FullList = GetFullList(BasesList)

    # print(FullList)
    # print("EV: ", len(ev_citations_list), "\nIEEE: ", len(ieeexplore_citations_list), "\nSCOPUS", len(scopus_citations_list), "\nSD: ", len(sd_citations_list), "\nWOS: ", len(wos_citations_list), "\nTOTAL: ", len(ev_citations_list)+len(ieeexplore_citations_list)+len(scopus_citations_list)+len(sd_citations_list)+len(wos_citations_list))

    # LIST OF ALL PAPERS (DUPLICATIONS REMOVED)
    after_ce1 = ce1(FullList, ev_citations_list, ieeexplore_citations_list, scopus_citations_list, sd_citations_list, wos_citations_list)
    # JOIN BASES. e.g. 'WOS-IEEE-SD'
    print(after_ce1)

    bases_joint = join_bases(after_ce1)

    # WRITE CSV
    # new_csv(bases_joint)




    # years = ['2016','2017','2018','2019','2020','2021','2022']
    # amount_per_year = [4,5,6,17,22,19,14]
    # # for each_year in years:
    # #     total = 0
    # #     for i in range(len(NewFullList)):
    # #         if NewFullList[i]['year'] == each_year:
    # #             total+=1
    # #     amount_per_year.append(total)
    #
    #
    # # PLOT
    #
    # plt.grid(axis='y', zorder=0, linestyle='--')
    #
    # counter = 0
    # for spine in plt.gca().spines.values():
    #     if counter == 2:
    #         spine.set_visible(True)
    #     else:
    #         spine.set_visible(False)
    #     counter += 1
    #
    # plt.xticks(range(len(amount_per_year)), years)
    # plt.yticks([])
    #
    # bars = plt.bar(range(len(amount_per_year)), amount_per_year, zorder=3, color='#365841')
    # plt.bar_label(bars)
    #
    # plt.show()

    # PAPERS PER BASE ---------------------

    # data = [len(scopus_citations_list),len(wos_citations_list),len(ieeexplore_citations_list),len(sd_citations_list),len(ev_citations_list)]
    # labels = ['Scopus', 'Web of Science', 'IEEExplore', 'Science Direct', 'Eng. Village']
    #
    # plt.tick_params(
    #     axis='x',  # changes apply to the x-axis
    #     which='both',  # both major and minor ticks are affected
    #     bottom=False,  # ticks along the bottom edge are off
    #     top=False,  # ticks along the top edge are off
    #     labelbottom=False)  # labels along the bottom edge are off
    #
    # # plt.grid(axis='x', zorder=0, linestyle='--')
    #
    # counter = 0
    # for spine in plt.gca().spines.values():
    #     if counter == 0:
    #         spine.set_visible(True)
    #     else:
    #         spine.set_visible(False)
    #     counter += 1
    #
    # plt.yticks(range(len(data)), labels)
    #
    # # plt.ylabel('Search Databases')
    # # plt.xlabel('Amounts')
    # # plt.title('I am title')
    #
    # bars = plt.barh(range(len(data)), data, zorder=3, color='#365841')
    # plt.bar_label(bars)
    #
    # plt.show()


if __name__ == '__main__':
    main()