# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:16:34 2019

@author: BRUNO ZOE
"""

import requests

from bs4 import BeautifulSoup

# the target we want to open

url='https://www.monitor.co.ug/'

#open with GET method

resp=requests.get(url)

print ("i am here")

print (resp)

#http_respone 200 means OK status

if resp.status_code==200:

  print("Successfully opened the web page")

  print("The news are as follows :- ")

  # we need a parser,Python built-in HTML parser is enough .

  soup=BeautifulSoup(resp.text,'html.parser')

  # l is the list which contains all the text i.e news

  #l=soup.find("div",{"class":"five-eight column"})
  l=soup.find_all("section",{"class":"aside column"})
  
  #print ("Results: ")

  #now we want to print only the text part of the anchor.

  #print (l,"hello")

  #for i in l.findAll("p"):

    #print(i.text)

  for i in l:
      hs = i.find_all("a")
      length = len(hs)
      #print(hs[length-1].text)
      
  for h in hs:
      print(h.text)
              
  else:

    print("Error")