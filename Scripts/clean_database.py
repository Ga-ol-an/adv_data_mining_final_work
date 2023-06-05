# Import the numpy and pandas package
import pandas as pd
import numpy as np

# Data visualisation
import matplotlib.pyplot as plt
import seaborn as sns



def apply_mask(mask_regex, column, dataframe):
    mascara = dataframe[column].str.contains(mask_regex, regex=True, case = False)
    dataframe = dataframe[mascara]
    return dataframe


caminho_arquivo = 'Databases/cars_20230601.csv'

# Ler o arquivo CSV usando o Pandas
annouced_cars = pd.read_csv(caminho_arquivo)

#Remove linhas nulas
annouced_cars = annouced_cars.dropna()

# Definir a expressão regular para extrair o motor
motor_regex = r'([1-9]\.[0-9])'  

#Aplica uma máscara para remover aquelas linhas que não contem o motor
annouced_cars = apply_mask(motor_regex, 'descricao', annouced_cars )

#Cria a coluna motor
annouced_cars['motor'] = annouced_cars['descricao'].str.extract(motor_regex, expand=False)


## O código a seguir remove linhas baseado no numero de ocorrencia

# Define the columns to consider
columns_to_check = ['marca', 'modelo', 'tipo'] 

# Define the threshold for the number of occurrences
occurrence_threshold = 15  

# Create a mask to identify rows with values that occur more than 15 times
mask = annouced_cars.groupby(columns_to_check)[columns_to_check[0]].transform('count') > 15

# Filter the data based on the mask
annouced_cars = annouced_cars[mask]


# Display the resulting data
print(annouced_cars)

annouced_cars.to_csv('outputs/db_filtrado_04062023.csv', index=False)
