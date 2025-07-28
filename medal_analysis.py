
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


Olympic_Swimming_Results = pd.read_csv("C:/Users/xenia/OneDrive/Desktop/Olympic_Swimming_Results_1912to2020.csv")
Olympic_Swimming_Results = Olympic_Swimming_Results.dropna()


##¿Qué nadadores han ganado más medallas individuales en pruebas no relevo?

top_nadadores = Olympic_Swimming_Results[
    (Olympic_Swimming_Results["Relay?"] == 0) & 
    (Olympic_Swimming_Results["Rank"].isin([1, 2, 3]))
]
conteo_medallas = top_nadadores.groupby("Athlete").size().reset_index(name="Total Medals")
top_10 = conteo_medallas.sort_values("Total Medals", ascending=False).head(10)

print(top_10)

##¿Cuál es la evolución de los tiempos ganadores en 100m Libre Hombres a lo largo de los años?

libre_100_hombres = Olympic_Swimming_Results[
    (Olympic_Swimming_Results["Distance (in meters)"] == "100m") &
    (Olympic_Swimming_Results["Stroke"] == "Freestyle") &
    (Olympic_Swimming_Results["Gender"] == "Men") &
    (Olympic_Swimming_Results["Rank"] == 1)
].copy()

libre_100_hombres["Results"] = pd.to_numeric(libre_100_hombres["Results"], errors="coerce")
libre_100_hombres = libre_100_hombres.dropna(subset=["Results"])

evolucion = libre_100_hombres[["Year", "Results"]].sort_values("Year")

print(evolucion)



## Modelo de regresión lineal para predecir el tiempo ganador en 100m Libre Hombres

libre_100_hombres["Results"] = pd.to_numeric(libre_100_hombres["Results"], errors="coerce")
libre_100_hombres = libre_100_hombres.dropna(subset=["Results", "Year"])

X = libre_100_hombres["Year"].values.reshape(-1, 1)
y = libre_100_hombres["Results"].values
modelo = LinearRegression()
modelo.fit(X, y)

predicciones = modelo.predict(X)


# Visualización
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Resultados reales")
plt.plot(X, predicciones, color="red", label="Regresión lineal")
plt.title("Evolución del tiempo ganador en 100m libre masculino")
plt.xlabel("Año")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)
plt.show()

# Coeficientes
print("Pendiente (mejora por año):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)

print(libre_100_hombres.shape)


# Calcular la velocidad de mejora en 100m Libre Hombres

X = libre_100_hombres["Year"].values.reshape(-1, 1)   
y = libre_100_hombres["Results"].values               

# Crear modelo y ajustar
modelo = LinearRegression()
modelo.fit(X, y)

velocidad_mejora_por_año = modelo.coef_[0]

print(f"Velocidad de mejora: {velocidad_mejora_por_año:.4f} segundos por año")


