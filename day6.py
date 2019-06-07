# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:39:11 2019

@author: BRUNO ZOE
"""
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
name = "wepukhulu"
lst = list(name)
length = len(lst)
tname = tuple(lst)

d={1:"class", 2:[3,[4,5,[6,7]]]}
d3 = {}

for i in list(range(length)):
    d3[tup[i]] = tname[i]
    
print(d3.items())
 
#for k,v in d2.items():
    #print(k,v)

#print (d2.items())
    
#d[3] = "bruno"
#del d[1]
#print (d.keys())
#print (d.values())

#for k,v in d.items():
    #print (k,v)


#print number seven from dictionary
v = list(d[2])
i = v[1]
k = i[2]
#print(k[1])