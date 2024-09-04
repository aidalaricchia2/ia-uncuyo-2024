import node as n
from collections import deque
import environment as e
import time

def bfs(env):
    nombre = "BFS"
    start_time = time.time()
    
    # Crear el nodo inicial
    nodo = n.Nodo(env.initial_state, None)
    
    # Caso en que initial_state = final_state
    if nodo.goal_test(env.final_state):
        return nodo, 0, 0, 0
    
    # Crear una cola FIFO (frontera)
    frontier = deque([nodo])
    
    # Diccionario para almacenar los estados explorados
    explored = set()
    
    # Contadores
    first_cost = 0 # escenario 1
    second_cost = 0 # escenario 2
    
    while frontier:
        # Extraer el nodo de la frontera
        node = frontier.popleft()
        
        # Guardarlo en los explorados (clave primaria su ubicacion (x, y))
        explored.add(node.estado)
        
        actions, action_number = node.possible_actions(env)
        first_cost += len(actions) # escenario 1
        
        for action in actions:
            action_cost = action_number.popleft()
            child = n.Nodo(action, node, action_cost)
            second_cost += action_cost + 1 # escenario 2
            if child.estado not in explored and child.estado not in (n.estado for n in frontier):
                if child.goal_test(env.final_state):
                    explored_amount = len(explored)
                    path, moves = solution(child)
                    end_time = time.time()
                    final_time = end_time - start_time
                    return path, moves, explored_amount, first_cost, second_cost, final_time, True, nombre
                
                frontier.append(child)

    end_time = time.time()
    final_time = end_time - start_time
    path, moves = solution(node)
    return path, moves, len(explored), first_cost, second_cost, final_time, False, nombre

def solution(child):
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
