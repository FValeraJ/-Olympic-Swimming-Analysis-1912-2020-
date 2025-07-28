# Olympic-Swimming-Analysis-1912-2020-


Este proyecto explora los resultados de natación en los Juegos Olímpicos desde 1912 hasta 2020, utilizando Python y Power BI para extraer insights relevantes sobre atletas, países y evolución del rendimiento.

---

##  Objetivos

- Identificar nadadores con más medallas individuales.
- Analizar evolución de tiempos en pruebas icónicas.
- Visualizar desempeño por país y estilo de nado.
- Preparar dataset limpio para Power BI.

---

##  Estructura

| Carpeta         | Contenido                                                                 |
|----------------|--------------------------------------------------------------------------|
| `data/`         | Dataset original sin modificar                                           |
| `analysis/`     | Scripts de análisis con Pandas                                           |
| `visuals/`      | Gráficos generados                                            |


---
🔎 Análisis y resultados
🥇 1. Nadadores con más medallas individuales (sin relevos)
Se filtraron las competencias individuales (no relevos) y se contaron las medallas (oro, plata y bronce).

Top 10 atletas individuales más premiados:

Athlete	Total Medals
Michael Phelps	16
Katie Ledecky	8
Krisztina Egerszegi	7
Ryan Lochte	7
Kirsty Leigh Coventry	6
Mark Spitz	6
Inge De Bruijn	6
Laszlo Cseh	6
Susan O'Neill	5
Janet Evans	5

🗒️ Michael Phelps domina absolutamente, duplicando al segundo lugar. La mayoría de estos atletas también tienen medallas en relevos, pero aquí solo se consideraron logros individuales.

⏱️ 2. Evolución del tiempo ganador en 100m libre masculino
Se analizaron los tiempos ganadores (Rank = 1) de la prueba de 100m libre masculino desde 1932 hasta 2020.

Resultados por año:

1932 – 58.20s  
1936 – 57.60s  
1952 – 57.40s  
1956 – 55.40s  
1960 – 55.10s  
1964 – 53.40s  
1968 – 52.20s  
1972 – 51.22s  
1976 – 49.99s  
1980 – 50.40s  
1984 – 49.80s  
1988 – 48.63s  
1992 – 49.02s  
1996 – 48.74s  
2000 – 48.30s  
2004 – 48.17s  
2008 – 47.21s  
2012 – 47.52s  
2016 – 47.58s  
2020 – 47.02s

Tendencia: Con un modelo de regresión lineal simple, se obtuvo:
<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/5675630a-abc9-4af6-ad39-ecedd70ea158" />


Pendiente: -0.1440 segundos por año

Intercepto: 336.56

🔁 Interpretación: En promedio, los nadadores han mejorado su tiempo en unos 0.14 segundos por año, lo cual es bastante si se toma en cuenta que las diferencias entre oro y plata suelen ser de centésimas.



📈 Gráficas interactivas disponibles
Dentro del archivo interactive_graphs.ipynb puedes encontrar un dashboard para explorar:

Distribución de medallas de oro, plata y bronce.

Filtros por:

-País

-Año

-Género

-Distancia (metros)

-Tipo de nado (stroke)
