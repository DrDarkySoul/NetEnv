import random
from SecurityTemplate import SecurityTemplate
from enum import Enum


class Kind(Enum):
    NO = 0,
    SAFE = 1,
    DANGER = 2


class TrafficGenerator:
    history = []
    checker = SecurityTemplate()

    def __init__(self, connections, size):
        self.connections = connections
        self.connections_number = len(self.connections)
        self.message_size = size

    def generate(self, kind=Kind.NO):
        connection_index = random.randint(0, self.connections_number - 1)
        connection = self.connections[connection_index]
        message = random.getrandbits(self.message_size)
        if kind == Kind.SAFE:
            check = True
            while check:
                if not self.checker.check(message):
                    check = False
                    break
                message = random.getrandbits(self.message_size)
        if kind == Kind.DANGER:
            check = True
            while check:
                if self.checker.check(message):
                    check = False
                    break
                message = random.getrandbits(self.message_size)
        note = {'connection': connection, 'message': message}
        self.history.append(note)

    def run(self, kind=Kind.NO, i=0):
        if i <= 0:
            while True:
                self.generate(kind)
        else:
            while i:
                self.generate(kind)
                i -= 1
