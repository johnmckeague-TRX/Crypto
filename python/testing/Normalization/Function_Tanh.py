# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:16:41 2018

@author: John McKeague
"""

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












