from formattingUniData import formatting_the_univariate_data
from splitTrain import split_train
from trainingMLP import training_MLP
from meanSquaredError import MeanSquaredError
import matplotlib.pyplot as plt
from pandas import ExcelWriter, DataFrame
from os.path import isdir
from os import makedirs


def generating_report(data, rate, name, nsteps, noutputs, mvalue):
    '''
    This function will receive 6 parameters:
        data: normalized data
        rate: 0 < x <1 of the splitted data, this corresponds to percentual 
              used to train the model
        name: tris parameter will ve used in the file report creation
        nsteps: is the number of neurons in the input layer
        noutputs: is the number of neuron in the output layer
        mvalue: is the maximum value in the nomalized data

        It is important to say that this  function do not return anything, 
        beyond a report excel file and a figure of the prediction
    '''
    path = f'./reports/T+{noutputs}/{name}/'
    if not isdir(path):
        makedirs(path)

    data_formatted = formatting_the_univariate_data(data, nsteps, noutputs)

    X_tr, y_tr, X_ts, y_ts = split_train(
        data_formatted, rate, nsteps, noutputs)

    out, model = training_MLP(X_tr, y_tr, X_ts, nsteps, noutputs)

    # Printing The comparison between both
    plt.plot(out*mvalue, color='red', label='Forecast')
    plt.plot(y_ts*mvalue, color='blue', label='Test Serie')
    plt.xlabel('Months')
    plt.title(f'Forecast the electrical energy consumption through {len(out)} months', fontdict={
              'fontsize': 14}, pad=20)
    plt.ylabel('Electrical Energy Compuption (MWh)')
    plt.legend(loc='upper left')
    plt.savefig(f'{path}fig{name}.png')

    # Creating Excel
    nlayers = len(model.layers)
    row = 0

    writer = ExcelWriter(f'{path}Report{name}.xlsx', engine='openpyxl')

    doOut = out.flatten()
    doYts = y_ts.flatten()
    dfOutput = DataFrame({'Forecasted': doOut,
                          'Expected': doYts,
                          'Difference': doOut-doYts})
    dfOutput.to_excel(writer, sheet_name='Output', index=False)

    doMSE = [MeanSquaredError(out, y_ts)]
    dfMse = DataFrame({'MSE': doMSE})
    dfMse.to_excel(writer, sheet_name='MSE', index=False)

    for i in range(nlayers):
        varname = f'df{i}'
        bib = ' = DataFrame('
        finalproduct = varname + bib + '{'
        worb = len(model.layers[i].get_weights())
        for j in range(worb):
            neurons = len(model.layers[i].get_weights()[j])
            for k in range(neurons):
                if j == 0:
                    finalproduct += f'\'L{i+1}Wn{k+1}\': model.layers[{i}].get_weights()[{j}][{k}],'
                else:
                    finalproduct += f'\'L{i+1}B\':model.layers[{i}].get_weights()[{j}]'
                    break
        finalproduct += '})'
        exec(finalproduct)
        exec(f'{varname}.to_excel(writer, sheet_name=\'WeightsAndBiases\', startrow={row}, index=False)')
        row += 22
        writer.save()

    writer.close()
    print('\nFinished...\n')
