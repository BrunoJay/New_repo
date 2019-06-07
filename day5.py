# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:17:18 2019

@author: BRUNO ZOE
"""

from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt

import pandas as pd

import csv

url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

#url = "one.csv"
#url = "example/africa.csv"

data=pd.read_csv(url)

text = data.Region

#text = data.response #Region

wordcloud = WordCloud(

  width = 3000,

  height = 2000,

  background_color = 'black',

  stopwords = STOPWORDS).generate(str(text))

fig = plt.figure(

  figsize = (40, 30),

  facecolor = 'k',

  edgecolor = 'k')

plt.imshow(wordcloud, interpolation = 'bilinear')

plt.axis('off')

plt.tight_layout(pad=0)

plt.savefig('results2.png')

plt.show()