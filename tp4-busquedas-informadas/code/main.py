import numpy as np
import matplotlib.pyplot as plt
import environment as e
import csv
import os

# Importar los algoritmos que desees ejecutar
from bfs import bfs  # Algoritmo BFS
from dfs import dfs  # Algoritmo DFS
from dls import dls  # Algoritmo DLS
from ucs import ucs  # Algoritmo UCS
from agent_random import random_agent  # Algoritmo Agente Aleatorio
from a_star import a_star  # Algoritmo A Estrella

# Parámetros del experimento
num_trials = 30
size = 100
holes_rate = 0.08
seed = 12

# Inicializar listas para almacenar los resultados
explored_counts = []
first_costs = []
second_costs = []
times = []

# Selección del algoritmo
algorithm_name = "AStar"  # Cambia esto a "BFS", "DLS", "UCS", "RandomAgent", "AStar" según el algoritmo a ejecutar

# Ejecutar el algoritmo seleccionado en el loop de pruebas
for i in range(num_trials):
    env = e.Environment(size, holes_rate, seed + i)
    
    # Llamada al algoritmo seleccionado
    if algorithm_name == "BFS":
        result = bfs(env)
    elif algorithm_name == "DFS":
        result = dfs(env)
    elif algorithm_name == "DLS":
        limit = 20  # Limite de profundidad para DLS
        result = dls(env, limit)
    elif algorithm_name == "UCS":
        result = ucs(env)
    elif algorithm_name == "RandomAgent":
        result = random_agent(env)
    elif algorithm_name == "AStar":
        result = a_star(env)

    
    path, moves, explored_amount, first_cost, final_time, found, nombre = result

    # Almacenar resultados solo si el objetivo fue encontrado
    if found:
        explored_counts.append(explored_amount)
        first_costs.append(first_cost)
        #second_costs.append(second_cost)
        times.append(final_time)

# Calcular medias y desviaciones estándar
explored_mean = np.mean(explored_counts) 
explored_std = np.std(explored_counts) 
first_cost_mean = np.mean(first_costs) 
first_cost_std = np.std(first_costs) 
#second_cost_mean = np.mean(second_costs) 
#second_cost_std = np.std(second_costs) 
time_mean = np.mean(times)
time_std = np.std(times) 

# Mostrar resultados
print("Resultados del Experimento:")
print(f"Cantidad de estados explorados - Media: {explored_mean:.2f}, Desviación estándar: {explored_std:.2f}")
print(f"Costo total - Media: {first_cost_mean:.2f}, Desviación estándar: {first_cost_std:.2f}")
print(f"Tiempo empleado - Media: {time_mean:.5f}, Desviación estándar: {time_std:.5f}")

# Guardar resultados en archivo CSV
csv_file = 'resultados_comparados.csv'

# Si el archivo no existe, escribir el encabezado
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["RESULTADO 30 EJECUCIONES EN N ENTORNOS DISTINTOS (PROMEDIO)", "", "", "", "", "", ""])
        writer.writerow(["", "BFS", "DFS", "DLS", "UCS", "RandomAgent", "AStar"])
        writer.writerow(["states_n", "", "", "", "", "", ""])
        writer.writerow(["cost_e1", "", "", "", "", "", ""])
        writer.writerow(["cost_e2", "", "", "", "", "", ""])
        writer.writerow(["time", "", "", "", "", "", ""])
        writer.writerow(["cont_found", "", "", "", "", "", ""])

# Guardar los resultados obtenidos en el archivo CSV según el algoritmo
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    if algorithm_name == "BFS":
        writer.writerow([f"states_n", explored_mean, "", "", "", "", ""])
        writer.writerow([f"cost_e1", first_cost_mean, "", "", "", "", ""])
        #writer.writerow([f"cost_e2", second_cost_mean, "", "", "", "", ""])
        writer.writerow([f"time", time_mean, "", "", "", "", ""])
        writer.writerow([f"cont_found", len(explored_counts), "", "", "", "", ""])
    elif algorithm_name == "DFS":
        writer.writerow([f"states_n", "", explored_mean, "", "", "", ""])
        writer.writerow([f"cost_e1", "", first_cost_mean, "", "", "", ""])
        #writer.writerow([f"cost_e2", "", second_cost_mean, "", "", "", ""])
        writer.writerow([f"time", "", time_mean, "", "", "", ""])
        writer.writerow([f"cont_found", "", len(explored_counts), "", "", "", ""])
    elif algorithm_name == "DLS":
        writer.writerow([f"states_n", "", "", explored_mean, "", "", ""])
        writer.writerow([f"cost_e1", "", "", first_cost_mean, "", "", ""])
        #writer.writerow([f"cost_e2", "", "", second_cost_mean, "", "", ""])
        writer.writerow([f"time", "", "", time_mean, "", "", ""])
        writer.writerow([f"cont_found", "", "", len(explored_counts), "", "", ""])
    elif algorithm_name == "UCS":
        writer.writerow([f"states_n", "", "", "", explored_mean, "", ""])
        writer.writerow([f"cost_e1", "", "", "", first_cost_mean, "", ""])
        #writer.writerow([f"cost_e2", "", "", "", second_cost_mean, "", ""])
        writer.writerow([f"time", "", "", "", time_mean, "", ""])
        writer.writerow([f"cont_found", "", "", "", len(explored_counts), "", ""])
    elif algorithm_name == "RandomAgent":
        writer.writerow([f"states_n", "", "", "", "", explored_mean, ""])
        writer.writerow([f"cost_e1", "", "", "", "", first_cost_mean, ""])
        #writer.writerow([f"cost_e2", "", "", "", "", second_cost_mean, ""])
        writer.writerow([f"time", "", "", "", "", time_mean, ""])
        writer.writerow([f"cont_found", "", "", "", "", len(explored_counts), ""])
    elif algorithm_name == "AStar":
        writer.writerow([f"states_n", "", "", "", "", "", explored_mean])
        writer.writerow([f"cost_e1", "", "", "", "", "", first_cost_mean])
        #writer.writerow([f"cost_e2", "", "", "", "", "", second_cost_mean])
        writer.writerow([f"time", "", "", "", "", "", time_mean])
        writer.writerow([f"cont_found", "", "", "", "", "", len(explored_counts)])
