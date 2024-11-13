# Reporte de Aida Laricchia
## Lectura: Introducción al Aprendizaje Estadístico
### Respuestas a los puntos 1, 2, 5, 6 y 7 de la sección 2.4 (página 52 del ISLRv2)

### 1. En cada uno de los apartados (a) a (d), ¿esperaríamos que el rendimiento de un método flexible sea mejor o peor que el de un método inflexible? Justifique su respuesta.

**a) El tamaño de la muestra \( n \) es extremadamente grande y el número de predictores \( p \) es pequeño.**

En este caso, se esperaría que un método inflexible sea más adecuado. Cuando hay muchos datos y pocos predictores, un modelo sencillo como la regresión lineal es capaz de capturar la relación entre los predictores y la respuesta de manera efectiva, sin riesgo de sobreajuste. Un enfoque flexible podría ser innecesariamente complejo.

**b) El número de predictores \( p \) es extremadamente grande y el número de observaciones \( n \) es pequeño.**

Aquí, un enfoque flexible sería preferible. Con muchos predictores y pocos datos, un modelo inflexible no tendría suficiente capacidad para capturar la complejidad del problema. Un modelo flexible, por otro lado, podría ajustarse mejor a la relación entre los predictores y la respuesta.

**c) La relación entre los predictores y la respuesta es altamente no lineal.**

Un modelo flexible sería más adecuado en este caso. Métodos como los árboles de decisión o las redes neuronales son capaces de modelar relaciones no lineales complejas que los modelos inflexibles, como la regresión lineal, no pueden representar.

**d) La varianza de los términos de error, \( \sigma^2 = Var(\epsilon) \), es extremadamente alta.**

En este escenario, un método inflexible podría ser preferido. Los modelos flexibles tienden a ajustarse demasiado a la variabilidad de los errores, lo que puede llevar a un sobreajuste. En contraste, los modelos inflexibles son más robustos ante el ruido, lo que puede resultar en un mejor rendimiento en nuevos datos.

### 2. Explica si cada escenario es un problema de clasificación o regresión, y señala si nos interesa más la inferencia o la predicción. Además, proporciona los valores de \( n \) y \( p \).

**a) Recolectamos datos de las 500 principales empresas de EE. UU., registrando su beneficio, número de empleados, industria y salario del CEO. Nos interesa entender qué factores afectan al salario del CEO.**

- **Tipo de problema:** Regresión.
- **Objetivo principal:** Inferencia (identificar los factores que afectan al salario del CEO).
- **\( n \):** 500, **\( p \):** 3 (beneficio, número de empleados, industria).

**b) Estamos considerando lanzar un nuevo producto y deseamos saber si será un éxito o un fracaso. Recopilamos datos de 20 productos similares lanzados anteriormente, con información sobre si fue un éxito o un fracaso, precio, presupuesto de marketing, precio de la competencia y diez variables más.**

- **Tipo de problema:** Clasificación.
- **Objetivo principal:** Predicción (determinar el éxito o fracaso del nuevo producto).
- **\( n \):** 20, **\( p \):** 13 (precio, presupuesto de marketing, etc.).

**c) Queremos predecir el cambio porcentual en el tipo de cambio USD/Euro en relación con los cambios semanales en los mercados bursátiles del mundo. Recolectamos datos semanales de todo 2012, registrando el cambio porcentual del USD/Euro y los cambios en los mercados de EE. UU., Reino Unido y Alemania.**

- **Tipo de problema:** Regresión.
- **Objetivo principal:** Predicción (predecir el cambio porcentual).
- **\( n \):** 52 (semanas de 2012), **\( p \):** 3 (cambios en los mercados bursátiles).

### 5. ¿Cuáles son las ventajas y desventajas de un enfoque muy flexible (en comparación con un enfoque menos flexible) para regresión o clasificación? ¿En qué circunstancias podría preferirse un enfoque más flexible sobre uno menos flexible? ¿Cuándo podría ser preferible un enfoque menos flexible?

