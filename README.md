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

**Resumen de tiempos por año (selección):**

| Año  | Tiempo Ganador (s) |
|------|---------------------|
| 1932 | 58.20               |
| 1968 | 52.20               |
| 1988 | 48.63               |
| 2008 | 47.21               |
| 2020 | 47.02               |

---

### Modelos de regresión aplicados

#### Regresión lineal simple
- Ecuación estimada:  
  Tiempo = -0.1440 × Año + 336.56
- Pendiente (mejora promedio por año): −0.1440 segundos
- Predicción para 2024: 45.02 segundos
  <img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/62900e79-1db4-4a49-b745-6ccd3bd16bc3" />


#### Regresión polinómica (grado 2)
- Ecuación estimada:  
  Tiempo = 0.0009167 × Año² - 3.7697 × Año + 3920.92
- Predicción para 2024: 46.41 segundos
<img width="1000" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/3552f9f3-1bca-4c22-82b7-2c93e5192fc3" />

---

### Comparación de predicciones

| Modelo                | Tiempo estimado en 2024 |
|----------------------|--------------------------|
| Regresión lineal     | 45.02 segundos           |
| Regresión polinómica | 46.41 segundos           |

La regresión lineal indica una mejora constante. El modelo polinómico sugiere que la mejora ha comenzado a desacelerarse en años recientes.
esto se debe al hecho de quede como podemos ver 

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
