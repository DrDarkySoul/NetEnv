import json


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


class Environment(object):
    def __init__(self):
        self.path = "config/Environment.json"
        self.topology = {}
        self.nodes_number = 0
        with open(self.path) as config:
            raw_topology = json.load(config)
            if check_topology(raw_topology):
                self.nodes_number = raw_topology['number_nodes']
                self.topology = raw_topology['nodes']

    def print(self):
        nodes_num = self.nodes_number
        nodes = self.topology
        print(f"The network consists of {nodes_num} nodes:")
        for index, node in enumerate(nodes):
            index += 1
            indexes = [i + 1 for i, v in enumerate(node) if v == 1]
            print(f"Node №{index} connected with {indexes} nodes:")


e = Environment()
e.print()
