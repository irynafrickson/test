import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline

def calculate (in_list):

    # must have 9 digits
    if (len(in_list)==9):
        
        # convert list into 3 x 3 array
        work_array = np.array(in_list)
        work_array = work_array.reshape((3,3))

        # calculate result
        result = {
            'mean': [work_array.mean(axis=0), work_array.mean(axis=1), work_array.mean()],
            'variance': [work_array.var(axis=0), work_array.var(axis=1), work_array.var()],
            'standard deviation': [work_array.std(axis=0), work_array.std(axis=1), work_array.std()],
            'max': [work_array.max(axis=0), work_array.max(axis=1), work_array.max()],
            'min': [work_array.min(axis=0), work_array.min(axis=1), work_array.min()],
            'sum': [work_array.sum(axis=0), work_array.sum(axis=1), work_array.sum()]
            }
        return result
    else:
        print('Value Error. List must contain nine numbers.')

print ('Calculator. Enter 9 numbers, one at a time.')

# Input list
in_list = [0,1,2,3,4,5,6,7,8]

# Intut 9 digits
for i in range(9):
    try:
        in_list[i] = int( input ('Enter digit: '))
    except: 
        print ('Incorrect input')

# Call function
result = calculate (in_list)

# Print result
print ('Result:')
try:
    for key in result:
        print (key + ' : ' + str( result[key] ))
except:
    print ('Try again')
    