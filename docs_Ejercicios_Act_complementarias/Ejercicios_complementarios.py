# ============================================================
# Ejercicios Complementarios - Semana 4
# ============================================================

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
from scipy import stats

# ============================================================
# EJERCICIO 1: Normalización Min-Max
# ============================================================
print("\nEJERCICIO 1: Normalización Min-Max")

datos = np.array([10, 20, 30, 40, 50])
norm = (datos - datos.min()) / (datos.max() - datos.min())

print("Datos originales:", datos)
print("Datos normalizados:", norm)


# ============================================================
# EJERCICIO 2: Estandarización (Z-Score)
# ============================================================
print("\nEJERCICIO 2: Z-Score")

datos = np.array([2, 4, 4, 4, 5, 5, 7, 9])
media = np.mean(datos)
std = np.std(datos)

z_scores = (datos - media) / std

print("Media:", media)
print("Desviación estándar:", std)
print("Z-scores:", z_scores)


# ============================================================
# EJERCICIO 3: Comparación de técnicas
# ============================================================
print("\nEJERCICIO 3: Comparación de escaladores")

datos = np.array([100, 200, 300, 400, 500]).reshape(-1, 1)

minmax = MinMaxScaler().fit_transform(datos)
standard = StandardScaler().fit_transform(datos)

print("MinMaxScaler:\n", minmax)
print("StandardScaler:\n", standard)


# ============================================================
# EJERCICIO 4: Identificación de valores faltantes
# ============================================================
print("\nEJERCICIO 4: Valores faltantes")

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

print("Valores nulos:\n", df.isnull())
print("Conteo por columna:\n", df.isnull().sum())
print("Porcentaje:\n", df.isnull().mean() * 100)
print("Filas con nulos:\n", df[df.isnull().any(axis=1)])


# ============================================================
# EJERCICIO 5: Estrategias de imputación 
# ============================================================
print("\nEJERCICIO 5: Imputación")

print("Eliminar filas:\n", df.dropna())
print("Imputar media:\n", df.fillna(df.mean()))
print("Imputar mediana:\n", df.fillna(df.median()))

# CORRECTO PARA PANDAS NUEVO
print("Forward fill:\n", df.ffill())
print("Backward fill:\n", df.bfill())


# ============================================================
# EJERCICIO 6: Imputación avanzada
# ============================================================
print("\nEJERCICIO 6: Imputación avanzada")

imputer = SimpleImputer(strategy='mean')
df_imputado = imputer.fit_transform(df)

print("Datos imputados:\n", df_imputado)


# ============================================================
# EJERCICIO 7: Detección de outliers (IQR)
# ============================================================
print("\nEJERCICIO 7: Outliers con IQR")

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])

Q1 = np.percentile(datos, 25)
Q3 = np.percentile(datos, 75)
IQR = Q3 - Q1

lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

outliers = datos[(datos < lim_inf) | (datos > lim_sup)]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Límites:", lim_inf, lim_sup)
print("Outliers:", outliers)


# ============================================================
# EJERCICIO 8: Outliers con Z-score
# ============================================================
print("\nEJERCICIO 8: Outliers con Z-score")

z = stats.zscore(datos)
outliers_z = datos[np.abs(z) > 3]

print("Outliers detectados:", outliers_z)


# ============================================================
# EJERCICIO 9: Manejo de outliers
# ============================================================
print("\nEJERCICIO 9: Manejo de outliers")

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])

# Eliminación
sin_outliers = datos[datos < 50]

# Capping
capped = np.clip(datos, None, 30)

# Log transformación
log_data = np.log(datos)

print("Sin outliers:", sin_outliers)
print("Capped:", capped)
print("Log:", log_data)


# ============================================================
# EJERCICIO 10: Variables categóricas
# ============================================================
print("\nEJERCICIO 10: One-Hot Encoding")

df_cat = pd.DataFrame({
    'color': ['rojo', 'azul', 'verde', 'rojo']
})

encoded = pd.get_dummies(df_cat)

print(encoded)


# ============================================================
# EJERCICIO 11: Transformaciones numéricas
# ============================================================
print("\nEJERCICIO 11: Transformaciones")

datos = np.array([1, 2, 3, 4, 5, 10, 20, 30])

print("Log:", np.log(datos))
print("Raíz:", np.sqrt(datos))


# ============================================================
# EJERCICIO 12: Feature Engineering
# ============================================================
print("\nEJERCICIO 12: Feature Engineering")

df_feat = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df_feat['ratio'] = df_feat['A'] / df_feat['B']
df_feat['diferencia'] = df_feat['A'] - df_feat['B']

print(df_feat)


# ============================================================
# EJERCICIO 13: Escaladores
# ============================================================
print("\nEJERCICIO 13: Escaladores")

data = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("StandardScaler:\n", StandardScaler().fit_transform(data))


# ============================================================
# EJERCICIO 14: Pipeline
# ============================================================
print("\nEJERCICIO 14: Pipeline")

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

print("Pipeline creado:", pipeline)


# ============================================================
# EJERCICIO 15: Investigación
# ============================================================
print("\nEJERCICIO 15")

print("Preparación de datos mejora la calidad del modelo")
print("Data leakage es fuga de información")
print("Train/Test separa entrenamiento y evaluación")


# ============================================================
# EJERCICIO 16: Técnicas avanzadas
# ============================================================
print("\nEJERCICIO 16")

print("SMOTE: balanceo de clases")
print("KNN Imputer: imputación por vecinos")
print("Target Encoding: codificación avanzada")
