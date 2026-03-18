import numpy as np
from agent import VaccumCleaner
from environment import Environment


if __name__ == "__main__":
    # criar environment
    my_env = Environment(n_cols=5)
    # criar agente
    agent = VaccumCleaner()
    # adicionar agente ao ambiente
    my_env.add_agent(np.random.randint(len(my_env.room)))

    # for loop rodando a função do agente
    for i in range(20):
        my_env.render()
        # função do agente
        my_env = agent.act(my_env)
        input()
        if sum(my_env.room) == 0: # ambiente está todo limpo
            my_env.render()
            print("Finished cleaning room")
            break

