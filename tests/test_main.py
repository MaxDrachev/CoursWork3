from Main.main import open_json, filter_operation, sort_operations, get_amount, hide_number_from, hide_number_to, \
    new_date
test_one = [
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

def test_open_json():
    assert type(open_json('test_file.json')) == list
    assert open_json('test_file.json') == [
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
    assert filter_operation(test_one) == []



def test_sort_operations():
    pass


def test_hide_number_from():
    pass


def test_get_amount():
    pass


def test_hide_number_to():
    pass


def test_new_date():
    pass

test_one = [
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