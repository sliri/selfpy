# 7.2.6
#################


def shopping():
    """ This function does something ot lists """
    number = None
    while number != 0:
        shopping_str = input('Please enter a valid shopping list:')
        shopping_list = shopping_str.split(',')
        number = int(input('Please ente a number between 1-9:'))
        if number == 1:
            for product in shopping_list:
                print(product)
        elif number == 2:
            print(len(shopping_list))
        elif number == 3:
            checked_product = input('Please enter a product:')
            if checked_product in shopping_list:
                print('Product in shopping list')
            else:
                print('Product NOT in shopping list')
        elif number == 4:
            checked_product = input('Please enter a product:')
            print('You have', shopping_list.count(checked_product), 'repetitions')
        elif number == 5:
            checked_product = input('Please enter a product:')
            if checked_product in shopping_list:
                shopping_list.remove(checked_product)
            print(shopping_list)
        elif number == 6:
            checked_product = input('Please enter a product:')
            if not (checked_product in shopping_list):
                shopping_list.append(checked_product)
            print(shopping_list)
        elif number == 7:
            for product in shopping_list:
                if not (product.isalpha()) or len(product) < 3:
                    print(product)
        elif number == 8:
            for product in shopping_list:
                while shopping_list.count(product) > 1:
                    shopping_list.remove(product)
            print(shopping_list)
        elif number == 9:
            quit()
    quit()
