import json
import binascii


def unhexlify_array(arr):
    arr_bin = []
    for string in arr:
        arr_bin.append(binascii.unhexlify(string))
    return arr_bin


class SecurityTemplate:
    path = "config/Templates.json"

    def __init__(self):
        with open(self.path) as config:
            raw_template = json.load(config)
            self.size = raw_template['size']
            self.masks = raw_template['masks']
            self.masks_bin = unhexlify_array(self.masks)

    def check(self, msg):
        for template in self.masks_bin:
            if template == msg & template:
                return True
        return False
