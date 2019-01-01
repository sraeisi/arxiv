import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import datetime
import json as js


##this file reads the data downloaded from https://github.com/HeinrichHartmann/arxiv_meta/blob/
##discards the empty or unnecessary fields, and creates a pandas dataframe, using 
##that data.


#path = "Archives/"
path = "shortList"
# np.loadtxt(file)
#temp_file = ''
recordList = []
idList = []
for root, dirs, files in os.walk(path, False):
    print(root)
    for file in files:
        with open(root +'/' + file) as f:
            temp_file = f.readline() 
            while(temp_file):
                record = js.loads(temp_file)
                idList.append(record[0])
                recordList.append(record[1])
                temp_file = f.readline() 
            

        
"""        
keySet = {'contributor', 'coverage', 'creator', 'date', 'description', 'format', 'identifier', 'language',
 'publisher', 'relation', 'rights', 'source', 'subject', 'title', 'type'}
i = 0
propList = [set([]) for i in range(len(keySet))]
for keyInd, key in enumerate(keySet):
    #print(key)
    for record in recordList:
        propList[keyInd].update(record[key])
    
    
for keyInd, key in enumerate(keySet):
    print(key,": ", len(propList[keyInd]))

print(len(recordList))


for record in recordList:
    for keyInd, key in enumerate(keySet):
        if(len(propList[keyInd]))<=1 :
            record.pop(key, None)
"""

recordDataFrame =  pd.DataFrame(recordList)
recordDataFrame['ID'] = idList
recordDataFrame.index = list ( recordDataFrame['ID'] )
recordDataFrame = recordDataFrame.drop('ID', axis = 1)
omittedList = ["contributor", "coverage", "format", "publisher",  "relation", "rights","source","type"]
"""
#recordDataFrame.loc['0706.1954']
keyAttributes = []
for key in recordDataFrame.keys():
    tempSet = set(recordDataFrame[key].sum())
    
    print( key," " , len(tempSet) )
    keyAttributes.append ( len(tempSet) )
    
for keyInd, key in enumerate( recordDataFrame.keys() ):
    if( keyAttributes[keyInd] <= 1 ):
        print( "omitted key: ", key )
        recordDataFrame = recordDataFrame.drop(key, axis = 1)
"""

for keyInd, key in enumerate( omittedList ):
    print( "omitted key: ", key )
    recordDataFrame = recordDataFrame.drop(key, axis = 1)

#recordDataFrame.to_csv('Archive_DataFrame.csv')
recordDataFrame.to_csv('Sample_DataFrame.csv')