import node as n
from collections import deque
import environment as e
import time

def dfs(env):
    nombre = "DFS"
    start_time = time.time()
    
    # Crear el nodo inicial
    nodo = n.Nodo(env.initial_state, None)
    
    # Caso en que initial_state = final_state
    if nodo.goal_test(env.final_state):
        return nodo
    
    # Crear una pila (stack) LIFO (frontera)
    frontier = deque([nodo])
    
    # Diccionario para almacenar los estados explorados
    explored = set()
    
    # Contadores
    first_cost = 0  # Escenario 1
    second_cost = 0  # Escenario 2
    move_count = 0  # Limite de movimientos
    explored_amount = 0  # Total de estados explorados
    
    while frontier and (move_count < 1000):
        # Extraer el nodo de la frontera (último nodo añadido, por ser LIFO)
        node = frontier.pop()
        
        # Guardarlo en los explorados (clave primaria su ubicación (x, y))
        explored.add(node.estado)
        
        # Obtener las acciones posibles y sus respectivos costos
        actions, action_number = node.possible_actions(env)
        first_cost += 1  # Escenario 1: Contador básico
        
        for action in actions:
            action_cost = action_number.popleft()  # Obtener el costo de la acción
            child = n.Nodo(action, node, action_cost)
            second_cost += action_cost + 1  # Escenario 2: Coste adicional de cada acción
            
            # Verificar si el estado del nodo hijo ya fue explorado o está en la frontera
            if child.estado not in explored and all(child.estado != n.estado for n in frontier):
                if child.goal_test(env.final_state):
                    # Se encontró una solución
                    explored_amount = len(explored)
                    path, moves = solution(child)
                    end_time = time.time()
                    final_time = end_time - start_time
                    return path, moves, explored_amount, first_cost, second_cost, final_time, True, nombre
                
                frontier.append(child)  # Agregar el nodo hijo a la frontera
        move_count += 1  # Incrementar el contador de movimientos

    # Si no se encontró solución dentro del límite de movimientos
    end_time = time.time()
    final_time = end_time - start_time
    path, moves = solution(node)                  
    return path, moves, explored_amount, first_cost, second_cost, final_time, False, nombre

def solution(child):
    """
    Esta función reconstruye el camino desde el nodo objetivo hasta el nodo inicial,
    recorriendo hacia atrás desde el nodo hijo (estado objetivo) hasta la raíz.
    """
    path = []
    moves = []
    # Añadir el estado del nodo objetivo
    path.append(child.estado)
    moves.append(child.action_number)
    # Recorrer hacia atrás hasta llegar al nodo raíz
    node = child.parent
    while node is not None:
        path.append(node.estado)
        moves.append(node.action_number)
        node = node.parent
    path.reverse()
    moves.reverse()
    return path, moves

# Código para probar la función
# env = e.Environment(100, 0.08, 9)  # size, percent, seed
# result = dfs(env)

def showMoves(moves, env):
    """
    Esta función muestra gráficamente los movimientos del agente en el entorno.
    """
    # Resetear el entorno para iniciar un nuevo episodio
    state = env.environment.reset()
    # Renderizar el entorno inicial
    env.environment.render()
    time.sleep(2)
    for i in range(1, len(moves)):
        time.sleep(0.5)
        next_state, reward, done, truncated, info = env.environment.step(moves[i])  
    env.environment.render()
    time.sleep(0.5)

# Código para visualizar la solución
# path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
# info = {
#     'algorithm_name': nombre,
#     'posición inicial agente': env.initial_state,
#     'posición objetivo': env.final_state,
#     'env_n': 0,
#     'camino generado': path,
#     'movimientos': moves,
#     'states_n': explored_amount,
#     'cost_e1': first_cost,  # escenario 1
#     'cost_e2': second_cost,  # escenario 2
#     'time': final_time,
#     'solution_found': found 
# }
# print(info)

# if found:
#     showMoves(moves, env)
