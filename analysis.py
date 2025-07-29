
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline



Olympic_Swimming_Results = pd.read_csv("C:/Users/xenia/OneDrive/Desktop/Olympic_Swimming_Results_1912to2020.csv")
Olympic_Swimming_Results = Olympic_Swimming_Results.dropna()


##¿Qué nadadores han ganado más medallas individuales en pruebas no relevo?

top_nadadores = Olympic_Swimming_Results[
    (Olympic_Swimming_Results["Relay?"] == 0) & 
    (Olympic_Swimming_Results["Rank"].isin([1, 2, 3]))
]
conteo_medallas = top_nadadores.groupby("Athlete").size().reset_index(name="Total Medals")
top_10 = conteo_medallas.sort_values("Total Medals", ascending=False).head(10)


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

# Coeficientes
print("Pendiente (mejora por año):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)



# Calcular la velocidad de mejora en 100m Libre Hombres

X = libre_100_hombres["Year"].values.reshape(-1, 1)   
y = libre_100_hombres["Results"].values               

# Crear modelo y ajustar regresión lineal simple
modelo = LinearRegression()
modelo.fit(X, y)

velocidad_mejora_por_año = modelo.coef_[0]

print(f"Velocidad de mejora: {velocidad_mejora_por_año:.4f} segundos por año")

# Predecir el tiempo ganador en 2024 Con regresión lineal simple
año_2024 = np.array([[2024]])
prediccion_2024 = modelo.predict(año_2024)

print(f"Predicción del tiempo ganador en 2024 regresión lineal simple: {prediccion_2024[0]:.4f} segundos")  


# Modelo polinómico de grado 2
grado = 2
modelo_poly = make_pipeline(PolynomialFeatures(degree=grado), LinearRegression())
modelo_poly.fit(X, y)

# Predicción modelo polinómico grado 2
predicciones_poly = modelo_poly.predict(X)

# Visualización modelo polinómico grado 2
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Resultados reales")
plt.plot(X, predicciones_poly, color="green", label=f"Regresión polinómica (grado {grado})")
plt.title("Evolución del tiempo ganador en 100m libre masculino")
plt.xlabel("Año")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)
plt.show()

# Coeficientes del modelo polinómico grado 2
modelo_entrenado = modelo_poly.named_steps['linearregression']
print("Coeficientes del modelo polinómico grado 2:", modelo_entrenado.coef_)
print("Intercepto:", modelo_entrenado.intercept_)

# Predecir el tiempo ganador en 2024 Con regresión polinómica grado 2
poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
poly_model.fit(X, y)

# Predicción polinómica
pred_2024_poly = poly_model.predict(np.array([[2024]]))
print(f"Predicción polinómica 2024: {pred_2024_poly[0]:.4f} segundos")


# Ordenar libre_100_hombres ordenado por año
libre_100_hombres = libre_100_hombres.sort_values("Year").reset_index(drop=True)

# Calcular la diferencia entre tiempos consecutivos
libre_100_hombres["Diferencia (s)"] = libre_100_hombres["Results"].diff()

# Mostrar las diferencias junto con año y tiempo
diferencias = libre_100_hombres[["Year", "Results", "Diferencia (s)"]]

print(diferencias)

#graficar las diferencias de edicion a edcion de los juegos olímpicos en los 100m libre masculino

plt.bar(diferencias["Year"], diferencias["Diferencia (s)"], color='skyblue', edgecolor='black')
plt.axhline(0, color='gray', linestyle='--')
plt.title("Diferencia de tiempo ganador año a año (100m libre masculino)")
plt.xlabel("Año")
plt.ylabel("Diferencia en segundos")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
