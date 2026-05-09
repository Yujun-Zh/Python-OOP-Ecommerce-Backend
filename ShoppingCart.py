from Shoppingitem import ShoppingItem


class ShoppingCart:

    def __init__(self):
        self.cart = [] # Empty list of shopping items

    def add_to_cart(self, product, qty): # Find a product with the given pid
        new_item = ShoppingItem(product, qty)
        self.cart.append(new_item)
        print('Added to cart')

    def view_cart(self):
        print('\n *** Shopping Cart***')
        for item in self.cart:
            print(item.product, item.qty)

