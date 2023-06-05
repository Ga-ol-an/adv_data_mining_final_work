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

#Printa a coluna Motor
print(annouced_cars['motor'])
