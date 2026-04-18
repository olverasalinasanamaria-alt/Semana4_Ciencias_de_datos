# ============================================================
# Actividades Prácticas - Semana 4
# Preparación y Procesamiento de Datos
# ============================================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# ============================================================
# ACTIVIDAD 4.1: VALORES FALTANTES
# ============================================================
print("\nACTIVIDAD 4.1: Identificación de valores faltantes")

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

print("Valores nulos:\n", df.isnull())
print("Conteo:\n", df.isnull().sum())
print("Información general:\n")
print(df.info())

# ============================================================
# ACTIVIDAD 4.2: IMPUTACIÓN
# ============================================================
print("\nACTIVIDAD 4.2: Imputación")

print("Media:\n", df.fillna(df.mean()))
print("Mediana:\n", df.fillna(df.median()))

# Métodos modernos (pandas nuevo)
print("Forward fill:\n", df.ffill())
print("Backward fill:\n", df.bfill())

# Imputación avanzada
imputer = SimpleImputer(strategy='mean')
df_imputado = imputer.fit_transform(df)
print("Imputación con sklearn:\n", df_imputado)

# ============================================================
# ACTIVIDAD 4.3: TRANSFORMACIÓN
# ============================================================
print("\nACTIVIDAD 4.3: Transformación de datos")

datos = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)

# Normalización
minmax = MinMaxScaler().fit_transform(datos)
print("Min-Max:\n", minmax)

# Estandarización
standard = StandardScaler().fit_transform(datos)
print("Z-score:\n", standard)

# One-Hot Encoding
df_cat = pd.DataFrame({'color': ['rojo', 'azul', 'verde']})
print("One-Hot:\n", pd.get_dummies(df_cat))

# ============================================================
# ACTIVIDAD 4.4: PIPELINE
# ============================================================
print("\nACTIVIDAD 4.4: Pipeline")

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

print("Pipeline creado correctamente:\n", pipeline)

print("\nProceso completado correctamente.")