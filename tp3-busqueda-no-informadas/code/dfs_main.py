import numpy as np
import matplotlib.pyplot as plt
import environment as e
from dfs import dfs 
#from dfs import *
# Parámetros del experimento
num_trials = 30
size = 100
holes_rate = 0.08
seed = 12

explored_counts = []
first_costs = []
second_costs = []
times = []

for i in range(num_trials):
    env = e.Environment(size, holes_rate, seed + i)
    result = dfs(env)
    
    path, moves, explored_amount, first_cost, second_cost, final_time, found, _ = result
    
    if found:
        explored_counts.append(explored_amount)
        first_costs.append(first_cost)  
        second_costs.append(second_cost)
        times.append(final_time)

# Calcular medias y desviaciones estándar
explored_mean = np.mean(explored_counts) 
explored_std = np.std(explored_counts) 

first_cost_mean = np.mean(first_costs) 
first_cost_std = np.std(first_costs) 

second_cost_mean = np.mean(second_costs) 
second_cost_std = np.std(second_costs) 

time_mean = np.mean(times)
time_std = np.std(times) 

#Escenario 1
print("Escenario 1")
print(f"Cantidad de estados explorados - Media: {explored_mean}, Desviación estándar: {explored_std}")
print(f"Costo total - Media: {first_cost_mean}, Desviación estándar: {first_cost_std}")
print(f"Tiempo empleado - Media: {time_mean}, Desviación estándar: {time_std}")

#Escenario 2
print("Escenario 2")
print(f"Cantidad de estados explorados - Media: {explored_mean}, Desviación estándar: {explored_std}")
print(f"Costo total - Media: {second_cost_mean}, Desviación estándar: {second_cost_std}")
print(f"Tiempo empleado - Media: {time_mean}, Desviación estándar: {time_std}")

# Crear gráficos de cajas y bigotes
plt.figure(figsize=(20, 5))

# Gráfico de estados explorados
plt.subplot(1, 4, 1)
plt.boxplot(explored_counts if explored_counts else [[]])
plt.title('Estados Explorados')
plt.ylabel('Cantidad de Estados')

# Gráfico de costo total escenario 1
plt.subplot(1, 4, 2)
plt.boxplot(first_costs if first_costs else [[]])
plt.title('Costo Escenario 1')
plt.ylabel('Costo')

# Gráfico de costo total escenario 2
plt.subplot(1, 4, 3)
plt.boxplot(second_costs if second_costs else [[]])
plt.title('Costo Escenario 2')
plt.ylabel('Costo')

# Gráfico de tiempo empleado
plt.subplot(1, 4, 4)
plt.boxplot(times if times else [[]])
plt.title('Tiempo Empleado')
plt.ylabel('Tiempo (segundos)')

# Ajustar diseño y guardar la figura
plt.tight_layout()
plt.savefig('resultados_boxplots.png')

print("Gráficos guardados en 'resultados_boxplots.png'")
