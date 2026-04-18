# Semana 4: Preparación y Procesamiento de Datos

## 1. Introducción

En la presente semana desarrollé un conjunto de actividades enfocadas en la preparación y procesamiento de datos, elementos fundamentales dentro del flujo de trabajo en ciencia de datos. A lo largo de este trabajo, comprendí que la calidad de los resultados obtenidos en cualquier modelo depende directamente de la calidad de los datos utilizados.

Desde mi perspectiva, esta etapa es crítica, ya que permite transformar datos crudos en información estructurada y útil para el análisis. En este sentido, no solo ejecuté código, sino que también analicé, interpreté y reflexioné sobre cada técnica aplicada.

---

## 2. Ejercicios Complementarios

### Ejercicio 1: Normalización Min-Max

En este ejercicio apliqué la técnica de normalización Min-Max, cuyo objetivo es escalar los datos dentro de un rango específico, generalmente entre 0 y 1.

A partir de los datos [10, 20, 30, 40, 50], realicé el cálculo manual y posteriormente lo validé mediante Python. El resultado obtenido fue:

[0, 0.25, 0.5, 0.75, 1]

Esto confirma que la transformación fue correcta, ya que todos los valores se encuentran dentro del rango esperado.

Desde mi análisis, esta técnica es útil cuando se requiere comparar variables con diferentes escalas.

---

### Ejercicio 2: Estandarización (Z-Score)

En este caso, trabajé con la estandarización, que transforma los datos para que tengan media 0 y desviación estándar 1.

Calculé:

* Media = 5
* Desviación estándar = 2

Los valores estandarizados mostraron una distribución centrada en cero, lo cual es ideal para muchos modelos de machine learning.

Considero que esta técnica es especialmente útil cuando se desea eliminar el efecto de la escala sin perder la distribución original de los datos.

---

### Ejercicio 3: Comparación de técnicas

Comparé MinMaxScaler y StandardScaler, observando que:

* MinMaxScaler limita los valores entre 0 y 1
* StandardScaler centra los datos en torno a 0

Desde mi punto de vista, la elección depende del tipo de modelo y la naturaleza de los datos.

---

### Ejercicio 4: Valores faltantes

Identifiqué valores faltantes dentro de un DataFrame utilizando funciones como isnull(), sum() y mean().

Detecté:

* 20% de valores faltantes en la columna A
* 40% en la columna B

Esto me permitió comprender la importancia de evaluar la calidad de los datos antes de cualquier análisis.

---

### Ejercicio 5: Imputación de datos

Apliqué diferentes estrategias:

* Eliminación de filas
* Imputación con media
* Imputación con mediana
* Forward fill
* Backward fill

Cada técnica tiene implicaciones distintas. Por ejemplo, eliminar datos reduce el tamaño del dataset, mientras que imputar puede introducir sesgos.

---

### Ejercicio 6: Imputación avanzada

Utilicé SimpleImputer de sklearn, lo cual permite automatizar el proceso de imputación.

Esto facilita el trabajo en datasets grandes y mejora la reproducibilidad del análisis.

---

### Ejercicio 7: Detección de outliers (IQR)

Calculé:

* Q1 = 14
* Q3 = 22
* IQR = 8

Identifiqué como outlier el valor 100.

Este método es efectivo para detectar valores extremos en distribuciones no normales.

---

### Ejercicio 8: Detección de outliers (Z-score)

Aplicando Z-score, confirmé nuevamente que el valor 100 es un outlier significativo.

Esto refuerza la importancia de utilizar múltiples métodos para validar resultados.

---

### Ejercicio 9: Manejo de outliers

Exploré diferentes estrategias:

* Eliminación
* Capping
* Transformación logarítmica

Desde mi análisis, la mejor estrategia depende del contexto y del impacto en el modelo.

---

### Ejercicio 10: Variables categóricas

Implementé One-Hot Encoding, transformando variables categóricas en variables numéricas.

Esto es fundamental para que los modelos puedan interpretar datos categóricos.

---

### Ejercicio 11: Transformaciones numéricas

Apliqué transformaciones como logaritmo y raíz cuadrada, observando cómo afectan la distribución de los datos.

Estas técnicas ayudan a reducir la asimetría y mejorar el rendimiento de los modelos.

---

### Ejercicio 12: Feature Engineering

Creé nuevas variables como ratios y diferencias, lo cual permite enriquecer el dataset.

Considero que esta es una de las etapas más importantes, ya que puede mejorar significativamente la capacidad predictiva del modelo.

---

### Ejercicio 13: Escaladores

Analicé el uso de diferentes escaladores, concluyendo que cada uno tiene un propósito específico dependiendo del tipo de datos.

---

### Ejercicio 14: Pipeline

Implementé un pipeline que integra escalamiento y modelado.

Esto permite automatizar el flujo de trabajo y asegurar consistencia en el proceso.

---

### Ejercicio 15: Investigación

Comprendí que:

* La preparación de datos es esencial para obtener buenos resultados
* Data leakage puede invalidar un modelo
* La separación entre entrenamiento y prueba es fundamental

---

### Ejercicio 16: Técnicas avanzadas

Investigé técnicas como:

* SMOTE
* KNN Imputation
* Target Encoding

Estas herramientas permiten abordar problemas más complejos en ciencia de datos.

---

## 3. Actividades Prácticas

Durante el desarrollo de las actividades prácticas, trabajé en:

* Identificación de valores faltantes
* Aplicación de técnicas de imputación
* Transformación de datos
* Creación de pipelines

Cada una de estas actividades reforzó mi comprensión sobre la importancia del preprocesamiento.

---

## 4. Resumen de Aprendizaje

A lo largo de esta semana aprendí que:

* La preparación de datos es una etapa crítica
* Los datos deben ser limpiados antes de modelar
* Las transformaciones mejoran la calidad del análisis
* Los pipelines facilitan la automatización

---

## 5. Dudas o Reflexión

Durante el desarrollo, me surgieron cuestionamientos sobre:

* Qué técnica de imputación es más adecuada en diferentes contextos
* Cómo evitar el overfitting en datasets pequeños
* Qué impacto tienen los outliers en modelos complejos

Estas dudas me motivan a seguir profundizando en el área.

---

## 6. Referencias

* Documentación oficial de pandas
* Documentación de scikit-learn
* Material de clase

---

## 7. Conclusión

En conclusión, esta semana me permitió comprender que la ciencia de datos no se trata únicamente de aplicar modelos, sino de preparar adecuadamente la información. Considero que las habilidades adquiridas son fundamentales para cualquier análisis futuro.

Este proceso fortaleció mi pensamiento crítico y mi capacidad para interpretar datos de manera estructurada y fundamentada.
