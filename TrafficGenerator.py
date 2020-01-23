import random


class TrafficGenerator:
    history = []

    def __init__(self, connections, size):
        self.connections = connections
        self.connections_number = len(self.connections)
        self.message_size = size

    def generate(self):
        connection_index = random.randint(0, self.connections_number - 1)
        connection = self.connections[connection_index]
        message = random.getrandbits(self.message_size)
        note = {'connection': connection, 'message': message}
        self.history.append(note)

    def run(self, i=0):
        if i <= 0:
            while True:
                self.generate()
        else:
            while i:
                self.generate()
                i -= 1
