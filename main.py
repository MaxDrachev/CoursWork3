import json


def open_json():
    with open('operations.json', "r", encoding="utf-8") as file:
        return json.load(file)


def filter_operation(operations_data):
    filtered_list = []
    for operation in operations_data:
        if operation.get('state') == 'EXECUTED':
            filtered_list.append(operation)
    return filtered_list

def sort_operations(operations_data: list[dict]) -> list[dict]:
    sorted_list = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return sorted_list

def five_last_operations(operations):
    five_last_operations = slice(5)
    return operations[five_last_operations]


def haid_number_card(five_last_o):
    operation_from = five_last_o.get('from')
    operation_to = five_last_o.get('to')
    if operation_from:
        blocks = operation_from.split(' ')
        if len(blocks[-1]) == 16:
            print(blocks)
            hide_operation_from = f"{blocks[:-1]}"
        else:
            pass




operations_data = open_json()
operations = filter_operation(operations_data)
operations = sort_operations(operations)
five_last_o = five_last_operations(operations)

for i in five_last_o:
    print(haid_number_card(i))
#for i in five_last_o:
    #print(i)

#print(filter_operation(operations_data))


