from unittest import mock

# if comment this import test fails becasue factory does not load
# DataCollectorCSV module
from data_cvs import DataCollectorCSV
from data_loader import DataLoader


class MockCollector(object):
    def get_patients(self):
        result = "mock"
        return result

# for "empty" test added other mock that return empty data


class MockCollectorEmpty(object):
    def get_patients(self):
        result = ""
        return result


def test_load_data_csv():
    dt = DataLoader()
    patients = dt.load_data()
    assert patients == "csv"


@mock.patch("data_loader.DataCollectorFactory.get_data_collector_instance")
def test_load_data_correct_loading(mock_get_collector_instance):
    mock_get_collector_instance.return_value = MockCollector()
    dt = DataLoader()
    patients = dt.load_data()
    print(patients)
    assert patients == "mock"


@mock.patch("data_loader.DataCollectorFactory.get_data_collector_instance")
def test_load_data_empty_result(mock_get_collector_instance):
    mock_get_collector_instance.return_value = MockCollectorEmpty()
    dt = DataLoader()
    patients = dt.load_data()
    print(patients)
    assert patients == ""
