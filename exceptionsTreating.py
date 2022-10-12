def exceptions_treating(data, rate, nsteps, noutputs):
    '''
    This function will track exceptions on the entering data
        data must be normalized
        rate must be a float greater than 0 and lower equals to 1
        input neurons must be a positive integer
        output neurons bust be a positive integer
    '''
    str = ''
    ct = 0
    if data.max() > 1:
        str += '\n-Data not normalized\n'
        ct += 1
    if rate <= 0 or rate > 1:
        str += '\n-Rate out of scope\n'
        ct += 1
    if nsteps < 0:
        str += '\n-Invalid input neurons\n'
    if noutputs < 0:
        str += '\n-Invalid output neurons\n'
        ct += 1
    if noutputs + nsteps > len(data):
        str += '\n-Wrong Combinations of input and output neurons\n'
        ct += 1
    return str, ct
