
import matplotlib.pyplot as plt
import seaborn as sns

'''Función estadística descriptiva. Primer análisis EDA. Incluye describe de columna seleccionada. Con histograma y boxplot'''

def exploracion_num(dataframe,columna):
    print("ESTADÍSTICA DESCRIPTIVA \n")
    print(f"El mínimo de {columna} es", dataframe[columna].min())
    print(f"El máximo de {columna} es", dataframe[columna].max())
    print(f"La media de {columna} es", dataframe[columna].mean())
    print(f"La mediana de {columna} es", dataframe[columna].median())
    print(f"-"*20)
    print(f"DESCRIBE ENTERO:\n {dataframe[columna].describe()} \n")

    print(f"-"*20)

#PRIMERA VISUALIZACIÓN: 

# Histograma (Distribución): Muestra la forma de la distribución

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1) #Dos gráficos uno al lado del otro
    sns.histplot(data=dataframe, x=columna, kde=True) 
    plt.title(f'Histograma de {columna}')


#Box Plot (Atípicos y Dispersión): Muestra la mediana, cuartiles y outliers
    plt.subplot(1, 2, 2)
    sns.boxplot(data=dataframe, x=columna)
    plt.title(f'Box Plot de {columna}')
    
    plt.tight_layout() # Ajusta el espacio para que no se superpongan
    plt.show()


