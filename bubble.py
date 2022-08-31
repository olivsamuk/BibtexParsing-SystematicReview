import pandas as pd

papers = pd.read_csv("papers-categorized-new.csv")
data = {}
# COUNT PAPERS PER YEAR

for index, each_paper in papers.iterrows():

        if data.get(each_paper['problem']):
            if each_paper['attack'] in data[each_paper['problem']].keys():
                data[each_paper['problem']][each_paper['attack']]+=1
            else:
                data[each_paper['problem']].update({each_paper['attack']: 1})
        else:
            data[each_paper['problem']] = {each_paper['attack']: 1}

print(data)