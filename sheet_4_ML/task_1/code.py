import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
#1- Read the dataset, convert it to DataFrame and display some from it.
dataset=pd.read_csv("Wuzzuf_Jobs.csv")

#2- Display structure and summary of the data.
dataset.describe()

#3- Clean the data (null, duplications).
dataset.dropna(0)#drop null values in Title column
dataset.drop_duplicates(subset =["Title","Company"],keep = "first", inplace = True)

#4- Count the jobs for each company and display that in order (What are the
#   most demanding companies for jobs?).
plotData=dict()
for company in dataset['Company']:
    if company in plotData.keys():
        plotData[company]+=1
    else:
        plotData[company]=1

#5- Show step 4 in a pie chart.       
topcounter =Counter(plotData)
topTen= dict(topcounter.most_common(10))
plt.pie(topTen.values(), labels = topTen.keys())
print("Top 10 Demanding companies:-")
plt.show()

#6- Find out what are the most popular job titles.
plotData=dict()
for title in dataset['Title']:
    if title in plotData.keys():
        plotData[title]+=1
    else:
        plotData[title]=1
#7- Show step 6 in bar chart.      
topcounter =Counter(plotData)
topTen= dict(topcounter.most_common(10))
plt.bar(topTen.keys(),topTen.values(),width=0.2)
plt.xlabel("Job title")
plt.ylabel("Offers")
plt.title("Top 10 Jobs")
plt.show()

#8- Find out the most popular areas?
plotData=dict()
for city in dataset['Location']:
    if city in plotData.keys():
        plotData[city]+=1
    else:
        plotData[city]=1
#9- Show step 8 in bar chart.      
topcounter =Counter(plotData)
topTen= dict(topcounter.most_common(10))
plt.bar(topTen.keys(),topTen.values(),width=0.2)
plt.xlabel("City")
plt.ylabel("Popularity")
plt.title("Top 10 Cities")
plt.show()

#10- Print skills one by one , their count, and order the output to find out
#    the most important skills required.
skillsDict=dict()
for skills in dataset['Skills']:
    for skill in skills.split(','):
        if skill in skillsDict.keys():
            skillsDict[skill]+=1
        else:
            skillsDict[skill]=1
            
topcounter =Counter(skillsDict)
topTen= dict(topcounter.most_common(10))
print("Top 10 skills :-")
for skill,count in topTen.items():    
    print("%s : %d"%(skill,count))
    