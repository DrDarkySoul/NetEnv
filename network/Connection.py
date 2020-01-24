class Connection:
    from_ = -1
    to_ = -1

    def serialize(self):
        return {'from': self.from_, 'to': self.to_}

    def deserialize(self, ser):
        self.from_ = ser['from']
        self.to_ = ser['to']
