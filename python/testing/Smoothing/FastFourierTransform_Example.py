# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:19:53 2018

@author: John McKeague
"""

#______________________Import Required Libraries_______________________________
###############################################################################
import pandas as pd
import numpy as np
import chardet


#______________________Import Price Data from CSV______________________________
###############################################################################
#defining directory path to our text data source
path = "C:\\Users\\John McKeague\\Documents\\PersonalProjects\\CryptoCurrency_Analysis\\data\\Dummy_Data_csv.csv"

with open(path, 'rb') as f:
    char_type= chardet.detect(f.readline())  # or readline if the file is large
#print(char_type)

#pandas read data into table, sets headings
data_df = pd.read_table(path,encoding='latin_1', header=None, delimiter=',', names=['timestamp','value'])
#print(data)


###############################################################################
################ EXAMPLE:FUNCTION AND HOW TO USE FUNCTION #####################
###############################################################################

def fastfourier_transform( value_axis, freq_reduction):
            
    #Preform Discrete Fourier Transform on real values
    #- Online Documentation-
    #https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.fft.rfft.html 
    y_hat = np.fft.rfft(value_axis)
    
    #Set Frequency deduction Term. Acceptable values are between 1-len(y_hat)
    #Lower Freq_Term increases smoothing of dataset, higher Freq_Terms trys to exactly fit input set
    
    #Set values which occour after Freq_Term to zero
    y_hat[freq_reduction:] = 0.0
    
    #Preform Inverse Discrete Fourier Transform - i.e. Returns Transformed data back to real values
    #- Online Documentation-
    #https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.fft.irfft.html
    smooth = np.fft.irfft(y_hat)
    
    #Convert np array to pd dataframe
    smooth_df = pd.DataFrame(data = smooth)
    
    return smooth_df
  

values = data_df['value']
smooth = fastfourier_transform(values, 10)
###############################################################################


###############################################################################
############################ VISUALISATION ####################################
###############################################################################

x_len = len(data_df['timestamp'])
y_len = len(data_df['value'])
y_smooth_len = len(smooth)

print(x_len)
print(y_len)
print(y_smooth_len)

#Due to how Fourier Transform operates, transformed data has different length than to input set

x_plot = data_df['timestamp'][0:1000]
y_plot = data_df['value'][0:1000]


import matplotlib.pyplot as plt
#%matplotlib inline

plt.plot(x_plot,y_plot)
plt.plot(x_plot,smooth[0:1000])
plt.show()























