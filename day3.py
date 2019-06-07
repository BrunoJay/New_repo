import pandas as pd

import csv

url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

data=pd.read_csv(url)

#print (data)

#data = pd.read_csv(url,skiprows = 1)

c = data.tail()

#c = data.head()

#c = data[['Country','Region']]

#c = data[['Country']]

#c = data[['Region']]

#c = data[data.Region == 'AFRICA']

#c = data[data.Region != 'AFRICA']

#print (c.Region == 'OCEANIA')

#print (c)

#c.to_csv("example/others.csv")

print (c)

