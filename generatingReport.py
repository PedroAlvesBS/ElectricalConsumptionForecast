from msilib.schema import Error
from formattingUniData import formatting_the_univariate_data
from splitTrain import split_train
from trainingMLP import training_MLP
from meanSquaredError import MeanSquaredError
import matplotlib.pyplot as plt
from pandas import ExcelWriter, DataFrame, read_csv
from os.path import isdir
from os import makedirs
from exceptionsTreating import exceptions_treating
from normalize import normalize


def generating_report(rate, name, nsteps, noutputs):
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
    data = read_csv('./data.csv')

    norm_dataset = normalize(data)
    st, ct = exceptions_treating(norm_dataset, rate, nsteps, noutputs)
    try:
        if ct > 0:
            raise (Error)

        # Generating the first Graphic
        fig, ax = plt.subplots()
        ax.plot(data['POWER'])
        ax.set_title(
            'Time series of Brazilian electrical consumption througout the years', fontdict={
                'fontsize': 12}, pad=20)
        ax.set_xlabel('Time (months)')
        ax.set_ylabel(f'Electrical Consumption(MWh)')
        fig.savefig('Time series.png')
        path = f'./reports/T+{noutputs}/{name}/'

        if not isdir(path):
            makedirs(path)

        data_formatted = formatting_the_univariate_data(
            norm_dataset, nsteps, noutputs)

        X_tr, y_tr, X_ts, y_ts = split_train(
            data_formatted, rate, nsteps, noutputs)

        out, model = training_MLP(X_tr, y_tr, X_ts, nsteps, noutputs)

        mvalue = data['POWER'].max()

        # Printing The comparison between both
        fig, ax = plt.subplots()
        ax.plot(out*mvalue, color='red', label='Forecast')
        ax.plot(y_ts*mvalue, color='blue', label='Test Serie')
        ax.set_title(
            'Time series of Brazilian electrical consumption througout the years', fontdict={
                'fontsize': 12}, pad=20)
        ax.set_xlabel('Time (months)')
        ax.set_ylabel(f'Electrical Consumption(MWh)')
        fig.savefig(f'{path}fig{name}.png')

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
            exec(
                f'{varname}.to_excel(writer, sheet_name=\'WeightsAndBiases\', startrow={row}, index=False)')
            row += 22
            writer.save()

        writer.close()
        print('\nFinished...\n')
    except:
        print(st)
