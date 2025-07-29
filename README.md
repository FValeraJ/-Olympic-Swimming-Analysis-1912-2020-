# Olympic-Swimming-Analysis 1912–2020

Este proyecto explora los resultados de natación en los Juegos Olímpicos desde 1912 hasta 2020, utilizando Python y Power BI para extraer insights relevantes sobre atletas, países y evolución del rendimiento.

---

## Objetivos

- Identificar los nadadores con más medallas individuales (excluyendo relevos).
- Analizar la evolución de los tiempos ganadores.
- Visualizar el desempeño por país, estilo de nado y género.

---

## Estructura

| Carpeta/Archivo   | Contenido                                                       |
|-------------------|-----------------------------------------------------------------|
| `data`            | Dataset original sin modificar                                  |
| `analysis`        | Scripts de análisis con Python (Pandas, scikit-learn, etc.)     |
| `visuals`         | Dashboards interactivos generados en Power BI (`.pbix`)         |

---

## Análisis y Resultados

### 1. Nadadores con más medallas individuales (sin relevos)

Se filtraron las competencias individuales (`Relay? = 0`) y se contaron las medallas obtenidas (oro, plata y bronce).

**Top 10 atletas individuales más premiados:**

| Atleta                | Total Medallas |
|-----------------------|----------------|
| Michael Phelps        | 16             |
| Katie Ledecky         | 8              |
| Krisztina Egerszegi   | 7              |
| Ryan Lochte           | 7              |
| Kirsty Leigh Coventry | 6              |
| Mark Spitz            | 6              |
| Inge De Bruijn        | 6              |
| Laszlo Cseh           | 6              |
| Susan O'Neill         | 5              |
| Janet Evans           | 5              |

Michael Phelps domina ampliamente, duplicando al segundo lugar. La mayoría de estos atletas también tienen medallas en relevos, pero aquí solo se consideraron logros individuales.

---

### 2. Evolución del tiempo ganador en 100m libre masculino (1932–2020)

Se analizaron los tiempos de los nadadores ganadores (Rank = 1) en los 100m libres masculinos.

**Resumen de tiempos por año 100 libre:**

## Tabla de Resultados

| Año | Atleta                          | Resultado      |
|-----|----------------------------------|----------------|
| 2020 | Caeleb Dressel                  | 47.02          |
| 2016 | Kyle Chalmers                   | 47.580         |
| 2012 | Nathan Adrian                   | 47.520         |
| 2008 | Alain Bernard                   | 47.210         |
| 2004 | Pieter Van Den Hoogenband      | 48.170         |
| 2000 | Pieter Van Den Hoogenband      | 48.300         |
| 1996 | Alexander Popov                | 48.740         |
| 1992 | Alexander Popov                | 49.020         |
| 1988 | Matthew Biondi                 | 48.630         |
| 1984 | Ambrose Iv Gaines              | 49.800         |
| 1980 | Jörg Woithe                    | 50.400         |
| 1976 | Jim Montgomery                 | 49.990         |
| 1972 | Mark Spitz                     | 51.220         |
| 1968 | Michael Vincent Wenden        | 52.200          |
| 1964 | Donald Arthur Schollander     | 53.400          |
| 1960 | Lance Melvin Larson           | 55.100          |
| 1956 | Jon Malcolm Henricks          | 55.400          |
| 1952 | Clark Currie Scholes          | 57.400          |
| 1952 | Hiroshi Suzuki                 | 57.400         |
| 1948 | Taha Yussuf El Gamal          | 1:00.500        |
| 1936 | Ferenc Csik                    | 57.600         |
| 1932 | Yasuji Mioyazaki               | 58.200         |

Podemos observar una mejora sostenida en los tiempos ganadores desde 1932, pasando de más de 58 segundos a apenas 47.02 en 2020. Sin embargo, a partir del año 2000, la reducción en tiempos se vuelve mucho más lenta, lo que refuerza los hallazgos de la regresión polinómica, que sugiere una desaceleración en la mejora.

Esto se alinea con la teoría de que los nadadores se están acercando al límite fisiológico y técnico de rendimiento en esta prueba. A partir de cierto punto, las mejoras dependen más de factores marginales (tecnología, biomecánica, nutrición, estrategia de carrera), en lugar de cambios drásticos en la preparación o técnica básica.
---

### Modelos de regresión aplicados para interpretación del rendimiento en 100m Libre Hombres 

#### Regresión lineal simple
- Pendiente (mejora promedio por año): −0.1440 segundos
- Predicción para 2024: 45.02 segundos
  <img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/62900e79-1db4-4a49-b745-6ccd3bd16bc3" />


#### Regresión polinómica (grado 2)
- Predicción para 2024: 46.41 segundos
<img width="1000" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/3552f9f3-1bca-4c22-82b7-2c93e5192fc3" />

---

### Comparación de predicciones

| Modelo                | Tiempo estimado en 2024 |
|----------------------|--------------------------|
| Regresión lineal     | 45.02 segundos           |
| Regresión polinómica | 46.41 segundos           |

La regresión lineal indica una mejora constante a lo largo del tiempo.
El modelo polinómico sugiere que la mejora ha comenzado a desacelerarse en años recientes.

Esto se debe al hecho de que, como podemos ver en los datos históricos, los tiempos ganadores han alcanzado un punto cercano al límite fisiológico humano. Es decir, aunque en décadas anteriores se lograban reducciones de tiempo más significativas, en los últimos Juegos Olímpicos la mejora ha sido mínima. El modelo polinómico capta esa curvatura, mostrando cómo la tasa de mejora ya no es lineal, sino que se aplana con el tiempo.
---
### Diferencias Edicion tras edicion de los juegos olimpicos
 Year  Results  Diferencia (s)
| Año  | Tiempo (s) | Diferencia (s) |
| ---- | ---------- | -------------- |
| 1980 | 50.40      | —              |
| 1984 | 49.80      | -0.60          |
| 1988 | 48.63      | -1.17          |
| 1992 | 49.02      | +0.39          |
| 1996 | 48.74      | -0.28          |
| 2000 | 48.30      | -0.44          |
| 2004 | 48.17      | -0.13          |
| 2008 | 47.21      | -0.96          |
| 2012 | 47.52      | +0.31          |
| 2016 | 47.58      | +0.06          |
| 2020 | 47.02      | -0.56          |

<img width="1000" height="500" alt="Figure_3" src="https://github.com/user-attachments/assets/f2a8bccd-72d5-40e1-b961-05ba4f749776" />

El gráfico y la tabla reflejan una tendencia de mejora continua pero no constante, con algunos años donde el rendimiento se estabiliza o retrocede ligeramente. Esto es normal en deportes de élite, donde los márgenes de mejora son cada vez menores y dependen de factores múltiples. Los avances tecnológicos, cambios en técnicas de entrenamiento y la aparición de nadadores excepcionales explican las mejoras más pronunciadas en ciertos años.



---
### Visualización interactiva

Gráficas interactivas disponibles en el archivo `visuals.pbix`, incluyendo:

- Distribución de medallas por país.
- Evolución temporal de resultados.
- Filtros por:
  - País  
  - Año  
  - Género  
  - Distancia  
  - Estilo de nado

---
