
import matplotlib.pyplot as plt
import seaborn as sns

#VARIABLES NUMÉRICAS: 

## Tipos de variables:

    # - Continuas-> medir. Decimales. Pueden tomar infinitos valores dentro de un rango.
    #     - temperatura, peso, precio
    # - Discretas -> contar. Números enteros. Toman valores concretos dentro de un rango.
    #     - nº hijos, 

#Histograma: distribución variable numérica.
#Cómo se distribuyen valores y qué patrones hay.

"""Args:
        columna (str): El nombre de la columna a graficar (eje X).
        df (pd.DataFrame): El DataFrame que contiene los datos."""

def numerica_histplot (x, data):
    sns.histplot(
        x = columna,    # Nombre de la columna (como string)
        data = df,      # El DataFrame
        color = "violet",
        kde = True      # Opcional: añade la línea de densidad
    )
    plt.title(f'Distribución de: {columna}') # Añadir título es buena práctica
    plt.show() # Muestra el gráfico