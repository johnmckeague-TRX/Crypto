# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:57:47 2018

@author: John McKeague
"""
import pandas as pd
import numpy as np
import chardet


###############################################################################
############################## FUNCTIONS ######################################
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

def tanh_normalize(data_set, set_window,set_min_periods, window_type= None):
    
    #<Parameter Definitions>
    
    
    #data_set: Pandas Dataframe: Should be 1-dimensional column
    
    #Pandas 'Rolling' Function Documentation https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html
    
    #set_window: Size of moving window i.e. number of observation to calc statistic
    #min_periods: Minimum number of observation required to have a value
    
    #_______________Find Rolling Average and Rolling Standard Deviation________
    ###########################################################################
    #data_df: Determin Rolling Average
    value_rollingAv = data_set.rolling(window = set_window,
                                       min_periods = set_min_periods,
                                       win_type = window_type).mean() 
    #data_df: Determin Rolling Standard Deviation
    value_rollingStd = data_set.rolling(window = set_window,
                                    min_periods = set_min_periods).std()
    
    
    #_______________________Find Tanh Normalization____________________________
    ###########################################################################
    #Setting inner calculation 
    sigma = (data_set - value_rollingAv)/value_rollingStd
    sigma_prime = (sigma*0.01)+1  
    #Calculate Normalised 
    data_normalised = np.tanh(sigma_prime)*0.5
    
    return data_normalised



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
############################## ACTIONS ########################################
###############################################################################
window =10
min_period=10

data_normalised = tanh_normalize(data_df['value'], window, min_period)
#remove nan values
data_normalised =data_normalised[-len(data_normalised)+min_period:]

#get smoothed values via fourier transform
smooth = fastfourier_transform(data_normalised, 5)

###############################################################################

x_plot = data_df['timestamp'][-len(data_normalised)+min_period:]
y_plot = data_df['value'][-len(data_normalised)+min_period:]

if (len(x_plot)<=len(y_plot)):
    axis_length = len(x_plot)
else:
    axis_length = len(y_plot)



import matplotlib.pyplot as plt
#%matplotlib inline

#plt.plot(x_plot,y_plot)
plt.plot(x_plot,smooth[0:axis_length])
plt.show()

















