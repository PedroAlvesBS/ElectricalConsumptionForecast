from pandas import read_csv
from generatingReport import generating_report


def total_execution():
    dataset = read_csv('./data.csv')
    max_value = dataset['POWER'].max()

    norm_dataset = dataset['POWER']/max_value

    # Put the N of steps,
    #        N of outputs
    #        ^ Univariate data
    # rate of data 0.6 == 60%
    # name is the pattern to be outputted

    rt = 0.6
    nm = '60'
    nstp = 3
    nout = 1
    generating_report(norm_dataset, rate=rt, name=nm,
                      nsteps=nstp, noutputs=nout, mvalue=max_value)


if __name__ == '__main__':
    total_execution()
