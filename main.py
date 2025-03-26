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



if __name__ == "__main__":
    file_path = "products.txt"
    products = read_product_data(file_path)
    print(products)
