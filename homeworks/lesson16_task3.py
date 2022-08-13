class Product:

    def __init__(self, _type, name, price):
        self.type = _type
        self.name = name
        self.price = price

    def __str__(self):
        return f'Type: {self.type}, Name: {self.name}, Price: {self.price}'

    def __repr__(self):
        return f'Type: {self.type}, Name: {self.name}, Price: {self.price}'


class ProductStore:

    def __init__(self, name):
        self.name = name
        self.profit = 0
        self.products = list()

    def add(self, product, amount):
        sale_price = round(product.price * 1.3, 2)
        self.products.append({'product': product, 'amount': amount, 'sale_price': sale_price, 'discount': 0})

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product in self.products:
            if getattr(product['product'], identifier_type) == identifier:
                product['discount'] = percent

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product['product'].name != product_name:
                continue

            if product['amount'] < amount:
                print('Quantity is not enough!')
                return

            sale_price = product['sale_price']
            sale_price -= round(sale_price * product['discount']/100, 2)

            if sale_price < product['product'].price:
                print('Selling below cost')
                return

            product['amount'] -= amount
            self.profit += round((sale_price - product['product'].price) * amount, 2)

    def get_income(self):
        return self.profit

    def get_all_products(self):
        for product in self.products:
            if product['amount'] > 0:
                print(product)

    def get_product_info(self, product_name):
        for product in self.products:
            if product['product'].name == product_name:
                return product['product'].name, product['amount']


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore('Kyiv')
s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
print(s.profit)
