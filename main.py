from generatingReport import generating_report


def total_execution():
    # Put the N of steps,
    #        N of outputs
    #        ^ Univariate data
    # rate of data 0.6 == 60%
    # name is the pattern to be outputted

    rt = 0.6
    nstp = 1
    nout = 1
    generating_report(rate=rt,
                      nsteps=nstp, noutputs=nout)


if __name__ == '__main__':
    total_execution()
