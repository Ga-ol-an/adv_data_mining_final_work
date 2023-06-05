# Import the numpy and pandas package
import pandas as pd
import numpy as np

# Data visualisation
import matplotlib.pyplot as plt
import seaborn as sns


announced_cars = pd.read_csv('Databases/cars_no_about_no_accessories.csv')

# Apagando linhas com atributos faltantes
announced_cars.dropna(inplace=True)

columns = ['preco', 'quilometragem','ano']  # Substitua pelo nome das colunas desejadas

for column in columns:
    Q1 = announced_cars.quantile(0.25)
    Q3 = announced_cars.quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    announced_cars = announced_cars[(announced_cars >= lower_bound) & (announced_cars <= upper_bound)]


# Exibindo o DataFrame após remover os outliers

## OBS: Não faz tanto sentido assim printar o IQR depois de retirar os outliers. Eu printei mais para sabermos que funcionou.
# Talvez trabalhar em uma forma melhor de trabalhar o como mostrar isso.

## OBS 2: Esse código tá meio que muito simples, sem funcoes e tals, não me precoupei muito com a qualidade ainda. 

fig, axs = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(announced_cars['preco'], ax = axs[0])
plt2 = sns.boxplot(announced_cars['quilometragem'], ax = axs[1])
plt3 = sns.boxplot(announced_cars['ano'], ax = axs[2])
plt.tight_layout()
plt.savefig('Plots/Without_outliers_IQRs.pdf') # Talvez precise de mudar essa linha aqui
plt.show()

