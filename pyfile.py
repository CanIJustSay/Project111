import pandas as pd
import plotly.figure_factory as pff
import random
import statistics
import plotly.graph_objects as pgo
import os
os.system("cls")

df = pd.read_csv("data1.csv")
mathScore = df["Math_score"].tolist()

finalList = []
def Sample():
    sampleData = []
    for i in range(1,101):
        ranpos = random.randint(0, (len(mathScore)-1))
        val = mathScore[ranpos]
        sampleData.append(val)
    mean = statistics.mean(sampleData)
    finalList.append(mean)


for i in range(1, 1001):
    Sample()

mean = statistics.mean(finalList)
stdev = statistics.stdev(finalList)

firstSP = mean - stdev
firstEP = mean + stdev

secondSP = mean - (2*stdev)
secondEP = mean + (2*stdev)

thirdtSP = mean - (3*stdev)
thirdEP = mean + (3*stdev)

onedf = pd.read_csv("School_3_Sample.csv")
data1Math = onedf["Math_score"].tolist()
data1mean = statistics.mean(data1Math)



graph = pff.create_distplot([finalList],["Math Scores"],show_hist=False)
#mean
graph.add_trace(pgo.Scatter(x=[data1mean,data1mean],y=[0,0.17],mode="lines",name="Mean of Data 1"))

#stdevs
graph.add_trace(pgo.Scatter(x=[firstEP,firstEP],y=[0,0.17],mode="lines",name="First stdev"))

graph.add_trace(pgo.Scatter(x=[secondEP,secondEP],y=[0,0.17],mode="lines",name="Second stdev"))

graph.add_trace(pgo.Scatter(x=[thirdEP,thirdEP],y=[0,0.17],mode="lines",name="Third stdev"))


graph.show()

