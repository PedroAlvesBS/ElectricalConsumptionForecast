# Brazilian Electrical Consumption Forecast using Multilayer Perceptron

This work were developed by the Electrical Engineering Students from Centro Federal de Educação Tecnológica de Minas Gerais: 

[Igor de Souza Fonseca](https://www.linkedin.com/in/igor-souza-fonseca/) and [Pedro Henrique A B Santos](https://www.linkedin.com/in/phabs-1584b4123/)

under the orientation of the Professor

[Dr. Israel Teodoro Mendes](http://lattes.cnpq.br/1848195540280650),
 
and had the purpose of predict the electrical consumption based on its time series through Machine Learning Technique called multilayer perceptron.

## Dependencies

Our project was developed in Python and has the following libraries dependencies:
 
 - [Numpy](https://numpy.org/doc/stable/)
 - [Pandas](https://pandas.pydata.org/docs/)
 - [Tensorflow](https://www.tensorflow.org/?hl=pt-br)
 - [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
 - [Matplotlib](https://matplotlib.org/)

## Data

The data is in the project with the label 'Data.csv' and was formatted by ourselves ([EPE](https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/consumo-de-energia-eletrica)).

It comprehends monthly records of power in Mega Watt Hour from January - 2004 to December - 2021, in a total of 216 records.


## Execution

To execute the service you must go to the 'main.py' file and give some parameters.

- **rt** (float: 0 < x < 1): Rate of training data (if 0.6, it will correspond to 60:40/train:test)

- **nm** (string): The label of output file

- **nstp** (integer): Number of input neurons

- **nout** (integer): Number of output neuron
