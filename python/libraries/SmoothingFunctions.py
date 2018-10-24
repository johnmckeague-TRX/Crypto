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
