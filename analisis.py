# ============================================================
# Actividad 3 - Ciencia de Datos
# Análisis de Regresión Lineal Simple
# ============================================================

# Configuración para evitar errores de entorno gráfico
import matplotlib
matplotlib.use('Agg')

# Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

# ============================================================
# 1. CONFIGURACIÓN GENERAL
# ============================================================
RUTA_DATOS = "Datos/dataset.csv"
CARPETA_SALIDA = "Visualizaciones"

os.makedirs(CARPETA_SALIDA, exist_ok=True)

print("\nINICIO DEL ANÁLISIS\n")

# ============================================================
# 2. OBTENCIÓN DE LOS DATOS
# ============================================================
try:
    df = pd.read_csv(RUTA_DATOS)
    print("Dataset cargado correctamente.\n")
except Exception as e:
    print("Error al cargar el dataset:", e)
    exit()

# ============================================================
# 3. VALIDACIÓN DEL DATASET
# ============================================================
if 'Hits' not in df.columns or 'Runs' not in df.columns:
    print("Error: El dataset debe contener las columnas 'Hits' y 'Runs'.")
    exit()

# ============================================================
# 4. EXPLORACIÓN INICIAL
# ============================================================
print("Primeras filas del dataset:\n", df.head(), "\n")
print("Información del dataset:\n")
df.info()
print("\nEstadísticas descriptivas:\n", df.describe(), "\n")

# ============================================================
# 5. LIMPIEZA Y PREPARACIÓN DE DATOS
# ============================================================
print("Valores nulos antes de la limpieza:\n", df.isnull().sum(), "\n")

# Eliminación de valores nulos
df = df[['Hits', 'Runs']].dropna()

# Verificación de duplicados
duplicados = df.duplicated().sum()

print("Valores nulos después de la limpieza:\n", df.isnull().sum())
print("Número de registros duplicados:", duplicados, "\n")

# ============================================================
# 6. ANÁLISIS EXPLORATORIO (CORRELACIÓN)
# ============================================================
correlacion = df['Hits'].corr(df['Runs'])
print("Coeficiente de correlación de Pearson:", correlacion)

if correlacion > 0.9:
    print("Interpretación: Existe una relación positiva muy fuerte entre las variables.\n")
elif correlacion > 0.7:
    print("Interpretación: Existe una relación moderada.\n")
else:
    print("Interpretación: Relación débil o inexistente.\n")

# ============================================================
# 7. VISUALIZACIÓN DE LOS DATOS
# ============================================================
plt.figure()
plt.scatter(df['Hits'], df['Runs'])
plt.xlabel('Hits')
plt.ylabel('Runs')
plt.title('Relación entre Hits y Runs')
plt.savefig(f"{CARPETA_SALIDA}/01_datos_reales.png")
plt.close()

# ============================================================
# 8. DEFINICIÓN DE VARIABLES
# ============================================================
X = df[['Hits']]
y = df['Runs']

# ============================================================
# 9. ESTANDARIZACIÓN DE DATOS
# ============================================================
scaler = StandardScaler()
X_escalado = scaler.fit_transform(X)

# ============================================================
# 10. DIVISIÓN DE DATOS
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X_escalado, y, test_size=0.2, random_state=42
)

print("Tamaño de entrenamiento:", X_train.shape)
print("Tamaño de prueba:", X_test.shape, "\n")

# ============================================================
# 11. ENTRENAMIENTO DEL MODELO
# ============================================================
modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("Modelo entrenado correctamente.\n")

# ============================================================
# 12. PREDICCIONES
# ============================================================
y_pred = modelo.predict(X_test)

# ============================================================
# 13. EVALUACIÓN DEL MODELO
# ============================================================
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)

print("Resultados del modelo:")
print("R2:", r2)
print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae, "\n")

# ============================================================
# 14. VISUALIZACIÓN DEL MODELO
# ============================================================
X_ordenado = X.sort_values(by='Hits')
y_linea = modelo.predict(scaler.transform(X_ordenado))

plt.figure()
plt.scatter(df['Hits'], df['Runs'], label='Datos reales')
plt.plot(X_ordenado, y_linea, label='Modelo de regresión')
plt.xlabel('Hits')
plt.ylabel('Runs')
plt.title('Modelo de Regresión Lineal')
plt.legend()
plt.savefig(f"{CARPETA_SALIDA}/02_modelo_regresion.png")
plt.close()

# ============================================================
# 15. COMPARACIÓN REAL VS PREDICHO
# ============================================================
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel('Valores reales')
plt.ylabel('Valores predichos')
plt.title('Comparación Real vs Predicho')
plt.savefig(f"{CARPETA_SALIDA}/03_comparacion.png")
plt.close()

# ============================================================
# 16. INTERPRETACIÓN DEL MODELO
# ============================================================
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_

print("Interpretación del modelo:")
print(f"Por cada incremento de una unidad en Hits, Runs aumenta aproximadamente {pendiente:.4f}.")
print(f"El modelo explica el {r2*100:.2f}% de la variabilidad de los datos.\n")

# ============================================================
# 17. CONCLUSIÓN
# ============================================================
if r2 > 0.9:
    print("Conclusión: El modelo presenta un desempeño excelente y alta capacidad predictiva.")
elif r2 > 0.7:
    print("Conclusión: El modelo es adecuado, pero puede mejorarse.")
else:
    print("Conclusión: El modelo no es suficientemente preciso.")

print("\nFIN DEL ANÁLISIS\n")