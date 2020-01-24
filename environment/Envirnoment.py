from network.Network import Network
from enums.Behavior import Behavior


class Environment:
    network = Network()
    action_space = 2
    observation_space = 64
    info = ""

    def __init__(self, behavior=Behavior.ONLY_SAFE):
        self.done = False
        self.behavior = behavior

    def reset(self):
        self.done = False

    def step(self, action):
        if (action != 0) & (action != 1):
            print("Wrong action")
            return -1, -1, False, ""

        note = self.network.step()

        # if()

        observation = 0
        reward = 0
        done = self.done
        info = self.info
        return observation, reward, done, info
