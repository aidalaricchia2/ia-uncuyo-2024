---
title: Introduccion

---

# Reporte trabajo practico 2
## Introducción

El objetivo de este proyecto es evaluar el desempeño de un agente reflexivo simple en el entorno clásico del mundo de la aspiradora, un modelo frecuentemente utilizado en el estudio de agentes inteligentes. Este entorno se caracteriza por ser una cuadrícula en la que la suciedad se distribuye aleatoriamente, y donde el agente tiene la tarea de limpiar la mayor cantidad posible de celdas sucias en un período determinado de 1000 acciones. El desafío radica en cómo las características del entorno, como el tamaño de la cuadrícula y el porcentaje de suciedad, afectan la eficiencia del agente en la realización de esta tarea.
## Marco Teorico

El mundo de la aspiradora es un entorno simplificado y ampliamente utilizado en la inteligencia artificial para estudiar el comportamiento de agentes racionales. En este modelo, el agente debe tomar decisiones basadas en las percepciones limitadas que tiene de su entorno inmediato y actuar para maximizar su rendimiento, definido en este caso como la cantidad de celdas limpiadas. El agente reflexivo simple actúa basándose en reglas predefinidas que responden directamente a las percepciones actuales, sin considerar un historial de acciones o consecuencias futuras. Este tipo de agente es útil para estudiar cómo decisiones simples pueden llevar a comportamientos efectivos en entornos dinámicos y parcialmente observables.

Además, se contrasta el desempeño del agente reflexivo con el de un agente aleatorio, que toma decisiones sin seguir ninguna estrategia específica. La comparación entre ambos agentes permite explorar cómo una estrategia simple y reflexiva puede mejorar el rendimiento frente a un comportamiento sin dirección.
## Diseño Experimental

Para evaluar el desempeño del agente reflexivo simple, se implementó un simulador que mide la eficiencia del agente en limpiar celdas sucias en distintos entornos. Se definieron siete tamaños de cuadrícula: 2×2, 4×4, 8×8, 16×16, 32×32, 64×64 y 128×128. Para cada tamaño, se establecieron cuatro niveles de suciedad en el entorno: 10%, 20%, 40% y 80%.

El experimento consistió en ejecutar el agente reflexivo en cada una de estas configuraciones de entorno, repitiendo la simulación 10 veces para cada combinación de tamaño de cuadrícula y porcentaje de suciedad. Posteriormente, se repitió el experimento utilizando un agente aleatorio, que selecciona sus acciones de manera no planificada.

Los resultados de estas pruebas permiten analizar la eficiencia del agente reflexivo en comparación con el agente aleatorio, evaluando cómo las características del entorno influyen en su rendimiento.
## Análisis y discusión de resultados
Resultados obtenido luego del analisis:
![agenteRandom](https://hackmd.io/_uploads/r1xDikno0.png)
![agenteReflexivo](https://hackmd.io/_uploads/HJxPoy2sR.png)
Ejemplo matriz 8x8 luego de una iteración:
![WhatsApp Image 2024-08-21 at 18.44.55](https://hackmd.io/_uploads/rycbnyhiR.jpg)
En los experimentos con agentes de limpieza en cuadrículas, ambos agentes (reflexivo simple y aleatorio) se comportan de manera similar en matrices pequeñas de 2x2 y 4x4. Sin embargo, a medida que se aumenta el tamaño de la cuadrícula, el agente reflexivo simple muestra una eficiencia significativamente mayor en comparación con el agente aleatorio.
## Conclusión

El estudio revela que un agente reflexivo simple demuestra una eficiencia significativamente mayor en comparación con un agente aleatorio, especialmente en cuadrículas de mayor tamaño. Mientras que el agente aleatorio opera sin ningún criterio, seleccionando acciones de manera aleatoria, el agente reflexivo sigue reglas específicas basadas en las percepciones del entorno, como limpiar cuando detecta suciedad. Esta ventaja se vuelve más evidente en cuadrículas grandes, donde el agente reflexivo puede gestionar mejor la complejidad del entorno. Aunque el agente reflexivo muestra un buen rendimiento en entornos pequeños o con alta densidad de suciedad, su eficacia disminuye en entornos grandes con baja densidad de suciedad, lo que sugiere que el desarrollo de agentes más sofisticados, que puedan adaptarse a diferentes condiciones del entorno, es crucial para mejorar la eficiencia en tareas de limpieza automatizadas.