from datetime import datetime, timedelta

def read_product_data(file_path):
    products = {}
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            name, date_str, price = line.strip().split(', ')
            date = datetime.strptime(date_str, "%Y-%m-%d")
            price = float(price)
            if name not in products:
                products[name] = []
            products[name].append((date, price))
    return products


def get_price_change(products, product_name):
    if product_name not in products:
        return f"Товар '{product_name}' не знайдено у файлі."

    one_month_ago = datetime.now() - timedelta(days=30)
    filtered_prices = [(date, price) for date, price in products[product_name] if date >= one_month_ago]

    if not filtered_prices:
        return f"Немає даних за останній місяць для '{product_name}'."

    filtered_prices.sort()
    first_price = filtered_prices[0][1]
    last_price = filtered_prices[-1][1]

    price_diff = last_price - first_price
    trend = "зросла" if price_diff > 0 else "зменшилась" if price_diff < 0 else "не змінилась"

    return f"Ціна на '{product_name}' {trend} на {abs(price_diff):.2f} грн за останній місяць."

if __name__ == "__main__":
    file_path = "products.txt"
    products = read_product_data(file_path)
    product_name = input("Введіть назву товару: ")
    print(get_price_change(products, product_name))
