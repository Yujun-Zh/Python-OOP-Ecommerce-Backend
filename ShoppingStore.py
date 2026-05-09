from Product import Product

class ShoppingStore:

    def __init__(self):
        self.catalog = []


    def catalog_4m_file(self.datafile):
        catalog = list()  # catalog is a list of Product objects

        with open(datafile, mode='r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            pname, pid, price, category = line.split(',')
            pid = int(pid)
            price = float(price)
            new_product = Product(pname, pid, price, category)  # Object
            self.catalog.append(new_product)

    def view_catalog(self):

        print(f'***** Product Catalog *****')
        for product in self.catalog:
            print(product)
