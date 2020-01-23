import json


def create_config():
    config = {'number_nodes': 8}
    first_node   = [0, 0, 0, 1, 0, 0, 0, 0]
    second_node  = [0, 0, 0, 1, 0, 0, 0, 0]
    third_node   = [0, 0, 0, 1, 0, 0, 0, 0]
    fourth_node  = [1, 1, 1, 0, 0, 0, 0, 1]
    fifth_node   = [0, 0, 0, 0, 0, 0, 0, 1]
    sixth_node   = [0, 0, 0, 0, 0, 0, 0, 1]
    seventh_node = [0, 0, 0, 0, 0, 0, 0, 1]
    eighth_node  = [0, 0, 0, 1, 1, 1, 1, 0]
    config['nodes'] = \
        [first_node, second_node, third_node, fourth_node, fifth_node, sixth_node, seventh_node, eighth_node]

    with open('config/Environment.json', 'w') as outfile:
        json.dump(config, outfile)


def create_template():
    config = {'size': 128}
    masks = [
        'AA19000000000019',
        '3219000088000000',
        '2424242424242424',
        '3324000000000000',
        '0000000000000512'
    ]
    config['masks'] = masks

    with open('config/Templates.json', 'w') as outfile:
        json.dump(config, outfile)

create_template()
