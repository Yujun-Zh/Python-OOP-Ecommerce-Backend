from Product import Product

class ShoppingItem:

    def __init__(self, product, quantity):
        self.prod = product
        self.qty = quantity

    def __str__(self):
        line = f'Item.({self.prod.pname}, {self.prod.pid}, {self.prod.price}, Qty={self.qty})'
        return line



if __name__ == '__main__':

    pr = Product('Laptop', 123, 799.99, 'Electronics')
    print(pr)
    item = ShoppingItem(pr, 3)
    print(item)
