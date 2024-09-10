class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        f = open(self.__file_name, "r")
        goods = f.read()
        f.close()
        return goods

    def add(self, *products):
        for product in products:
            if product.name and str(product.weight) in self.get_products():
                print(f"Продукт {product} уже есть в магазине")
            else:
                f = open(self.__file_name, "a")
                f.write(f"{product}\n")
                f.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
