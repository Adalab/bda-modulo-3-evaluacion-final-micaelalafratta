
# FASE 1: Exploración y limpieza
## EDA
### 1.1. EDA: Exploración inicial. Customer Flight Activity 
Datos sobre vuelos. Función exploración.

Solo hay números. 

Detección problemas:

1. NULOS: No hay nulos

2. VALORES ATÍPICOS: 
- Hay 1864 duplicados. 
- ¿por qué el 95.87% de los Loyalty number está duplicado? Hay valores repetidos por viajes recurrentes. El registro es de viajes mensuales/viajero. 
- por qué hay 999986.0 Loyalty Number si el total de filas es 405624. ¿Son consecutivos? ¿Faltan la mitad?

3. DATOS FALTANTES: 

4. TENDENCIA DATOS: ESTADÍSTICA

### 1. 2. EDA: Exploración inicial. Customer Loyalty History. 
Datos personales para fidelización. 

Detección problemas:

1. NULOS: Hay nulos. 

- Salary                25.32    ¿cómo imputar? ver la moda por educación y empresa. 
- Cancellation Year     87.65    - Nulos en Cancellation porque siguen activos. En este caso, nulos altos es positivo.
- Cancellation Month    87.65    - Nulos en Cancellation porque siguen activos

2. VALORES ATÍPICOS: 

- No hay duplicados. 
- Falta "College" en "Education" 

3. DATOS FALTANTES: 

4. TENDENCIA DATOS: ESTADÍSTICA


### 1.3. Unión de los CSV

### 1.4. EDA: Exploración inicial merged

- Cambiar Points Accumulated float64 a int64. No hay medios puntos. ??

## 2. Limpieza datos 

### 2.1. Eliminación valores nulos, datos completos.

### 2.2. Corrección errores: Cambio tipo datos, mayus, minus
Función limpieza. 


# FASE 2: Visualización
Usar la gráfica que se adecúe más. Tipo variables. ¿Una o comparación entre dos o tres?


1. ¿Cómo se distribuye la cantidad de vuelos reservados por mes durante el año?
2. ¿Existe una relación entre la distancia de los vuelos y los puntos acumulados por los cliente?
- Dos variables
3. ¿Cuál es la distribución de los clientes por provincia o estado?
4. ¿Cómo se compara el salario promedio entre los diferentes niveles educativos de los clientes?
5. ¿Cuál es la proporción de clientes con diferentes tipos de tarjetas de fidelidad? 
6. ¿Cómo se distribuyen los clientes según su estado civil y género?



## CRITERIOS:

- Análisis Exploratorio de los datos.*
- Gestión de nulos. *
- Visualización de datos con matplotlib y seaborn.*
- Estadística descriptiva.