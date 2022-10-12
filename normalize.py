def normalize(dataset):
    '''
    This function will normalize the data given
    '''
    norm_dataset = dataset['POWER']/dataset['POWER'].max()

    return norm_dataset
