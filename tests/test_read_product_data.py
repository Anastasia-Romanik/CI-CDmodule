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

