  
import csv
import plotly.express as px
import numpy as np
def getDataSource(dataPath):
    coffee = []
    sleep = []
    with open(dataPath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return{'x':coffee,'y':sleep}
def findCorelations(dataSources):
    correlations = np.corrcoef(dataSources['x'],dataSources['y'])
    print("The correlation value between coffee drank and hours of sleep is "+ str(correlations[0,1]))
def setup():
    dataPath = './coffee.csv'
    dataSource = getDataSource(dataPath)
    findCorelations(dataSource)
setup()