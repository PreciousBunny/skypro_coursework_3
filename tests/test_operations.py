import pytest
from classes.operations import Operations


def test_operations_repr():
    operations = Operations([{"id": 1, "date": "2023-02-27T18:00:00", "description": "Operation 1", "state": "EXECUTED"}])
    expected_repr = [{"id": 1, "date": "2023-02-27T18:00:00", "description": "Operation 1", "state": "EXECUTED"}]
    assert operations.__repr__() == f"Operations({expected_repr})"


def test_operations_give_last_operations():
    all_operations = [
        {"id": 1, "date": "2023-02-27T18:00:00", "description": "Operation 1", "state": "EXECUTED"},
        {"id": 2, "date": "2023-03-01T09:00:00", "description": "Operation 2", "state": "EXECUTED"},
        {"id": 3, "description": "Operation 3", "state": "EXECUTED"}
    ]
    operations = Operations(all_operations)
    assert len(operations.last_operations) == 2
    assert operations.last_operations[0]['id'] == 2
    assert operations.last_operations[1]['id'] == 1


def test_date_reversed():
    assert Operations.date_reversed("2023-02-27T18:00:00") == "27.02.2023"


@pytest.fixture
def operations_instance():
    all_operations = [
        {
            "id": 1,
            "date": "2023-02-27T18:00:00",
            "description": "Operation 1",
            "from": "Account A",
            "to": "Account B",
            "operationAmount": {"amount": 9999, "currency": {"name": "USD"}},
            "state": "EXECUTED"

        },
        {
            "id": 2,
            "date": "2023-03-01T09:00:00",
            "description": "Operation 2",
            "from": "Account A",
            "to": "Account B",
            "operationAmount": {"amount": 9999, "currency": {"name": "USD"}},
            "state": "EXECUTED"
        },
        {
            "id": 3,
            "date": "2023-03-03T10:00:00",
            "description": "Operation 3",
            "operationAmount": {"amount": 6666, "currency": {"name": "RUB"}},
            "state": "EXECUTED"
        },
        {
            "id": 4,
            "date": "2023-04-01T12:00:00",
            "description": "Operation 4",
            "from": "Account A",
            "to": "Account B",
            "operationAmount": {"amount": 9999, "currency": {"name": "USD"}},
            "state": "EXECUTED"
        },
        {
            "id": 5,
            "date": "2023-05-01T15:00:00",
            "description": "Operation 5",
            "from": "Account A",
            "to": "Account B",
            "operationAmount": {"amount": 9999, "currency": {"name": "USD"}},
            "state": "EXECUTED"
        },
        {
            "id": 6,
            "date": "2023-06-10T09:00:00",
            "description": "Operation 6",
            "from": "Account A",
            "to": "Account B",
            "operationAmount": {"amount": 9999, "currency": {"name": "USD"}},
            "state": "CANCELED"
        }

    ]
    return Operations(all_operations)


def test_operations_output_last_operations(operations_instance, capsys):
    operations_instance.output_last_operations()
    captured = capsys.readouterr()
    assert "Операция: 2" in captured.out
    assert "01.04.2023 Operation 4" in captured.out
    assert "Статус: ОТМЕНЕНО" not in captured.out
    assert "Статус: ВЫПОЛНЕНО" in captured.out
    assert "6666 RUB" in captured.out