
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

### 1. 2. EDA: Exploración inicial. Customer Loyalty History. 
Datos personales para fidelización. 

Detección problemas:

1. NULOS: Hay nulos. 

- Salary                25.32    ¿cómo imputar? 
    - Faltaban los datos de salario para las personas que tienen "College". Se ha hecho media entre el valor superior (Bachelor) e inferior (High School and below). Se ha sobrescrito "College" con dicha media. 


- Cancellation Year     87.65    - Nulos en Cancellation porque siguen activos. En este caso, nulos altos es positivo.
- Cancellation Month    87.65    - Nulos en Cancellation porque siguen activos. nulos altos es positivo.
    - Imputación inactividad de cancelación (son usuarios activos): Se sustituye por 0
        - Codifica "la cancelación aún no ha ocurrido
        - Permite conversión de NaN a 0. Permite convertir de float a int, como enrollment.

2. VALORES ATÍPICOS: 
- No hay duplicados. 

3. DATOS FALTANTES: 
- Falta "College" en "Education" 

### 1.3. Unión de los CSV

### 1.4. EDA: Exploración inicial merged

- "Points Accumulated": 
        - Parece que "Points Accumulated" es float por error de escritura o porque la aerolínea da número decimales, pero, ¿después se pueden gastar?. 
- Truncar número y quitar decimales o redondear. 
 - float64 a int64 como "Points Redeemed". Los ya gastados son enteros, normalmente con centenas.


# FASE 2: Visualización

1. ¿Cómo se distribuye la cantidad de vuelos reservados por mes durante el año?
2. ¿Existe una relación entre la distancia de los vuelos y los puntos acumulados por los cliente?
- Dos variables
3. ¿Cuál es la distribución de los clientes por provincia o estado?
4. ¿Cómo se compara el salario promedio entre los diferentes niveles educativos de los clientes?
5. ¿Cuál es la proporción de clientes con diferentes tipos de tarjetas de fidelidad? 
6. ¿Cómo se distribuyen los clientes según su estado civil y género?


