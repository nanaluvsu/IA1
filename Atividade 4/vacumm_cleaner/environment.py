import numpy as np


class Environment:
    def __init__(self, n_cols):
        self.room = np.random.randint(low=0, high=2, size=n_cols)
        self.agent_location = None

    def add_agent(self, col_index):
        self.agent_location = col_index

    def render(self):
        print([str(i) for i in self.room])
        agent_position = ["-" for i in self.room]
        agent_position[self.agent_location] = "X"
        print(agent_position)
