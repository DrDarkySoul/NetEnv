from Network import Network


class Environment:
    network = Network()
    action_space = 2
    observation_space = 64
    info = ""

    def __init__(self):
        self.done = False

    def reset(self):
        self.done = False

    def step(self, action):
        observation = 0
        reward = 0
        done = self.done
        info = self.info
        return observation, reward, done, info
