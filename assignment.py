import numpy as np
import pandas as pd
import pickle
from datetime import date

def load_csv(filepath):
    data = []
    col = []
    checkcol = False
    with open(filepath) as f:
        for val in f.readlines():
            val = val.replace("\n","")
            val = val.split(',')
            if checkcol is False:
                col = val
                checkcol = True
            else:
                data.append(val)
    df = pd.DataFrame(data=data, columns=col)
    return df

myData = load_csv('AssignmentData.csv')
print(myData.head())


table1 = pd.read_csv('AssignmentData.csv')
dict1 = table1.to_dict()

#for item in dict1.items():

#for index, row in table1.iterrows():
#    if(row["gender2"] != "male" or row["gender2"] != "female"):



# table1_misspel = table1.replace(misspel, "female")

#col_selected = table1[['Date of Service', 'Date of Birth', 'gender2']]
#for index, row in col_selected.iterrows():
    #if(row["Date of Service"]


#assignmentTable = numpy.genfromtxt('assignmentData.csv', delimiter=',', skip_header=1, dtype=None)