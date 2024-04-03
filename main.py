import json
import datetime


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
    return sorted_list[:5]


def hide_number_from(operations):
    operation_from = operations.get('from')
    if operation_from:
        blocks = operation_from.split(' ')
        numbers = blocks[-1]
        if len(blocks[-1]) == 16:
            hide_operation_from = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            return f'{" ".join(blocks[:-1])} {hide_operation_from}'
        else:
            return f'Счет **{numbers[-4:]}'
    else:
        return f"Зачисление"


def get_amount(operations):
    amount = operations.get('operationAmount')
    amount_need = amount.get('amount')
    return amount_need


def hide_number_to(operations):
    operation_to = operations.get('to')
    if operation_to:
        checks = operation_to.split(' ')
        check = checks[-1]
        return f'Счет **{check[-4:]}'


def new_date(operations):
    data = operations['date']
    dt_data = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return dt_data.strftime("%d.%m.%Y")


operations_data = open_json()
operations = filter_operation(operations_data)
operations = sort_operations(operations)
for i in operations:
    print(f'{new_date(i)} {i['description']}')
    print(f'{hide_number_from(i)} -> {hide_number_to(i)}')
    print(f'{get_amount(i)}\n')
