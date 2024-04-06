import pytest
from CoursWork.Main.main import open_json, filter_operation, sort_operations, hide_number_from, hide_number_to, \
    new_date


def test_open_json():
    assert type(open_json('/Users/1/PycharmProjects/sky-python/CoursWork3/CoursWork/tests/test_file.json')) == list
    assert open_json('/Users/1/PycharmProjects/sky-python/CoursWork3/CoursWork/tests/test_file.json') == [
{
  "1": "3"
},
  {
    "2": "4"
  },
  {
    "3": "2"
  },
  {
    "4": "1"
  }
  ]


def test_filter_operation():
    assert filter_operation([{
    "id": 536723678,
    "state": "EXECUTED",
    "date": "2018-06-12T07:17:01.311610",
    "operationAmount": {
      "amount": "26334.08",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 4195191172583802",
    "to": "Счет 17066032701791012883"
  },
  {
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2018-12-28T23:10:35.459698",
    "operationAmount": {
      "amount": "49192.52",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 96231448929365202391"
  },
  {
    "id": 476991061,
    "state": "CANCELED",
    "date": "2018-11-23T17:47:33.127140",
    "operationAmount": {
      "amount": "26971.25",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Gold 7305799447374042",
    "to": "Maestro 3364923093037194"
  }]) == [{
    "id": 536723678,
    "state": "EXECUTED",
    "date": "2018-06-12T07:17:01.311610",
    "operationAmount": {
      "amount": "26334.08",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 4195191172583802",
    "to": "Счет 17066032701791012883"
  },
  {
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2018-12-28T23:10:35.459698",
    "operationAmount": {
      "amount": "49192.52",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 96231448929365202391"
  }]



def test_sort_operations():
    pass


def test_hide_number_from():
    assert hide_number_from({
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
    "operationAmount": {
      "amount": "40701.91",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 5999414228426353",
    "to": "Счет 72731966109147704472"
  }) == "Visa Gold 5999 41** **** 6353"
    assert hide_number_from({
      "id": 716496732,
      "state": "EXECUTED",
      "date": "2018-04-04T17:33:34.701093",
      "operationAmount": {
        "amount": "40701.91",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "to": "Счет 72731966109147704472"
    }) == "Зачисление"
    assert hide_number_from({
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 72731966109147704472"
    }) == "Счет **4368"



def test_hide_number_to():
    assert hide_number_to({
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 72731966109147704472"
    }) == "Счет **4472"


def test_new_date():
    assert new_date({
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 72731966109147704472"
    }) == "04.04.2018"
