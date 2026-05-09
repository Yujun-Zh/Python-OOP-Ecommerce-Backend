from Product import Product
from ShoppingStore import ShoppingStore
from ShoppingCart import ShoppingCart

from ShoppingStore import catalog_4m_file

catalog = catalog_4m_file('data.txt')
print(catalog)

def main():

    mystore = ShoppingStore()  # Creates a shopping store object
    mystore.catalog_4m_file('data.txt')

    mycart = ShoppingCart()  # creates an empty shopping cart


    Main_Menu = '''*** Main Shopping Menu
    1. View Catalog
    2. Shopping Menu
    3. Check out
    4. Exit'''

    shop_menu = '''
    1. Add Product to Cart
    2. Remove Product from Cart
    3. View Cart
    4. Back to Main Menu'''


    while main_choice >0 :
        print(Main_Menu)
        main_prompt = 'Please enter your choice [1-4]: '
        main_choice = int(input(main_prompt))
        print(main_choice)

        if main_choice == 1: # View Catalog
            mystore.view_catalog()
        elif main_choice == 2: #Shopping Menu
            #=============================
            shop_choice = 0
            while shop_choice >= 0:
                print(shop_menu)
                shop_choice = int(input('Please enter your shopping choice [1-4]: '))

                if shop_choice == 1: # add to cart
                    data = input('Please enter pid, qty: ')
                    pid, qty = data.split(',')
                    pid = int(pid)
                    qty = int(qty)

                    # Step 1 - Find Product by the pid
                    prod_found = False
                    for prod in mystore.catalog:
                        if prod.pid == pid:
                            prod_found = True
                            break

                    # Step 2 - Add Product to cart
                    if prod_found:
                        mycart.add_to_cart(prod, qty) # add to mycart
                    else:
                        print('No Such Product Found!')

                elif shop_choice == 2:
                    pass
                elif shop_choice == 3:
                    mycart.view_cart()
                elif shop_choice == 4:  # Back to Main
                    break
                else:
                    print('\n Invalid Shop Choice ..  Try Again')

            #=============================
        elif main_choice == 3: #Check out
            pass
        elif main_choice == 4: #Exit
            print('Thank You!')
            print('Exiting the App')
            break
        else:
            print('\n\n\n Invalid Choice ... try again')
            main_prompt = 'Please enter your choice [1-4]: '
            main_choice = int(input(main_prompt))







if __name__ == '__main__':
    main()