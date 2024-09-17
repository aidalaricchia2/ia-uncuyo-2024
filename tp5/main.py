import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ej1 import *
from ej2 import *

def ejecutar_algoritmos(n_values, num_runs=30, max_evaluations=1000):
    resultados = []
    for n in n_values:
        print(f"Ejecutando para N={n}")
        for run in range(num_runs):
            # Hill Climbing
            start_time = time.time()
            solucion_hc, h_hc, eval_hc = hill_climbing(n, max_evaluations)
            tiempo_hc = time.time() - start_time
            resultado_hc = {
                'Algoritmo': 'Hill Climbing',
                'N': n,
                'Run': run + 1,
                'Solucion': solucion_hc,
                'H': h_hc,
                'Optimo': h_hc == 0,
                'Tiempo': tiempo_hc,
                'Estados_Evaluados': eval_hc
            }
            resultados.append(resultado_hc)
            
            # Simulated Annealing
            start_time = time.time()
            solucion_sa, h_sa, eval_sa = simulated_annealing(n, max_evaluations)
            tiempo_sa = time.time() - start_time
            resultado_sa = {
                'Algoritmo': 'Simulated Annealing',
                'N': n,
                'Run': run + 1,
                'Solucion': solucion_sa,
                'H': h_sa,
                'Optimo': h_sa == 0,
                'Tiempo': tiempo_sa,
                'Estados_Evaluados': eval_sa
            }
            resultados.append(resultado_sa)
    
    return pd.DataFrame(resultados)


def guardar_csv(df, filename='resultados_nreinas.csv'):
    df.to_csv(filename, index=False)
    print(f"Resultados guardados en {filename}")


# -------------------- Cálculo de Estadísticas -------------------- #

def calcular_estadisticas(df):
    estadisticas = []
    grouped = df.groupby(['Algoritmo', 'N'])
    for (alg, n), group in grouped:
        total = len(group)
        exitos = group[group['Optimo'] == True]
        num_exitos = len(exitos)
        porcentaje_exitos = (num_exitos / total) * 100
        
        if num_exitos > 0:
            tiempo_promedio = exitos['Tiempo'].mean()
            tiempo_std = exitos['Tiempo'].std()
            estados_promedio = exitos['Estados_Evaluados'].mean()
            estados_std = exitos['Estados_Evaluados'].std()
        else:
            tiempo_promedio = None
            tiempo_std = None
            estados_promedio = None
            estados_std = None
        
        estadistica = {
            'Algoritmo': alg,
            'N': n,
            'Porcentaje_Exitos': porcentaje_exitos,
            'Tiempo_Promedio': tiempo_promedio,
            'Tiempo_Desviacion': tiempo_std,
            'Estados_Promedio': estados_promedio,
            'Estados_Desviacion': estados_std
        }
        estadisticas.append(estadistica)
    
    return pd.DataFrame(estadisticas)

# -------------------- Generación de Boxplots -------------------- #

def generar_boxplots(df, n_values):
    for n in n_values:
        subset = df[df['N'] == n]
        
        # Boxplot de Tiempos de Ejecución
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Algoritmo', y='Tiempo', data=subset)
        plt.title(f'Distribución de Tiempos de Ejecución para N={n}')
        plt.ylabel('Tiempo (segundos)')
        plt.xlabel('Algoritmo')
        plt.savefig(f'boxplot_tiempo_N{n}.png')
        plt.close()
        
        # Boxplot de Estados Evaluados
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Algoritmo', y='Estados_Evaluados', data=subset)
        plt.title(f'Distribución de Estados Evaluados para N={n}')
        plt.ylabel('Estados Evaluados')
        plt.xlabel('Algoritmo')
        plt.savefig(f'boxplot_estados_N{n}.png')
        plt.close()
    
    print("Boxplots generados y guardados como imágenes.")


#EJECUCION PRUEBAAAAA

n_values = [4, 8, 10,12,15]
    
# Ejecutar los algoritmos
df_resultados = ejecutar_algoritmos(n_values, num_runs=30, max_evaluations=1000)
    
# Guardar resultados en CSV
guardar_csv(df_resultados, 'resultados_nreinas.csv')

# Calcular estadísticas
df_estadisticas = calcular_estadisticas(df_resultados)
print("\nEstadísticas por Algoritmo y N:")
print(df_estadisticas)
    
# Guardar estadísticas en CSV
guardar_csv(df_estadisticas, 'estadisticas_nreinas.csv')
    
# Generar boxplots
generar_boxplots(df_resultados, n_values)