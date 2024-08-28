import random
import copy
from environment import *
from agent import  *

# Parámetros del entorno
#size = int(input("Ingrese el tamaño: "))
suma_random=0
suma_reflexivo=0

for i in range (10):
    print('Iteracion',i+1 )
    size = 128
    init_posX = random.randint(0, size-1)
    init_posY = random.randint(0, size-1)
    #dirt_rate= float(input("Ingrese porcentaje de suciedad en el tablero. Numero entre 0 y 1: "))
    dirt_rate=0.8
    while dirt_rate<0 or dirt_rate>=1:
        dirt_rate= float(input("Ingrese porcentaje de suciedad en el tablero. Numero entre 0 y 1: "))

    # Crear el entorno
    env = Environment(size,size, init_posX, init_posY, dirt_rate)
    env1=copy.deepcopy(env)



    agent_reflex = Agent(env)
    agent_random = Agent(env1)

    #env1.print_environment()
    #Agente Random
    for _ in range(1000):
        #env1.print_environment()
        action = random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha', 'Limpiar', 'NoHacerNada'])
        #print(f"Acción elegida: {action}")
        agent_action = agent_random.choose_action(action)
        if action == 'Limpiar' and env1.is_dirty: env1.accept_action('Limpiar')
        else:
            env1.accept_action(agent_action)
    print("Rendimiento final random:", env1.get_performance())
    suma_random=suma_random+env1.get_performance()
                                


    #Agente Reflexivo
    
    #env.print_environment()
    for _ in range(1000):
        #env.print_environment()
        action = random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha', 'NoHacerNada'])
        #print(f"Acción elegida: {action}")
        agent_action = agent_reflex.choose_action(action)
        if env.is_dirty : env.accept_action('Limpiar')

        env.accept_action(agent_action)
    print("Rendimiento final reflexivo:", env.get_performance())
    suma_reflexivo=suma_reflexivo+env.get_performance()
prom_random=suma_random/10
print('El promedio random : ', prom_random )
prom_reflex=suma_reflexivo/10
print('El promedio reflexivo : ', prom_reflex )




