import pytest
from unittest.mock import mock_open, patch
from datetime import datetime
from main import read_product_data


@pytest.fixture
def mock_file_data():
    return "Шампунь, 2025-03-01, 150.0\nШампунь, 2025-03-02, 140.0\nКрем, 2025-03-01, 200.0"


def test_read_product_data(mock_file_data):
    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        result = read_product_data("mock_file.txt")

    expected_result = {
        "Шампунь": [
            (datetime(2025, 3, 1), 150.0),
            (datetime(2025, 3, 2), 140.0)
        ],
        "Крем": [
            (datetime(2025, 3, 1), 200.0)
        ]
    }

    assert result == expected_result


def test_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        result = read_product_data("mock_file.txt")

    assert result == {}

# Параметризація для перевірки неправильного формату даних
@pytest.mark.parametrize("invalid_data, expected_exception", [
    ("Шампунь; 2025-03-01; 150.0\nШампунь; 2025-03-02; 140.0", ValueError),  # неправильний роздільник
    ("Шампунь, 03-01-2025, 150.0\nШампунь, 03-02-2025, 140.0", ValueError)     # неправильний формат дати
])
def test_invalid_format(invalid_data, expected_exception):
    with patch("builtins.open", mock_open(read_data=invalid_data)):
        with pytest.raises(expected_exception):
            read_product_data("mock_file.txt")