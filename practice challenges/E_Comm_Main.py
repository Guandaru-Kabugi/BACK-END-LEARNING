from E_commerce_Product_Inventory import *

def user_interface():
    print("Welcome to the E_Commerce Store")
    continue_playing = True
    while continue_playing:
        # user_choice = int(input('Select 1 to Add Product, 2 to See all Products, 3 to Update Products, 4 to Delete Products, 5 to Exit:  '))
        # user_choice = int(user_input)
        # if not isinstance(user_choice, int) or user_choice not in [1, 2, 3, 4, 5]:
        #         raise ValueError('Invalid choice, please select a valid option (1-5).') #using issistance
        try:
            user_input = input('Select 1 to Add Product, 2 to See all Products, 3 to Update Products, 4 to Delete Products, 5 to Exit:  ')
            if not user_input.isdigit(): #it helps ensure that when users input letters, they can get flagged.
                raise ValueError('Invalid choice, please enter a number.')
            user_choice = int(user_input)
            
            if user_choice not in [1, 2, 3, 4, 5]:
                raise ValueError('Invalid choice, please select a valid option (1-5).')
            match user_choice:
                case 1:
                    product_name = input("Please provide name of product:  ")
                    product_price = float(input("Please provide price of the product:  "))
                    product_quantity = int(input("Please provide quantity of the product:  "))
                    product_unit = input("Please say whether the product is in liters or grams:  ")
                    product = Product(product_name,product_price,product_quantity,product_unit)
                    product.add_product_to_database()
                case 2:
                    Product.read_display_inventory()
                case 3:
                    print("Here is a list of products in the inventory")
                    Product.read_display_inventory()
                    choice = int(input("What do you want to update: Select 1 for price and 2 for Quantity:  "))
                    Product.update_product_details(choice)
                case 4:
                    print("Here is a list of products in the inventory")
                    Product.read_display_inventory()
                    id = int(input("Please input id of product to delete:  "))
                    Product.remove_product(id)
                case 5:
                    print("Goodbye")
                    continue_playing = False
                    os.system('cls')
                case _:
                    raise ValueError('Invalid choice')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    user_interface()
