import json


class SerializedClass:
    a = 10
    string = "Ns gbljh"


file = {}
json.dump(SerializedClass(), file)
print(file)

