# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:39:09 2018

@author: John McKeague
"""

# tanh s' = 0.5[tanh(0.01(s-μ)/σ + 1] #This is the Formula....
#
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

data = data_df['value']



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



data_normalised_a = tanh_normalize(data, 10, 10)



















##________________Find Rolling Average and Rolling Standard Deviation___________
################################################################################
#
#set_window = 10 #function input
#set_min_periods = 10 #function input
#
##Determin Rolling Average
#value_rollingAv = data.rolling(window = set_window,
#                               min_periods = set_min_periods).mean()
#
##Determin Rolling Standard Deviation
#value_rollingStd = data.rolling(window = set_window,
#                                min_periods = set_min_periods).std()
#
##Remove 'Nan' values due to rolling window and min observed periods
#value_rollingAv = value_rollingAv[set_window-1:]
#value_rollingStd = value_rollingStd[set_window-1:]
#
#
##_________________________Find Tanh Normalization______________________________
################################################################################
#
##Creating Normalisation Function - TanH Estimator
##Documentation found https://stackoverflow.com/questions/43061120/tanh-estimator-normalization-in-python
#
##Setting inner calculation 
#sigma = (master_df['value'] - master_df['value_rollingAv'])/master_df['value_rollingStd']
#sigma_prime = (sigma*0.01)+1
#
##Calculate Normalised 
#value_normalised = np.tanh(sigma_prime)*0.5

def tanh_normalize(data_df, set_window,set_min_periods):
    
    #_______________Find Rolling Average and Rolling Standard Deviation________
    ###########################################################################
    #data_df: Determin Rolling Average
    value_rollingAv = data_df.rolling(window = set_window,
                                   min_periods = set_min_periods).mean() 
    #data_df: Determin Rolling Standard Deviation
    value_rollingStd = data_df.rolling(window = set_window,
                                    min_periods = set_min_periods).std()
    #data_df: Remove 'Nan' values due to rolling window and min observed periods
    value_rollingAv = value_rollingAv[set_window-1:]
    value_rollingStd = value_rollingStd[set_window-1:]
    
    
    #_______________________Find Tanh Normalization____________________________
    ###########################################################################
    #Setting inner calculation 
    sigma = (master_df['value'] - master_df['value_rollingAv'])/master_df['value_rollingStd']
    sigma_prime = (sigma*0.01)+1  
    #Calculate Normalised 
    value_normalised = np.tanh(sigma_prime)*0.5

        
      
        
        
        
        
        



















