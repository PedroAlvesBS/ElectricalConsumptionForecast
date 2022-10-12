from numpy import array


def formatting_the_univariate_data(data, n_steps, n_output=1):
    '''

    This function takes the data and split
    in how many steps we passed.
    This is necessary because we are working
    with univariate input data.

    Example:
            data = [1, 2, 3, 4, 5, 6, 7]
            n_steps = 3
            f_data = formatting_the_univariate_data(data, n_steps)
            >>print(f_data)
            >>[1,2,3,4]
              [2,3,4,5]
              [3,4,5,6]
              [4,5,6,7]

    As we passed 3 steps, then, the 3 first
    columns are the input data, and the 4 one
    is the output expected.

    '''

    if n_steps > 0 and n_steps + n_output < len(data):

        C_LENGTH = n_steps + n_output
        f_output = []
        idx = 0

        while True:
            row = data[idx:(idx + C_LENGTH)].to_numpy()
            f_output.append(row)
            if row[-1] == data.iloc[-1]:
                break

            idx += 1

        return array(f_output)
    else:
        return 0
