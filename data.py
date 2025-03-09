import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset con el delimitador correcto
df = pd.read_csv("dato.csv", sep=";")

# Mostrar los nombres de las columnas para verificar
print(df.columns)

# Revisión inicial
total_filas, total_columnas = df.shape
costo_promedio = df["Costo de Vida"].mean()

# País con mayor y menor costo de vida
pais_mas_caro = df.loc[df["Costo de Vida"].idxmax(), "Pais"]
pais_mas_barato = df.loc[df["Costo de Vida"].idxmin(), "Pais"]

# Datos de Perú
peru = df[df["Pais"] == "Peru"]
costo_peru = peru["Costo de Vida"].values[0] if not peru.empty else "No disponible"
ranking_peru = peru["Ranking Global"].values[0] if not peru.empty else "No disponible"

# Mostrar información
print(f"Nro. de Filas: {total_filas}")
print(f"Nro. de Columnas: {total_columnas}")
print(f"Costo de vida promedio: {costo_promedio:.2f}")
print(f"País con costo de vida más alto: {pais_mas_caro}")
print(f"País con costo de vida más bajo: {pais_mas_barato}")
print(f"Costo de Vida en Perú: {costo_peru}")
print(f"Ranking de Perú: {ranking_peru}")

# Visualización de los 10 países con el costo de vida más alto
top_10_caro = df.nlargest(10, "Costo de Vida")
plt.figure(figsize=(12,6))
sns.barplot(data=top_10_caro, x="Costo de Vida", y="Pais", palette="Reds_r")
plt.title("Top 10 países con mayor costo de vida")
plt.xlabel("Costo de Vida")
plt.ylabel("Países")
plt.show()

# Visualización de los 10 países con el costo de vida más bajo
top_10_barato = df.nsmallest(10, "Costo de Vida")
plt.figure(figsize=(12,6))
sns.barplot(data=top_10_barato, x="Costo de Vida", y="Pais", palette="Blues")
plt.title("Top 10 países con menor costo de vida")
plt.xlabel("Costo de Vida")
plt.ylabel("Países")
plt.show()

# Filtrar países de América
paises_america = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "Mexico", "Canada", "United States"]
df_america = df[df["Pais"].isin(paises_america)]

# Visualización del costo de vida en América
plt.figure(figsize=(12,6))
sns.barplot(data=df_america, x="Costo de Vida", y="Pais", palette="viridis")
plt.title("Costo de vida en países de América")
plt.xlabel("Costo de Vida")
plt.ylabel("Países")
plt.show()
