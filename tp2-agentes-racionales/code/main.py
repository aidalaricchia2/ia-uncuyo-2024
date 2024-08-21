import random
import copy
from environment import *
from agent import  *

# Parámetros del entorno
size = int(input("Ingrese el tamaño: "))
init_posX = random.randint(0, size-1)
init_posY = random.randint(0, size-1)
dirt_rate= float(input("Ingrese porcentaje de suciedad en el tablero. Numero entre 0 y 1: "))
while dirt_rate<0 or dirt_rate>=1:
    dirt_rate= float(input("Ingrese porcentaje de suciedad en el tablero. Numero entre 0 y 1: "))

# Crear el entorno
env = Environment(size,size, init_posX, init_posY, dirt_rate)
env1=copy.deepcopy(env)

env1.print_environment()
env.print_environment()

agent_reflex = Agent(env)
agent_random = Agent(env1)
#Agente Random
for _ in range(1000):
    #env1.print_environment()
    action = random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha', 'Limpiar', 'NoHacerNada'])
    #print(f"Acción elegida: {action}")
    agent_action = agent_random.choose_action(action)
    env1.accept_action(agent_action)
print("Rendimiento final:", env1.get_performance())




#Agente Reflexivo
print('----------------')
env.print_environment()
for _ in range(1000):
    env.print_environment()
    action = input('Introduce la accion: Arriba, Abajo, Izquierda, Derecha, Limpiar, NoHacerNada: ')
    print(f"Acción elegida: {action}")
    agent_action = agent_reflex.choose_action(action)
    env.accept_action(agent_action)
print("Rendimiento final:", env.get_performance())






