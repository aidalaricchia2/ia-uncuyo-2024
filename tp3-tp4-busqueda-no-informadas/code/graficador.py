import numpy as np
import matplotlib.pyplot as plt
import environment as e
#from bfs import bfs
#from dfs import *
#from bcu import *
from pfl import depth_limited_search  # Importar la función correctamente

# Parámetros del experimento
num_trials = 30
size = 17
holes_rate = 0.08
seed = 12
limit = 10  # Definir el límite de profundidad

explored_counts = []
costs = []
times = []

for i in range(num_trials):
    env = e.Environment(size, holes_rate, seed + i)
    # Especificar el límite de profundidad
    result = depth_limited_search(env, limit)
    
    path, moves, explored_amount, first_cost, second_cost, final_time, found, _ = result
    
    if found:
        explored_counts.append(explored_amount)
        costs.append(first_cost)  # Usar first_cost si escenario 1 o segundo_cost para escenario 2
        times.append(final_time)

# Calcular medias y desviaciones estándar
explored_mean = np.mean(explored_counts) if explored_counts else 0
explored_std = np.std(explored_counts) if explored_counts else 0
cost_mean = np.mean(costs) if costs else 0
cost_std = np.std(costs) if costs else 0
time_mean = np.mean(times) if times else 0
time_std = np.std(times) if times else 0

print(f"Cantidad de estados explorados - Media: {explored_mean}, Desviación estándar: {explored_std}")
print(f"Costo total - Media: {cost_mean}, Desviación estándar: {cost_std}")
print(f"Tiempo empleado - Media: {time_mean}, Desviación estándar: {time_std}")

# Crear gráficos de cajas y bigotes
plt.figure(figsize=(12, 6))

# Gráfico de estados explorados
plt.subplot(1, 3, 1)
plt.boxplot(explored_counts if explored_counts else [[]])
plt.title('Estados Explorados')
plt.ylabel('Cantidad de Estados')

# Gráfico de costo total
plt.subplot(1, 3, 2)
plt.boxplot(costs if costs else [[]])
plt.title('Costo Total')
plt.ylabel('Costo')

# Gráfico de tiempo empleado
plt.subplot(1, 3, 3)
plt.boxplot(times if times else [[]])
plt.title('Tiempo Empleado')
plt.ylabel('Tiempo (segundos)')

# Ajustar diseño y guardar la figura
plt.tight_layout()
plt.savefig('resultados_boxplots.png')

print("Gráficos guardados en 'resultados_boxplots.png'")
