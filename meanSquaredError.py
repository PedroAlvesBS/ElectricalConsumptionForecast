def MeanSquaredError(expected, forecasted):
    '''
    This function will take two arrays with the same dimension and calculate
    the mean squared error between the array forecasted and the expected.

    Example:
        >> import numpy as np
        >> a = np.array([1,2,3])
        >> b = np.array([4,5,6])
        >> print(MeanSquaredError(a,b))
        >> 243

    '''
    try:
        if expected.shape != forecasted.shape:
            print(
                f"Shapes do not match expected{expected.shape} x forecasted {forecasted.shape}")
        else:
            return (pow((expected-forecasted), 2).sum())/len(forecasted)
    except:
        print('The parameters given do not correspond to Pandas DataFrames')
