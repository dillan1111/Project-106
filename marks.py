  
import csv
import plotly.express as px
import numpy as np
def getDataSource(dataPath):
    marks = []
    days = []
    with open(dataPath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks.append(float(row['Marks in Percentage']))
            days.append(float(row['Days Present']))
    return{'x':days,'y':marks}
def findCorelations(dataSources):
    correlations = np.corrcoef(dataSources['x'],dataSources['y'])
    print("The correlation value between days present and mark gotten is "+ str(correlations[0,1]))
def setup():
    dataPath = './marks.csv'
    dataSource = getDataSource(dataPath)
    findCorelations(dataSource)
setup()