import pandas as pd
def substring_after(s, delim):
    return s.partition(delim)[0]

def get_data(csv_file):
    papers = pd.read_csv(csv_file)
    data = {}
    for index, each_paper in papers.iterrows():
        data[index] = {'title': each_paper['title'], 'base':substring_after(each_paper['bases'], "-")}
    return data

papers = get_data('papers-categorized-new.csv')
print(papers)