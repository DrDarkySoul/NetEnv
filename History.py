class History:
    log = []

    def write(self, connection, message, kind, mask=-1):
        self.log.append({'connection': connection, 'message': message, 'kind': kind, 'mask': mask})

    def reset(self):
        self.log = []
