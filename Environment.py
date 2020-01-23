import json
from TrafficGenerator import TrafficGenerator


def check_topology(config):
    size = config['number_nodes']
    arr = config['nodes']
    check_main_diag = [i for i in range(0, size) if arr[i][i] != 0]
    if len(check_main_diag) != 0:
        print("Error in topology config: side diagonal has non-zero element")
        return False
    check_symmetry = True
    for i in range(0, size):
        for j in range(0, size):
            if arr[i][j] != arr[j][i]:
                check_symmetry = False
    if not check_symmetry:
        print("Error in topology config: array not symmetrical on the side diagonal")
        return False
    return True


class Environment:
    path = "config/Environment.json"
    topology = {}
    nodes_number = 0
    connects = []
    connects_number = 0

    def __init__(self):
        with open(self.path) as config:
            raw_topology = json.load(config)
            if check_topology(raw_topology):
                self.nodes_number = raw_topology['number_nodes']
                self.topology = raw_topology['nodes']
                self.connects = self.get_connects()
                self.connects_number = len(self.connects)
                self.generator = TrafficGenerator(self.connects, 512)

    def print(self):
        nodes_num = self.nodes_number
        nodes = self.topology
        print(f"The network consists of {nodes_num} nodes:")
        for index, node in enumerate(nodes):
            indexes = [i for i, v in enumerate(node) if v == 1]
            print(f"Node №{index} connected with {indexes} nodes:")

    def has_connect(self, i, j):
        if self.topology[i][j] == 1:
            return True
        return False

    def get_connects(self):
        connects = []
        size = self.nodes_number
        for i in range(0, size):
            for j in range(0, size):
                if self.topology[i][j] == 1:
                    connects.append([i, j])
        return connects

    def print_history(self, k=100):
        for i in range(0, k):
            sending = self.generator.history[i]
            connect = sending['connection']
            from_ = connect[0]
            to_ = connect[1]
            msg = sending['message']
            print(f"From node №{from_} to node №{to_} message: {hex(msg)}")


e = Environment()
e.print()
e.generator.run(1000)
e.print_history()
