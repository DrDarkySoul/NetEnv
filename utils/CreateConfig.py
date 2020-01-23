import json


def create_config():
    config = {'number_nodes': 8,
              'nodes': [
                  [0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 1, 1, 1, 0]]
              }
    with open('config/Network.json', 'w') as outfile:
        json.dump(config, outfile)


def create_template():
    config = {'size': 128,
              'masks': [
                  'AA19000000000019',
                  '3219000088000000',
                  '2424242424242424',
                  '3324000000000000',
                  '0000000000000512']
              }
    with open('config/Templates.json', 'w') as outfile:
        json.dump(config, outfile)
