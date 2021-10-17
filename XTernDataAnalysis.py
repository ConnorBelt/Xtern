import pandas as pd
from geopy import distance

data = pd.read_csv('ActivityPlan.csv')

data['lon'].astype(float)
data['lat'].astype(float)
name = data['Activity Name']
housing = data.loc[data['Activity'] == 'Housing ']
event = data.loc[data['Activity'] != 'Housing ']

coord1 = list(zip((housing['lat']),(housing['lon'])))
coord2 = list(zip((event['lat']),(event['lon'])))

for j in range(0,6):
    dis = 0
    for i in range(0,16):
        k = distance.distance(coord1[j],coord2[i]).miles
        dis = dis+k
    print("Housing: {}, Total Distance Traveled to Activities: {}".format(name[j],dis))
