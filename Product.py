class Product:

    def __init__(self, pname, pid, price, category):
        self.pname = pname
        self.pid = pid
        self.price = price
        self.category = category

    def __str__(self):  # print(product)
        line = f'Prod. ({self.pname},{self.pid},{self.price},{self.category})'
        return line

    def __repr__(self):  # print(list_of_product)
        line = f'\nProd. ({self.pname},{self.pid},{self.price},{self.category})'
        return line