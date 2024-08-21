import random
from environment import *
class Agent:
    def __init__(self, environment):
        self.environment = environment

    def choose_action(self, action):
        # Recibe la acción y la ejecuta
        return action

# Ejemplo de uso
env = Environment(5, 5, 2, 2, 0.4)  # Aumento el dirt_rate para mayor visibilidad de la suciedad
agent = Agent(env)

