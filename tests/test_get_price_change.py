import pytest
from datetime import datetime, timedelta
from main import get_price_change


@pytest.fixture
def product_data():
    now = datetime.now()
    return {
        "Шампунь": [
            (now - timedelta(days=10), 150.0),
            (now - timedelta(days=5), 160.0),
            (now - timedelta(days=2), 155.0)
        ],
        "Крем": [
            (now - timedelta(days=40), 200.0),
            (now - timedelta(days=35), 195.0)
        ],
        "Гель": [
            (now - timedelta(days=2), 180.0),
            (now - timedelta(days=1), 180.0)
        ]
    }

@pytest.mark.parametrize("product_name, expected_output", [
    ("Шампунь", "Ціна на 'Шампунь' зросла на 5.00 грн за останній місяць."),
    ("Крем", "Немає даних за останній місяць для 'Крем'."),
    ("Гель", "Ціна на 'Гель' не змінилась на 0.00 грн за останній місяць."),
    ("Мило", "Товар 'Мило' не знайдено у файлі.")
])
def test_get_price_change(product_data, product_name, expected_output):
    assert get_price_change(product_data, product_name) == expected_output