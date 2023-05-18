# Import the numpy and pandas package
import pandas as pd
import numpy as np

# Data visualisation
import matplotlib.pyplot as plt
import seaborn as sns



# Lendo o arquivo CSV
annouce_cars = pd.read_csv('Databases/cars_no_about_no_accessories.csv')

# Exibindo as primeiras linhas do DataFrame
#print(annouce_cars.head())

###! Para printar somente uma coluna, descomente o bloco a seguir
#column_name = 'preco'  # Substitua pelo nome da coluna desejada
# Plotando o gráfico de IQR
# plt.boxplot(annouce_cars[column_name])
# plt.title('Gráfico de IQR para a coluna {}'.format(column_name))
# plt.ylabel('Valores')
# plt.xlabel('Coluna')
# plt.show()

fig, axs = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(annouce_cars['preco'], ax = axs[0])
plt2 = sns.boxplot(annouce_cars['quilometragem'], ax = axs[1])
plt3 = sns.boxplot(annouce_cars['ano'], ax = axs[2])
plt.tight_layout()
plt.savefig('../Plots/Initial_IQRs.pdf')
plt.show()