**Ventajas de un enfoque flexible:**
- Permite modelar relaciones complejas y no lineales entre los predictores y la respuesta.
- Suele generar predicciones más precisas cuando la relación entre las variables es complicada.

**Desventajas de un enfoque flexible:**
- Mayor riesgo de sobreajuste, ya que puede ajustarse demasiado al ruido de los datos.
- Menor interpretabilidad y mayor complejidad en el modelo.
- Requiere más datos para evitar sobreajuste.

**Cuándo preferir un enfoque flexible:**
- Cuando las relaciones entre las variables son altamente no lineales o complejas y se dispone de una cantidad adecuada de datos.

**Cuándo preferir un enfoque inflexible:**
- Cuando se busca una mayor interpretabilidad del modelo o cuando las relaciones entre las variables son simples y lineales.

### 6. Describe las diferencias entre un enfoque paramétrico y uno no paramétrico en el aprendizaje estadístico. ¿Cuáles son las ventajas de un enfoque paramétrico para regresión o clasificación, en comparación con un enfoque no paramétrico? ¿Cuáles son sus desventajas?

- **Enfoque paramétrico:** Este enfoque asume una forma funcional específica para la relación entre los predictores y la respuesta (por ejemplo, lineal). La ventaja principal es que, al requerir estimar menos parámetros, el modelo es más sencillo y fácil de interpretar.
  - **Ventajas:** Simplicidad, facilidad de interpretación y menor requerimiento de datos.
  - **Desventajas:** Si el modelo asumido no refleja adecuadamente la realidad, puede generar un sesgo alto.

- **Enfoque no paramétrico:** No hace suposiciones sobre la forma funcional de la relación entre los predictores y la respuesta. Es más flexible y puede ajustarse mejor a relaciones complejas.
  - **Ventajas:** Mayor flexibilidad y capacidad de ajuste a datos no lineales.
  - **Desventajas:** Requiere más datos y puede ser menos interpretable.

### 7. El siguiente conjunto de datos contiene seis observaciones, tres predictores y una variable de respuesta cualitativa:

| Obs | X1   | X2   | X3  | Y    |
| --- | ---- | ---- | --- | ---- |
| 1   | 0    | 3    | 0   | Rojo |
| 2   | 2    | 0    | 0   | Rojo |
| 3   | 0    | 1    | 3   | Rojo |
| 4   | 0    | 1    | 2   | Verde|
| 5   | -1   | 0    | 1   | Verde|
| 6   | 1    | 1    | 1   | Rojo |

Suponiendo que queremos usar este conjunto de datos para hacer una predicción de \( Y \) cuando \( X1 = X2 = X3 = 0 \) utilizando el método de los K-vecinos más cercanos:

**a) Calcula la distancia euclidiana entre cada observación y el punto de prueba \( X1 = X2 = X3 = 0 \).**

**Observación 1:** = 3
**Observación 2:** = 2
**Observación 3:** = √10
**Observación 4:** = √5
**Observación 5:** = √2
**Observación 6:** = √3

**b) ¿Cuál es nuestra predicción con \( K = 1 \)? ¿Por qué?**

El punto más cercano es la observación 5 (distancia 1.41, clase Verde). La predicción es **Verde**.

**c) ¿Cuál es nuestra predicción con \( K = 3 \)? ¿Por qué?**

Las tres observaciones más cercanas son la observación 5 (Verde), la 6 (Rojo) y la 2 (Rojo). La predicción es **Rojo** (2 votos a favor de Rojo, 1 a favor de Verde).

**d) Si la frontera de decisión de Bayes en este problema es altamente no lineal, ¿esperaríamos que el mejor valor de \( K \) sea grande o pequeño? ¿Por qué?**

Se esperaría que \( K \) sea **pequeño**. Un valor pequeño de \( K \) permite capturar mejor la complejidad de una frontera no lineal, mientras que un \( K \) grande suavizaría demasiado la frontera y no capturaría las variaciones importantes.
