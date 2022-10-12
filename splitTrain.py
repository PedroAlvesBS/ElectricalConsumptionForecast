def split_train(data, proportion, nsteps, noutputs):
    '''

    This function receives the data and the proportion
    to be splited.
    The proportion used here is related to the train data,
    as the total is 1, the test will be complement to it.

    Example:
          >>data = [1,2,3,4,5,6]
          >>propotion = 0.6
          >>train, test = split_train(data, proportion)
          >>print (train)
          >> [1,2,3,4]
          >>print (test)
          >> [5,6]

    '''

    if proportion > 0 and proportion <= 1:
        index = round(len(data)*proportion)
        train = data[:index]
        test = data[index:]
        X = train[:, 0:nsteps]
        y = train[:, -noutputs:]
        XT = test[:, 0:nsteps]
        yT = test[:, -noutputs:]
        return X, y, XT, yT
    else:
        return 0, 0, 0, 0
