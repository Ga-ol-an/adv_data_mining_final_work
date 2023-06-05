# Import the numpy and pandas package
import pandas as pd
import numpy as np

# Data visualisation
import matplotlib.pyplot as plt
import seaborn as sns



# Lendo o arquivo CSV
annouced_cars = pd.read_csv('Databases/cars_no_about_no_accessories.csv')

# Exibindo as primeiras linhas do DataFrame
#print(annouce_cars.head())

###! Para printar somente uma coluna, descomente o bloco a seguir
#column_name = 'preco'  # Substitua pelo nome da coluna desejada
# Plotando o gráfico de IQR
# plt.boxplot(annouced_cars[column_name])
# plt.title('IQR {}'.format(column_name))
# plt.ylabel('Valores')
# plt.xlabel('Coluna')
# plt.show()

# Apagando linhas com atributos faltantes
annouced_cars.dropna(inplace=True)

fig, axs = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(annouced_cars['preco'], ax = axs[0])
plt2 = sns.boxplot(annouced_cars['quilometragem'], ax = axs[1])
plt3 = sns.boxplot(annouced_cars['ano'], ax = axs[2])
plt.tight_layout()
plt.savefig('Plots/Initial_IQRs.pdf') # Talvez precise de mudar essa linha aqui
plt.show()

